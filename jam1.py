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

    walk = fourstepmover(4, color1, color2)
    chill = fourstepmover(8, color2, colors.dim(color2, .1), 1.1)
    chill.loop = True
    walk.loop = True

    default = walk
    default.loop = True
    l.run(default)
    print("What would you like to do?")
    print("1. Cool fill 2. Freakout 3. Pulse 4. Walk")
    def handle_input(input):
        strippedInput = input.lstrip("i")
        immediate = False
        if strippedInput != input:
            immediate = True
        input = strippedInput

        def run(f):
            if immediate == True:
                l.runImmediately(f)
            else:
                l.run(f)

        if input == "1":
            print("Ok! Hold on dropping some dope beats in 4, 3, 2...")
            f = fourbarmover(color1, color2)
            run(f)
            l.run(chill)
        if input == "2":
            print("HOLD ON BUDDY")
            run(strobe(PartyBar().all(color3), 1/4.0, 4))
            l.run(chill)
        if input == "3":
            print("Nice and smooth")
            run(chill)
        if input == "4":
            print("To the dog park we go!")
            run(walk)

        
    shell.run(l, handle_input)
