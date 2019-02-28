from math import floor

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 100, 0)

def mix(c1, c2, a):
  b = (0, 0, 0)
  return (int(floor((c1[0]+c2[0]*a) / 2.0)),
          int(floor((c1[1]+c2[1]*a) / 2.0)),
          int(floor((c1[2]+c2[2]*a) / 2.0)))
