# Simple animation against (on MS Windows) transparent window
# Brygg Ullmer, Clemson University
# Begun 2024-08-26

import sys
sys.settrace #to debug persistent segfault 

import pgzrun
import pygame
from pygame._sdl2 import Window, Renderer
from enoTranspSetup import *

#DISPLAY_FLAGS = pygame.SHOWN
#pygame.display.set_mode((100, 100), DISPLAY_FLAGS)

WIDTH, HEIGHT = 500, 500

a1      = Actor("animist01a_100")
w1      = Actor("animist01a_100") #... though we don't plan to draw w1; just animate

dur     = 1.5 #duration
fuchsia = (255, 0, 128)  # Transparency key color

justBeginning = True
animPhase1    = True
pos1, pos2    = (0, 0), (500, 500)

##################### first frame invocations #####################

pRenderers, pWindows = {}, {}

def firstFrame():
  global pRenderers, pWindows 
  pWindows[0] = getWindow()
  pWindows[1] = newWindow("second Window", 600, 600) # this works, but a list does not, because of its "deep copy" mechanism
  #pWindows = [window1] #this "deepcopy" is sufficient to cause a segfault; long, long sigh

  pRenderers[1] = Renderer(pWindows[1])
   
  moveWindow(pWindows[1], 300, 300)

  transpWinSetup(screen, fuchsia, WIDTH, HEIGHT) #set up transparent window ~chromakey

  animate(a1, pos=pos2, tween='accel_decel', duration=dur, on_finished=animTransition)
  animate(w1, pos=(800,800), tween='accel_decel', duration=10)

##################### animation transition #####################

def animTransition():
  global animPhase1

  if animPhase1:
    animPhase1 = False; animate(a1, pos=pos1, tween='accel_decel', duration=dur, on_finished=animTransition)
  else:
    animPhase1 = True;  animate(a1, pos=pos2, tween='accel_decel', duration=dur, on_finished=animTransition)

##################### draw #####################

def draw():
  global pRenderers, pWindows
  global justBeginning

  if justBeginning: firstFrame(); justBeginning=False

  screen.fill(fuchsia)  # Transparent background ~chromakey
  a1.draw()

  x, y = w1.pos
  window1 = getWindow()
  moveWindow(window1, x, y)

  #renderer2 = pRenderers[1]
  #renderer2.clear()
  #renderer2.present()

pgzrun.go()

### end ###

