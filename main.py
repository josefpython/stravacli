from strava_api import StravaClient
from sys import argv
import colorama
from flag import check_flags
from os import system

def main(args):

    caf = args[0]
    name = args[1]
    pw = args[2]

    client = StravaClient()
    client.authorise_user(caf,name,pw)
    nejblizsi_jidlo = client.get_menu()

    for t,n in nejblizsi_jidlo.items():
        if t[0] == "O":
            t = " " + t
        print(t,"\t",check_flags(n))

if __name__ == "__main__":

    colorama.init()

    try:
        system("cls")
        print("\n" + colorama.Back.CYAN + colorama.Fore.BLACK + "Nejbližší objednatelné jídlo je:" + colorama.Style.RESET_ALL)
        main(argv[1:])
        input("..")
    except:
        print("\n"+colorama.Fore.RED+"Něco se dojebalo, gn")