from partybar import PartyBar
from time import sleep
import copy

def DmxSent(status):
    return


#  global wrapper
#  if wrapper:
#    wrapper.Stop()

class Command():
    def doubletime(self):
        self.switchAfter = self.switchAfter / 2.0

class DimCommand(Command):
    def __init__(self, scene, after, target, duration):
        self.scene2 = PartyBar.clone(scene)

def makeDimCommand(c, after, target, duration):
    c2 = copy.deepcopy(c)
    c2.dim(target)
    return FadeCommand(c, c2, after, duration)

def makeReverseDimCommand(c, after, target, duration):
    c2 = copy.deepcopy(c)
    c2.dim(target)
    return FadeCommand(c2, c, after, duration)


class SceneCommand(Command):
  def __init__(self, scene, after):
    self.scene = scene
    self.switchAfter = after
  def run(self, universe, client, bpm, lastState):
    client.SendDmx(universe, self.scene.data, DmxSent)
    return self.scene.data

class SleepCommand(Command):
  def __init__(self, duration):
      self.switchAfter = duration
  def run(self, universe, client, bpm, lastState):
      return lastState

class FadeCommand(Command):
  def __init__(self, scene1, scene2, after, duration):
    self.switchAfter = after
    self.scene1 = scene1
    self.scene2 = scene2
    self.duration = duration
  def doubletime(self):
    self.switchAfter = self.switchAfter / 2.0
    self.duration = self.duration / 2.0
  def run(self, universe, client, bpm, lastState):
    src = self.scene1
    if src == None:
        src = PartyBar(lastState)

    fps = 30
    frames = 0.0
    fade_duration = 60.0/bpm * self.duration
    numFrames = fade_duration*fps
    while frames < numFrames:
      bb = PartyBar.blend(src, self.scene2, frames/numFrames)
      client.SendDmx(universe, bb.data, DmxSent)
      frames = frames+1
      sleep(fade_duration/numFrames)
    client.SendDmx(universe, self.scene2.data, DmxSent)
    return self.scene2.data
