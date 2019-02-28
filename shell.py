from time import time

def count_and_run(l, scene):
    i = 0
    bpmSample = [0, 0, 0, 0]
    while i < 4:
        raw_input(">>")
        bpmSample[i] = time()
        i = i+1
    average = 0
    for i in range(3):
        average = average + (bpmSample[3-i]-bpmSample[3-(i+1)])
    average = average/3.0
    print("New bpm: " + str(60.0/average))
    raw_input()
    l.bpm = (60.0/average)
    l.runImmediately(scene)
    

def run(l, handler):
    bpmSample = [0, 0, 0, 0]
    while True:
        exec "import readline"
        exec "from effects import *"
        exec "from colors import *"
        exec "from partybar import PartyBar"
        r = raw_input(">>")
        if len(r) > 0:
#            try:
#            exec r
             handler(r)
#            except:
#                print("Error")
        else:
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
                        l.changeBpm(60/average)
                        print("BPM: " + str(60/average))
