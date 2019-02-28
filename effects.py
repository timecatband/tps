from partybar import PartyBar
from chase import Chase
from commands import *
from colors import *
import copy

def fourstepmover(duration, color, background = BLACK):
    c = Chase()
    p0 = PartyBar()
    p1 = PartyBar()
    p1.l1(color)
    p1.l2(background)
    p1.l3(background)
    p1.l4(background)
    
    p2 = PartyBar()
    p2.l1(background)
    p2.l2(color)
    p2.l3(background)
    p2.l4(background)
    p3 = PartyBar()
    p3.l1(background)
    p3.l2(background)
    p3.l3(color)
    p3.l4(background)
    p4 = PartyBar()
    p4.l1(background)
    p4.l2(background)
    p4.l3(background)
    p4.l4(color)

    sceneDur = duration / 4.0
    
    c.add(FadeCommand(None, p1, 0, sceneDur/4))
    c.add(FadeCommand(p1, p2, sceneDur, sceneDur/4))
    c.add(FadeCommand(p2, p3, sceneDur, sceneDur/4))
    c.add(FadeCommand(p3, p4, sceneDur, sceneDur/4))
    c.add(SleepCommand(sceneDur))
    return c
    

def onebardimmer(pb):
  c = Chase()
  pb2 = PartyBar.clone(pb)
  pb2.dim(0)
  c.add(FadeCommand(pb, pb2, 0, 4))
  return c

def twobardimmer(pb):
  c = Chase()
  pb2 = PartyBar.clone(pb)
  pb2.dim(0)
  # If we run the dim for the whole measure we lose time to
  # hit the next beat
  c.add(FadeCommand(pb, pb2, 0, 3.75))
  c.add(FadeCommand(pb2, pb, 4, 3.75))
  return c

def doubletime(chase):
  c = copy.deepcopy(chase)
  for command in c.commands:
      command.doubletime()
  return c

def fourbardoubler(chase):
    c = Chase()
    c.extend(chase)
    c.extend(chase)
    chase = doubletime(chase)
    c.extend(chase)
    c.extend(chase)
    chase = doubletime(chase)
    c.extend(chase)
    c.extend(chase)
    c.extend(chase)
    c.extend(chase)
    return c

def fourbarmover(color, background):
    return fourbardoubler(fourstepmover(4, color, background))

def strobe(scene, beatdivision, duration):
    c = Chase()

    off = PartyBar.clone(scene)
    off.dim(0)
    
    numScenes = (1.0/beatdivision) * duration
    numScenes = numScenes / 2
    sceneDuration = beatdivision
    scenes = 0
    while scenes < numScenes:
        print("Adding commands" + str(scenes))
        c.add(SceneCommand(scene, 0))
        c.add(SceneCommand(off, beatdivision))
        c.add(SleepCommand(beatdivision))
        scenes = scenes+ 1

    return c

def cstrobe(color, dst):
    p = PartyBar()
    p.all(color)
    c = strobe(p, 1/2.0, 4.0)
    return c

