#!/opt/local/bin/python2.7
from __future__ import print_function

import sys
sys.path.append("/opt/local/lib/python2.7/site-packages")

from ola.ClientWrapper import ClientWrapper
import array
import threading
import Queue
import signal

from math import floor
from math import ceil
from time import sleep
from time import time
import readline

# Spacebat
from colors import *
from commands import *
from chase import Chase
from effects import *
from partybar import PartyBar
import shell

wrapper = None

class StoppableClient():
  def __init__(self, client):
    self.client = client
    self.disabled = False
  def SendDmx(self, universe, data, done):
    if self.disabled == False:
      self.client.SendDmx(universe, data, done)

class QuitCommand(): pass

class LightDrummer():
  def __init__(self, client, bpm):
    # We don't grant the underlying client to runner threads, and instead grant them a "Stoppable"
    # wrapper client, so that these threads can be cancelled while fades are running and they aren't
    # pulling commands from the queue
    self.underlyingClient = client

    self.bpm = bpm
    # Used to retarget the phase when fixing BPM
    self.nextBeatTime = -1

    # The last client and queue we started a thread with: used for cancelling
    self.lastClient = None
    self.lastQueue = None

    self.universe = 1

    self.startThread()
  
  def startThread(self):
    # If we have an existing thread, we send it a QuitCommand and immediately disable a client.
    # This is the technique for interrupting fades
    if self.lastQueue != None:
      self.lastQueue.put(QuitCommand())
    if self.lastClient != None:
      self.lastClient.disabled = True

    self.lastQueue = Queue.Queue()
    self.lastClient = StoppableClient(self.underlyingClient)
    self.thread = threading.Thread(target=self.lightDrum, args=(self.lastClient,self.lastQueue))
    self.thread.setDaemon(True)
    self.thread.start()

  def runImmediately(self, command):
    self.startThread()
    self.run(command)

  def run(self, command):
    self.lastQueue.put(command)
  
  def runCommand(self, command):
    self.lastQueue.put(Chase().add(command))

  def runScene(self, scene):
    self.runCommand(SceneCommand(scene, 0))

  def changeBpm(self, newBpm):
    self.bpm = newBpm
    self.nextBeatTime = time() + 60.0/newBpm

  # The main executor thread
  def lightDrum(self, client, queue):
    chase = None
    lastState = PartyBar().all(WHITE).data

    while True:
      if chase != None and chase.loop == True:
        try:
          chase = queue.get(False)
        except:
          pass
      else:
        chase = queue.get()
      if chase == None:
        chase = queue.get()
      if client.disabled == True:
        return
      beatPos = 0
      startTime = time()
      
      if chase.bpm > 0:
        self.bpm = chase.bpm

      for command in chase.commands:
        beatPos = beatPos + command.switchAfter

        if self.nextBeatTime > 0:
          nextBeatPos = ceil(beatPos)
          startTime = self.nextBeatTime - nextBeatPos*(60.0/self.bpm)
          self.nextBeatTime = -1

        expectedTime = startTime + beatPos*(60.0/self.bpm)

        wait = expectedTime - time()
        if wait > 0:
          sleep(wait)

        lastState = command.run(self.universe, client, self.bpm, lastState)

def main():
  global wrapper
  wrapper = ClientWrapper()
  client = wrapper.Client()

  global l
  l = LightDrummer(client, 140)

  # Intro
  pb2 = PartyBar()
  pb2.set(PURPLE, BLUE, BLUE, PURPLE)
  l.run(twobardimmer(pb2))

  def handle_input(input):
    exec input in globals(),globals()


  shell.run(l, handle_input)

def signal_handler(signal, frame):
    sys.exit(0)

if __name__ == '__main__':
  signal.signal(signal.SIGINT, signal_handler)
  main()

