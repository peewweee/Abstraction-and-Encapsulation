import pyfiglet

def GUI():
    print("\033[0;35m ")
    title_text = " The Fan Class "
    title_line = title_text.center(150, "*")
    print(title_line)
    print("\033[0;32;40m ")
    calcu_banner = (pyfiglet.figlet_format("Phoebe's Fan Program", font="standard", width=150, justify="center"))
    print(calcu_banner)
    print("\033[0;36m")