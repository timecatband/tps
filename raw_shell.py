import sys
import tty
import termios
from time import time

class RawShell():
    def __init__(self, lightdrummer):
        self.l = lightdrummer
    
    def handler(self, ch):
        return False

    def innerLoop(self):
        bpmSample = [0, 0, 0, 0]
        ch = ""
        while ch != "q": 
            ch = sys.stdin.read(1)
            if self.handler(ch) == False:
                bpmSample[3] = bpmSample[2]
                bpmSample[2] = bpmSample[1]
                bpmSample[1] = bpmSample[0]
                bpmSample[0] = time()
            
                average = 0
                goodSamples = 0
                for i in range(3):
                    if bpmSample[i] - bpmSample[i+1] < 1:
                        goodSamples = goodSamples + 1
                        average = average + (bpmSample[i]-bpmSample[i+1])
                        if goodSamples == 3 and average != 0:
                            average = average/goodSamples
                            print("BPM: " + str(60/average))
                            self.l.changeBpm(60/average)
    def run(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            self.innerLoop()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch        
        
        
