from effects import *
from partybar import *
from colors import *
from commands import *

def intro():
    p = PartyBar()
    p.all(PURPLE)
    p.dim(.5)
    
    w = PartyBar()
    w.all(WHITE)
    w.dim(.8)

    r = PartyBar()
    r.all(RED)

    b = PartyBar()
    b.all(BLACK)

    c = Chase()

    # Riff
    c.add(SceneCommand(p, 0))
    c.add(SceneCommand(w, 5))
    # Response
    c.add(SceneCommand(p, 3))
    c.add(SceneCommand(r, 3.5))

    c.add(SceneCommand(p, 4.5))
    c.add(SceneCommand(w, 5))
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
    
    w = PartyBar()
    w.all(WHITE)

    c = Chase()
    
    #First g minor
    c.add(FadeCommand(None, p, 0, 0.5))
    c.add(FadeCommand(p, w, 2.5, 0.25))
    c.add(FadeCommand(w, p, 0.5, 0.4))
    c.add(FadeCommand(p, w, 1.5, .25))
    c.add(FadeCommand(w, p, 0.5, 0.4))
    c.add(FadeCommand(p, w, 1.5, .25))

    # Second g minor
    c.add(FadeCommand(None, p, 1.5, 0.5))
    c.add(FadeCommand(p, w, 2.5, 0.25))
    c.add(FadeCommand(w, p, 0.5, 0.4))
    c.add(FadeCommand(p, w, 1.5, .25))
    c.add(FadeCommand(w, p, 0.5, 0.4))
    c.add(SleepCommand(1.0))

    c.extend(fourstepmover(2, RED, WHITE))

    c.extend(c)

    for i in range(2):
        p2 = PartyBar()
        p2.set(ORANGE, PURPLE, PURPLE, ORANGE)
        c.add(FadeCommand(None, p2, 0, 0.5))
        c.add(FadeCommand(p2, w, 2.5, 0.25))
        c.add(FadeCommand(w, p2, 0.5, 0.4))
        c.add(FadeCommand(p, w, 1.5, .25))
        c.add(FadeCommand(w, p2, 0.5, 0.4))
        c.add(SleepCommand(1.0))
        c.extend(fourstepmover(2, RED, PURPLE))
        
    c.extend(cstrobe(RED, BLACK))
    c.extend(cstrobe(RED, BLACK))

    g = PartyBar()
    g.all(GREEN)
    r = PartyBar()
    r.all(RED)
    c.extend(onebardimmer(r))
    c.add(FadeCommand(None, g, 4, 0.5))
    c.add(SleepCommand(4))

    return c

def run(l):
    # count in
    l.run(fourstepmover(4, WHITE, BLACK))
    l.run(intro())
    l.run(montunos())
    
