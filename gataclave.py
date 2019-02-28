from effects import *
from partybar import *
from colors import *
from commands import *

def intro():
    c = Chase()

    # Riff
    c.add(SceneCommand(PartyBar.PURPLE, 0))
    c.add(SceneCommand(PartyBar.WHITE, 5))
    # Response
    c.add(SceneCommand(PartyBar.PURPLE, 3))
    c.add(SceneCommand(PartyBar.RED, 3.5))

    c.add(SceneCommand(PartyBar.PURPLE, 4.5))
    c.add(SceneCommand(PartyBar.WHITE, 5))
    c.add(SleepCommand(3))
    
    pr = PartyBar()
    pr.set(PURPLE, RED, RED, PURPLE)
    c.extend(onebardimmer(pr))
    c.add(SleepCommand(4))
    
    c.extend(strobe(pr, 1, 4))
    
    c.extend(c)

    return c

def montunos():
    p = PartyBar()
    p.set(PURPLE, GREEN, GREEN, PURPLE)
    p.dim(.7)
    
    c = Chase()
    
    #First g minor
    c.add(FadeCommand(None, p, 0, 0.5))
    c.add(FadeCommand(p, PartyBar.WHITE, 2.5, 0.25))
    c.add(FadeCommand(PartyBar.WHITE, p, 0.5, 0.4))
    c.add(FadeCommand(p, PartyBar.WHITE, 1.5, .25))
    c.add(FadeCommand(PartyBar.WHITE, p, 0.5, 0.4))
    c.add(FadeCommand(p, PartyBar.WHITE, 1.5, .25))

    # Second g minor
    c.add(FadeCommand(None, p, 1.5, 0.5))
    c.add(FadeCommand(p, PartyBar.WHITE, 2.5, 0.25))
    c.add(FadeCommand(PartyBar.WHITE, p, 0.5, 0.4))
    c.add(FadeCommand(p, PartyBar.WHITE, 1.5, .25))
    c.add(FadeCommand(PartyBar.WHITE, p, 0.5, 0.4))
    c.add(SleepCommand(1.0))

    c.extend(fourstepmover(2, RED, WHITE))

    c.extend(c)

    for i in range(2):
        p2 = PartyBar()
        p2.set(ORANGE, PURPLE, PURPLE, ORANGE)
        c.add(FadeCommand(None, p2, 0, 0.5))
        c.add(FadeCommand(p2, PartyBar.WHITE, 2.5, 0.25))
        c.add(FadeCommand(PartyBar.WHITE, p2, 0.5, 0.4))
        c.add(FadeCommand(p, PartyBar.WHITE, 1.5, .25))
        c.add(FadeCommand(PartyBar.WHITE, p2, 0.5, 0.4))
        c.add(SleepCommand(1.0))
        c.extend(fourstepmover(2, RED, PURPLE))
        
    c.extend(cstrobe(RED, BLACK))
    c.extend(cstrobe(RED, BLACK))

    c.extend(onebardimmer(PartyBar.RED))
    c.add(FadeCommand(None, PartyBar.GREEN, 4, 0.5))
    c.add(SleepCommand(4))

    return c

def run(l):
    # count in
    l.run(fourstepmover(4, WHITE, BLACK))
    l.run(intro())
    l.run(montunos())
    
