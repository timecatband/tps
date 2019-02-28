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
    c.extend(twobardimmer(pr))
    c.add(SleepCommand(4))
    c.extend(c)

    return c

def run(l):
    # count in
    l.run(fourstepmover(4, WHITE, BLACK))
    l.run(intro())
    
