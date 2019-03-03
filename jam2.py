from colors import *
from partybar import *
from chase import *
from commands import *
from effects import *
from random import random
import shell
import colors

ROYALRED = (RED, WHITE, YELLOW, PURPLE)
LUXURY = (YELLOW, RED, PURPLE, WHITE)
OCEANBLUE = (BLUE, CYAN, PURPLE, GREEN)
HALLOWEEN = (ORANGE, PURPLE, RED, GREEN)
SATANSFINGERS = (RED, PURPLE, ORANGE, RED)
FORESTGREEN = (GREEN, WHITE, BLUE, ORANGE)
GHOST = (GREEN, PURPLE, ORANGE, RED)

def ambientMover(duration, color, color2, fadeDivisor=1.1):
    c = Chase()
    color3 = mix(color, color2, 0.5)
    
    p1 = PartyBar().set(color, color3, color2, color3)
    p2 = PartyBar().set(color3, color, color3, color2)
    p3 = PartyBar().set(color2, color3, color, color3)
    p4 = PartyBar().set(color3, color2, color3, color)
    sceneDur = duration / 4.0
    
    c.add(FadeCommand(None, p1, 0, sceneDur/fadeDivisor))
    c.add(FadeCommand(p1, p2, sceneDur, sceneDur/fadeDivisor))
    c.add(FadeCommand(p2, p3, sceneDur, sceneDur/fadeDivisor))
    c.add(FadeCommand(p3, p4, sceneDur, sceneDur/fadeDivisor))
    c.add(SleepCommand(sceneDur))
    return c

def ambience1(color1, color2):
    scene1 = PartyBar().set(color1, color2, color2, color1)
    scene2 = PartyBar().set(color2, color1, color1, color2)
    scene3 = PartyBar().all(mix(color1, color2, 0.5))

    c = Chase()
    c.add(FadeCommand(None, scene1, 0, .4))

    c.addMany((FadeCommand(scene1, scene2, 0, 3.8),
               FadeCommand(scene2, scene3, 4, 3.8),
               FadeCommand(scene3, scene1, 4, 3.8),
               SleepCommand(4)))
    c.extend(ambientMover(8, color1, mix(color1, color2, 0.5), 1.1))
    c.add(FadeCommand(None, scene1, 0, 3.9))
    c.add(SleepCommand(4))
    c.loop = True
    return c

def secondAmbience(color1, color2):
    blended = mix(color1, color2, 0.5)
    p1 = PartyBar().set(blended, color2, color2, blended)
    p2 = copy.deepcopy(p1)
    p2.dim(0.5)
    c = Chase()
    c.addMany((
        FadeCommand(p1, p2, 0, 3.0),
        FadeCommand(p2, p1, 4, 3.0),
        SleepCommand(4)))
    c.extend(ambientMover(8, color1, blended, 1.1))
    c.extend(ambientMover(8, blended, color1, 1.1))
    c.add(FadeCommand(None, p1, 0, 0.5))
    c.loop = True
    return c

def indefstrobe(bpm, color):
#    p = PartyBar().all(color)
#    p.strobe(bpm)
#    c = Chase()
#    c.add(SceneCommand(p, 0))
    c = strobe(PartyBar().all(color), 1/8.0, 4)
    c.loop = True
    return c

def rapidAmbience(color1, color2):
    p1 = PartyBar().all(color1)
    p2 = PartyBar().all(color2)
    c = Chase()
    c.add(FadeCommand(None, p1, 0, 0.95))
    c.add(FadeCommand(p1, p2, 1, 0.95))
    c.loop = True
    return c

def chalkify(c):
    return (mix(c[0], WHITE, 0.8),
            mix(c[1], WHITE, 0.8),
            mix(c[2], WHITE, 0.8),
            mix(c[3], WHITE, 0.8))

CHALK = chalkify(HALLOWEEN)


def dechalkify(c):
    return (
        colors.dechalkify(c[0], 0.8),
        colors.dechalkify(c[1], 0.8),
        colors.dechalkify(c[2], 0.8),
        colors.dechalkify(c[3], 0.8))

def randomCc():
    return int(floor(random()*255))
def randomColor():
    return (randomCc(), randomCc(), randomCc())
def randomColorScheme():
    return (randomColor(), randomColor(), randomColor(), randomColor())

def jam(l, colorScheme):
    jam.colorScheme = colorScheme
    l.run(ambience1(jam.colorScheme[0], jam.colorScheme[1]))

    jam.lastInput = "1"

    def handle_input(input):
        if input == "1":
            l.runImmediately(ambience1(jam.colorScheme[0], jam.colorScheme[1]))
        if input == "2":
            l.runImmediately(secondAmbience(jam.colorScheme[0], jam.colorScheme[2]))
        if input == "3":
            l.runImmediately(indefstrobe(l.bpm, jam.colorScheme[3]))
            raw_input()
            l.runImmediately(ambience1(jam.colorScheme[0], jam.colorScheme[1]))
        if input == "4":
            m = fourstepmover(4, jam.colorScheme[0], jam.colorScheme[1])
            m.loop = True
            l.runImmediately(m)
        if input == "5":
            m = fourstepmover(2, jam.colorScheme[0], jam.colorScheme[1])
            m.loop = True
            l.runImmediately(m)
        if input == "6":
            m = fourstepmover(1, jam.colorScheme[0], jam.colorScheme[1])
            m.loop = True
            l.runImmediately(m)
        if input == "7":
            l.runImmediately(rapidAmbience(jam.colorScheme[0], jam.colorScheme[2]))
        if input == "8":
            jam.colorScheme = chalkify(jam.colorScheme)
            handle_input(jam.lastInput)
            input = jam.lastInput
        if input == "9":
            jam.colorScheme = dechalkify(jam.colorScheme)
            handle_input(jam.lastInput)
            input = jam.lastInput
        if input[0] == "c":
            input = input.lstrip("c")
            if input == "r":
                jam.colorScheme = randomColorScheme()
            else:
                jam.colorScheme = globals()[input]
            handle_input(jam.lastInput)
            input = jam.lastInput
        if input[0] == "-":
            l.bpm = l.bpm/2.0
            handle_input(jam.lastInput)
            input = jam.lastInput
        if input[0] == "=":
            l.bpm = l.bpm*2.0
            handle_input(jam.lastInput)
            input = jam.lastInput
        jam.lastInput = input


    shell.run(l, handle_input)
    print("After run shell")

def run(l):
    colorScheme = SATANSFINGERS
    jam(l, colorScheme)
    

