from partybar import PartyBar
from time import sleep

def DmxSent(status):
    return


#  global wrapper
#  if wrapper:
#    wrapper.Stop()

class Command():
    def doubletime(self):
        self.switchAfter = self.switchAfter / 2.0


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
        print("Using src: " + str(src))

    fps = 120
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
