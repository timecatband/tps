from colors import *
from partybar import *
from chase import *
from commands import *
from effects import *
import shell

ROYALRED = (RED, WHITE, YELLOW, PURPLE)
LUXURY = (YELLOW, RED, PURPLE, WHITE)
OCEANBLUE = (BLUE, CYAN, PURPLE, GREEN)
HALLOWEEN = (ORANGE, PURPLE, GREEN, RED)

def ambientMover(duration, color, color2, fadeDivisor=1.5):
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
    p = PartyBar().all(color)
    p.strobe(bpm*2)
    c = Chase()
    c.add(SceneCommand(p, 0))
    return c

def rapidAmbience(color1, color2):
    p1 = PartyBar().all(color1)
    p2 = PartyBar().all(color2)
    c = Chase()
    c.add(FadeCommand(None, p1, 0, 0.5))
    c.add(FadeCommand(p1, p2, 1, 0.5))
    c.loop = True
    return c

def jam(l, colorScheme):
    l.run(ambience1(colorScheme[0], colorScheme[1]))

    def handle_input(input):
        if input == "1":
            l.runImmediately(ambience1(colorScheme[0], colorScheme[1]))
        if input == "2":
            l.runImmediately(secondAmbience(colorScheme[0], colorScheme[2]))
        if input == "3":
            l.runImmediately(indefstrobe(l.bpm, colorScheme[3]))
            raw_input()
            l.runImmediately(ambience1(colorScheme[0], colorScheme[1]))
        if input == "4":
            m = fourstepmover(4, colorScheme[0], colorScheme[1])
            m.loop = True
            l.runImmediately(m)
        if input == "5":
            m = fourstepmover(2, colorScheme[0], colorScheme[1])
            m.loop = True
            l.runImmediately(m)
        if input == "6":
            m = fourstepmover(1, colorScheme[0], colorScheme[1])
            m.loop = True
            l.runImmediately(m)
        if input == "7":
            l.runImmediately(rapidAmbience(colorScheme[0], colorScheme[2]))

    shell.run(l, handle_input)
    print("After run shell")

def run(l):
    colorScheme = HALLOWEEN
    jam(l, colorScheme)
    
