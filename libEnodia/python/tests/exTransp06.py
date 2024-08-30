# Simple animation against (on MS Windows) transparent window
# Brygg Ullmer, Clemson University
# Begun 2024-08-26

from enoTranspSetup import *
WIDTH, HEIGHT = 500, 500

a1      = Actor("animist01a_100")
w1      = Actor("animist01a_100") #... though we don't plan to draw w1; just animate

dur     = 1.5 #duration
fuchsia = (255, 0, 128)  # Transparency key color

justBeginning = True
animPhase1    = True
pos1, pos2    = (0, 0), (500, 500)

##################### first frame invocations #####################

def firstFrame():
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
  global justBeginning
  if justBeginning: firstFrame(); justBeginning=False

  screen.fill(fuchsia)  # Transparent background ~chromakey
  a1.draw()

  x, y = w1.pos
  moveWindow(None, x, y) #hacky, evolving
  

### end ###
