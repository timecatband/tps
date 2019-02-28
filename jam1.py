from effects import *
import colors
import shell

def run(l):
    print("Hello Jammer! I am ISLA (Intelligent Spacedog Lighting Assistant")
    print("Please select a foreground color")
    s = raw_input(">")
    color1 = getattr(colors, s)
    print("Ok thanks. You're doing great. Now please select a background color")
    s = raw_input(">")
    color2 = getattr(colors, s)
    print("Now just select an effects color and we are ready to go!")
    s = raw_input(">")
    color3 = getattr(colors, s)

    print("Ok thanks! Those are great choices")

    default = fourstepmover(4, color1, color2)
    default.loop = True
    l.run(default)
    print("What would you like to do?")
    print("1. Cool fill 2. Freakout 3. Pulse")
    def handle_input(input):
        if input == "1":
            print("Ok! Hold on dropping some dope beats in 4, 3, 2...")
            f = fourbarmover(GREEN, WHITE)
            l.run(f)
            l.run(default)
        if input == "2":
            print("HOLD ON BUDDY")
            l.run(strobe(PartyBar().all(color3), 1/4.0, 4))
            l.run(default)
    shell.run(l, handle_input)
