from colors import *
from partybar import *
from chase import *
from commands import *
from effects import *
from random import random
from raw_shell import RawShell
import shell
import colors
import sys

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

class JamShell(RawShell):
    def __init__(self, l, colorScheme):
        self.l = l
        self.colorScheme = colorScheme
        self.lastInput = "1"
    def handler(self, input):
        if input == "1":
            self.l.runImmediately(ambience1(self.colorScheme[0], self.colorScheme[1]))
            return True
        if input == "2":
            self.l.runImmediately(secondAmbience(self.colorScheme[0], self.colorScheme[2]))
            return True
        if input == "3":
            self.l.runImmediately(indefstrobe(self.l.bpm, self.colorScheme[3]))
            sys.stdin.read(1)
            self.l.runImmediately(ambience1(self.colorScheme[0], self.colorScheme[1]))
            return True
        if input == "4":
            m = fourstepmover(4, self.colorScheme[0], self.colorScheme[1])
            m.loop = True
            self.l.runImmediately(m)
            return True
        if input == "5":
            m = fourstepmover(2, self.colorScheme[0], self.colorScheme[1])
            m.loop = True
            self.l.runImmediately(m)
            return True
        if input == "6":
            m = fourstepmover(1, self.colorScheme[0], self.colorScheme[1])
            m.loop = True
            self.l.runImmediately(m)
            return True
        if input == "7":
            self.l.runImmediately(rapidAmbience(self.colorScheme[0], self.colorScheme[2]))
            return True
        if input == "8":
            self.colorScheme = chalkify(self.colorScheme)
            self.handler(self.lastInput)
            input = self.lastInput
            return True
        if input == "9":
            self.colorScheme = dechalkify(self.colorScheme)
            self.handler(self.lastInput)
            input = self.lastInput
            return True
        if input[0] == "-":
            self.l.bpm = self.l.bpm/2.0
            self.handler(self.lastInput)
            input = self.lastInput
            return True
        if input[0] == "=":
            self.l.bpm = self.l.bpm*2.0
            self.handler(self.lastInput)
            input = self.lastInput
            return True
        return False
        self.lastInput = input

def jam(l, colorScheme):
    j = JamShell(l, colorScheme)
    l.run(ambience1(colorScheme[0], colorScheme[1]))

    j.run()

def run(l):
    colorScheme = ROYALRED
    jam(l, colorScheme)
    

