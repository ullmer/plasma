# Simple animation against (on MS Windows) transparent window
# Brygg Ullmer, Clemson University
# Begun 2024-08-26

#import pgzrun

from enoTranspSetup import *
from pygame._sdl2 import Window, Renderer
WIDTH, HEIGHT = 500, 500

a1      = Actor("animist01a_100")
w1      = Actor("animist01a_100") #... though we don't plan to draw w1; just animate

dur     = 1.5 #duration
fuchsia = (255, 0, 128)  # Transparency key color

justBeginning = True
animPhase1    = True
pos1, pos2    = (0, 0), (500, 500)

##################### first frame invocations #####################

pRenderers, pWindows = None, None

def firstFrame():
  global pRenderers, pWindows

  window1   = getWindow()
  #window2   = newWindow("second Window", 600, 600)

  #renderer1 = Renderer(window1)
  #renderer2 = Renderer(window2)
   
  #pWindows = [window1, window2]; pRenderers = [renderer1, renderer2]
  #moveWindow(window2, 300, 300)

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
  #window1 = pWindows[0]
  #moveWindow(window1, x, y)

  #renderer2.clear()
  #renderer2.present()

#pgzrun.go()

### end ###

