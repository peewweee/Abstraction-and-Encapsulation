import cowsay
def Header():
    print("\033[1;33m")
    cowsay.cow("Welcome! Get to know your pet.")
    print("\033[1;36m")

def Display():
    print("")
    print("\033[1;30;45m")
    display = "\N{cat face}ALL ABOUT YOUR PET\N{dog face}"
    display_center = display.center(120)
    print(display_center)
    print("\033[1;32;40m")