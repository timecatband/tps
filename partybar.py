import array
from math import floor
from colors import *

class PartyBar():
  def clone(other):
      pb = PartyBar()
      for i in other.data:
          pb.data.append(i)
      return pb
  def __init__(self, data=None):
      self.data = array.array('B')
      if data == None:
          self.data.append(0)
          self.data.append(255)
          for i in range(13):
              self.data.append(0)
      else:
          for i in data:
              self.data.append(i)
  def dim(self, amount):
    self.data[1] = int(floor(255*amount))
    return self

  def l1(self, color):
    self.data[3] = color[0]
    self.data[4] = color[1]
    self.data[5] = color[2]
    return self

  def l2(self, color):
    self.data[6] = color[0]
    self.data[7] = color[1]
    self.data[8] = color[2]
    return self

  def l3(self, color):
    self.data[9] = color[0]
    self.data[10] = color[1]
    self.data[11] = color[2]
    return self

  def l4(self, color):
    self.data[12] = color[0]
    self.data[13] = color[1]
    self.data[14] = color[2]
    return self

  def all(self, color):
    self.l1(color)
    self.l2(color)
    self.l3(color)
    self.l4(color)
    return self

  def set(self, c1, c2, c3, c4):
    self.l1(c1)
    self.l2(c2)
    self.l3(c3)
    self.l4(c4)
    return self

  def blend(p1, p2, a):
    dest = PartyBar()
    dest.data[1] = int(floor((p2.data[1]-p1.data[1])*a+p1.data[1]))
    for i in range(3,15):
      dest.data[i] = int(floor((p2.data[i]-p1.data[i])*a+p1.data[i]))
    return dest

PartyBar.RED = PartyBar().all(RED)
PartyBar.GREEN = PartyBar().all(GREEN)
PartyBar.BLUE = PartyBar().all(BLUE)
PartyBar.PURPLE = PartyBar().all(PURPLE)
PartyBar.BLACK = PartyBar().all(BLACK)
PartyBar.WHITE = PartyBar().all(WHITE)
PartyBar.CYAN = PartyBar().all(CYAN)
PartyBar.YELLOW = PartyBar().all(YELLOW)
PartyBar.ORANGE = PartyBar().all(ORANGE)

