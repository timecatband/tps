from effects import *
import shell

def run(l):
    c = fourstepmover(4, GREEN, WHITE)
    c.loop = True
    l.run(c)
    def handle_input(input):
        print("Handling input")
        if input == "1":
            print("Engaging mover")
            c = fourbarmover(GREEN, WHITE)
            l.run(c)
            c2 = fourstepmover(4, GREEN, WHITE)
            c2.loop = True
            l.run(c2)
    shell.run(l, handle_input)
