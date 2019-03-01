from effects import *
from partybar import *
from colors import *
from commands import *
from shell import *

def intro():
    c = Chase()

    # Riff
    c.addMany((SceneCommand(PartyBar.PURPLE, 0),
              FadeCommand(PartyBar.WHITE, PartyBar.BLACK, 5, 2),
               # Response
               SceneCommand(PartyBar.PURPLE, 3),
               FadeCommand(PartyBar.RED, PartyBar.GREEN, 3.5, 2),

               SceneCommand(PartyBar.PURPLE, 4.5),
               FadeCommand(PartyBar.WHITE, PartyBar.GREEN, 5, 2),
               SleepCommand(3)))
    
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
    c.addMany(
        (FadeCommand(None, p, 0, 0.5),
        FadeCommand(p, PartyBar.WHITE, 2.5, 0.25),
        FadeCommand(PartyBar.WHITE, p, 0.5, 0.4),
        FadeCommand(p, PartyBar.WHITE, 1.5, .25),
        FadeCommand(PartyBar.WHITE, p, 0.5, 0.4),
        FadeCommand(p, PartyBar.WHITE, 1.5, .25)))

    # Second g minor
    c.addMany((FadeCommand(None, p, 1.5, 0.5),
               FadeCommand(p, PartyBar.WHITE, 2.5, 0.25),
               FadeCommand(PartyBar.WHITE, p, 0.5, 0.4),
               FadeCommand(p, PartyBar.WHITE, 1.5, .25),
               FadeCommand(PartyBar.WHITE, p, 0.5, 0.4),
               SleepCommand(1.0)))

    c.extend(fourstepmover(2, RED, WHITE))

    c.extend(c)

    for i in range(2):
        p2 = PartyBar()
        p2.set(ORANGE, PURPLE, PURPLE, ORANGE)
        c.addMany((FadeCommand(None, p2, 0, 0.5),
                   FadeCommand(p2, PartyBar.WHITE, 2.5, 0.25),
                   FadeCommand(PartyBar.WHITE, p2, 0.5, 0.4),
                   FadeCommand(p, PartyBar.WHITE, 1.5, .25),
                   FadeCommand(PartyBar.WHITE, p2, 0.5, 0.4),
                   SleepCommand(1.0)))
        c.extend(fourstepmover(2, RED, PURPLE))
        
    c.extend(cstrobe(RED, BLACK))
    c.extend(cstrobe(RED, BLACK))

    c.extend(onebardimmer(PartyBar.RED))
    c.add(FadeCommand(None, PartyBar.GREEN, 4, 0.5))
    c.add(SleepCommand(4))
    
    c.extend(c)

    return c

def verse():
    p1 = PartyBar()
    p1.set(PURPLE, CYAN, CYAN, PURPLE)
    p2 = PartyBar()
    p2.set(ORANGE, CYAN, CYAN, ORANGE)
    p3 = PartyBar()
    p3.set(ORANGE, BLUE, BLUE, ORANGE)
    p4 = PartyBar()
    p4.set(CYAN, PURPLE, PURPLE, CYAN)

    c = Chase()
    
    c.addMany((FadeCommand(p1, p2, 0, 3.8),
               FadeCommand(p2, p3, 4, 3.8),
               FadeCommand(p3, p4, 4, 3.8),
               FadeCommand(p4, p1, 4, 3.8),
               SleepCommand(4)))
    c.loop = True
    return c
    


def run(l):
    # count in
    l.run(fourstepmover(4, WHITE, BLACK))
    l.run(intro())
    l.run(montunos())
    l.run(verse())
    count_and_run(l, fourstepmover(4, ORANGE, PURPLE))
    l.run(intro())
    l.run(montunos())
    l.run(verse)
    count_and_run(l, fourstepmover(4, RED, WHITE))
