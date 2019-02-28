from commands import *
from colors import *
from partybar import *
from chase import *
from effects import *
from shell import *
from timelights import *

def buildVerse():
    b1 = PartyBar()
    b1.set(CYAN, WHITE, WHITE, CYAN)
    b2 = PartyBar()
    b2.set(WHITE, mix(BLUE, RED, 0.3), mix(BLUE, RED, 0.3), WHITE)
    
    c = Chase()
    c.add(SceneCommand(b1, 0))
    c.add(FadeCommand(b1, b2, 1, 1.8))
    c.add(FadeCommand(b2, b1, 3, 1.8))
    c.loop = True
    return c

def buildChorus():
    white = PartyBar()
    white.set(YELLOW, WHITE, WHITE, YELLOW)
    fill = cstrobe(PURPLE, white)
    chorus = Chase()

    blue = PartyBar()
    blue.set(BLUE, WHITE, WHITE, BLUE)
    blue2 = PartyBar()
    blue2.set(BLUE, CYAN, CYAN, BLUE)
    
    cyan = PartyBar()
    cyan.set(CYAN, WHITE, WHITE, CYAN)

    black = PartyBar()
    black.all(BLACK)

    for i in range(32): #32
        chorus.add(makeDimCommand(white, 0, 0.5, .8))
        chorus.add(makeDimCommand(blue, 1, 0.3, .8))
        chorus.add(makeDimCommand(blue2, 1, 0.3, .8))
        chorus.add(SleepCommand(1))
    print("Running chorus")

    red = PartyBar()
    red.all(RED)
    purple = PartyBar()
    purple.all(PURPLE)
    orange = PartyBar()
    orange.all(ORANGE)


    chorus.add(makeDimCommand(red, 0, 0.5, 3))
    chorus.add(makeReverseDimCommand(purple, 6, 0.2, 2))
    chorus.add(makeReverseDimCommand(orange, 3, 0.2, 2))
    chorus.add(SleepCommand(3))
    chorus.add(makeDimCommand(red, 0, 0.5, 3))
    chorus.add(makeReverseDimCommand(purple, 6, 0.2, 2))
    chorus.add(makeReverseDimCommand(orange, 3, 0.2, 2))
x    chorus.add(SleepCommand(3))

    # "Theres...a sound around"
    chorus.add(SceneCommand(white, 0))
    chorus.add(SceneCommand(purple, 6))
    chorus.add(SceneCommand(orange, 3))
    chorus.add(SleepCommand(3))
    chorus.add(SceneCommand(white, 0))
    chorus.add(SceneCommand(purple, 6))
    chorus.add(SceneCommand(orange, 3))
    chorus.add(SleepCommand(3))

    # Ramp
    for i in range(16):
        chorus.add(SceneCommand(red, 0))
        chorus.add(SceneCommand(orange, 0.5))
        chorus.add(SceneCommand(purple, 0.5))
        chorus.add(SleepCommand(0.5))
    return (fill, chorus)
    


def run(l):
    v = buildVerse()
    (fill, chorus) = buildChorus()

    l.run(v)
    count_and_run(l, fill)

    chorus.bpm = l.bpm * 2
    l.run(chorus)

    v.bpm = l.bpm / 2.0
    l.run(v)
    count_and_run(l, fill)
    l.run(chorus)



    
