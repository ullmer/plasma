# Simple animation against (on MS Windows) transparent window
# Brygg Ullmer, Clemson University
# Begun 2024-08-26

import sys; sys.path.append("..")

sys.settrace #to debug persistent segfault 

import pgzrun
import pygame
from functools    import partial
from pygame._sdl2 import Window, Renderer
from enoWinMgr    import *

WIDTH, HEIGHT = 300, 300

##################### transparency 08 example #####################

class exTransp08:

  a1Fn          = "animist01a_100"
  subwinProxyFn = "one_red_pix"

  a1              = None
  winCoordProxies = None
  numSubwins      = 3

  pRenderers      = None
  pWindows        = None

  dur             = 1.5 #duration
  fuchsia         = (255, 0, 128)  # Transparency key color

  justBeginning   = True
  animPhase1      = True
  pos1, pos2      = (0, 0), (500, 500)

  winDimension    = (250, 250)
  winCoords       = [(0, 0), (0, 300), (0, 600)]
  ewm             = None #enoWinMgr

  ############# constructor #############

  def __init__(self, **kwargs):

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

    self.a1 = Actor(self.a1Fn)
    self.winCoordProxies = {}
    self.pRenderers      = {}
    self.pWindows        = {}

    for i in range(self.numSubwins): self.winCoordProxies[i] = Actor("one_red_pix")

  ##################### first frame invocations #####################
  
  def firstFrame(self):

    if self.ewm is None: print("exTransp08 firstFrame: ewm is not initialized!"); return

    wh, ww = self.winDimension
    
    pWindows[0] = self.ewm.getWindow()
    n = self.numSubwins - 1

    for i in [1, n]: 
      # dictionaries work for storing window handle, but lists do not, because of pygame_sdl2's "deep copy" limitations
      self.pWindows[i]   = self.ewm.newWindow("win" + str(i), ww, wh) 

      self.pRenderers[i] = Renderer(self.pWindows[i])
  
    #pWindows = [window1] #this "deepcopy" is sufficient to cause a segfault; long, long sigh
  
    for i in range(3):
      x, y                   = winCoords[i]
      winCoordProxies[i].pos = winCoords[i]
      moveWindow(pWindows[i], x, y)
  
    transpWinSetup(screen, fuchsia, WIDTH, HEIGHT)                     #set up transparent window ~chromakey
    #transpWinSetup(pRenderers[1], fuchsia, WIDTH, HEIGHT, pWindows[1]) #set up transparent window ~chromakey
  
    animate(a1, pos=pos2, tween='accel_decel', duration=dur, on_finished=animTransition1)
  
    w1 = winCoordProxies[0]
    animate(w1, pos=(800,800), tween='accel_decel', duration=4.)
  
  ##################### animation transition #####################
  
  def animTransition1():
    global animPhase1
  
    if animPhase1:
      animPhase1 = False; animate(a1, pos=pos1, tween='accel_decel', duration=dur, on_finished=animTransition)
    else:
      animPhase1 = True;  animate(a1, pos=pos2, tween='accel_decel', duration=dur, on_finished=animTransition)
  
  ##################### draw #####################
  
  def draw(ewm):
    global pRenderers, pWindows, winCoordProxies
    global justBeginning
  
    if justBeginning: firstFrame(); justBeginning=False
  
    screen.fill(fuchsia)  # Transparent background ~chromakey
    a1.draw()
  
    for i in range(3):
     wp = winCoordProxies[i]
     x, y = wp.pos
     moveWindowById(i, x, y, pWindows)
  
    for i in [1,2]:
      pRenderers[i].clear()
      pRenderers[i].present()
  
  ewm = enoWinMgr()

##################### main #####################
  
def drawEwm(ewm): ewm.draw()
  
draw = partial(drawEwm, ewm)
  
pgzrun.go()

### end ###

