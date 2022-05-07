from requests_html import HTMLSession, HTML

class AuthenticationError(Exception):
    pass

class StravaClient:

    def __init__(self) -> None:
        self.cookie_jar = None
        self.session_object = HTMLSession()

    def authorise_user(self, jidelna, jmeno, heslo):
        try:

            data = data={"zarizeni": jidelna, "uzivatel": jmeno, "heslo": heslo}
            r = self.session_object.post("https://www.strava.cz/Strava/Stravnik/prihlaseni", data=data)

            if r.url != "https://www.strava.cz/Strava/Stravnik/Uvod":
                raise AuthenticationError

            self.cookie_jar = r.cookies
            return 200

        except Exception:
            return 401

    def get_menu(self):

        if self.cookie_jar != None:
           
            r = self.session_object.get("https://www.strava.cz/Strava/Stravnik/Objednavky", cookies=self.cookie_jar)
            txt = HTML(html=r.text)
            menu_wrapped = [food for food in txt.find(".objednavka-obalka")]

            i=0
            while True:
                if (menu_wrapped[i].find(".zaskrtavaciPolicko-povolene")) != []:
                    break
                i+=1
            
            closest_foods = {}
            jmena = []
            typy = []

            for f in menu_wrapped[i].find(".objednavka-jidlo-popis"):
                typy.append(f.text)
            for f in menu_wrapped[i].find(".objednavka-jidlo-nazev"):
                jmena.append(f.text)            
            for a,jidlo in enumerate(jmena):
                closest_foods[typy[a]] = jidlo
            
            return closest_foods

        else:
            return 401