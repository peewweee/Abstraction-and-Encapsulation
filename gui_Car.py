import pyfiglet

def GUI():
    print("\033[1;33;40m ")
    calcu_banner = (pyfiglet.figlet_format("Car Class", font="isometric1", width=150, justify="center"))
    print(calcu_banner)
    print("\033[0;36m")