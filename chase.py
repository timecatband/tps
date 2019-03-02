import copy
from commands import *

class Chase():
  def __init__(self):
    self.commands = []
    self.loop = False
    self.bpm = -1
  def addScene(self, scene, switchAfter):
    self.commands.append(SceneCommand(scene, switchAfter))
    return self
  def add(self, command):
    self.commands.append(command)
    return self
  def addMany(self, commands):
    for c in commands:
      self.add(c)
    return self
  def extend(self, other):
      self.commands.extend(copy.deepcopy(other.commands))
      return self
