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
PINK = (133, 26, 30)

def dim(c, a):
  return (int(floor(c[0]*a)), int(floor(c[1]*a)), int(floor(c[2]*a)))

def mix(c1, c2, a):
  return (int(floor(c1[0]-c2[0])*a + c2[0]),
          int(floor(c1[1]-c2[1])*a + c2[1]),
          int(floor(c1[2]-c2[2])*a + c2[2]))


def dechalkify(c, a):
  if c[0] == max(c[0], c[1], c[2]):
    return (c[0], int(floor(c[1]*a)), int(floor(c[2]*a)))
  if c[1] == max(c[0], c[1], c[2]):
    return (int(floor(c[0]*a)), c[1], int(floor(c[2]*a)))
  if c[2] == max(c[0], c[1], c[2]):
    return (int(floor(c[0]*a)), int(floor(c[1]*a)), c[2])
  
