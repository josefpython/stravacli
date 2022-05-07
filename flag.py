import colorama

def check_flags(str):

    red = green = []

    with open("flags.flags", "r", encoding="utf-8") as f:
        flags = f.read().split("\n")
        red = flags[0].split(" ")
        green = flags[1].split(" ")

    str = str.replace(".", "").replace(",", "")
    strarr = str.split(" ")

    narr = []
    for word in strarr:
        if word.lower() in red:
            narr.append(colorama.Back.RED + word + colorama.Style.RESET_ALL)
        elif word.lower() in green:
            narr.append(colorama.Back.GREEN + word + colorama.Style.RESET_ALL)
        else:
            narr.append(word)


    return " ".join(narr)