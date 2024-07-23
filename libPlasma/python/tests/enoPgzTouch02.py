# Plasma Protein multitouch example
# Lead by Brygg Ullmer, Clemson University
# Begun 2024-07-20

#WIDTH  = 1920
#HEIGHT = 1080
WIDTH, HEIGHT = 800, 800

import os, sys, pathlib
sys.path.append("/home/ullmer/git/plasma/libPlasma/python/")
LIB_PATH = pathlib.Path(__file__).parents[1] #library in parent directory
sys.path.append(os.path.join(LIB_PATH, ''))

from proteinSchemas import *
from enoPgz         import *

touch_coords = {}
def normalizePos(x,y): return (int(x*WIDTH), int(y*HEIGHT))

############ finger -- potentially multitouch -- events ##########

def on_finger_down(finger_id, x, y):
  ix, iy                  = normalizePos(x,y)
  touch_coords[finger_id] = [ix,iy]

  multitouchDeposit([finger_id, ix, iy])
  print("finger DOWN", finger_id)

def on_finger_move(finger_id, x, y):
  ix, iy                  = normalizePos(x,y)
  touch_coords[finger_id] = [ix,iy]

  multitouchDeposit([finger_id, ix, iy])
  print("finger MOVE", ix, iy)

def on_finger_up(finger_id, x, y):
  print("finger UP")

################### "mouse" events ###################

def on_mouse_up(pos):
  print("mouse UP")
  touch_coords.clear()

################### draw ###################

def draw():
  screen.clear()
  screen.draw.circle((400, 300), 30, 'white')

  for finger_id in touch_coords:
    pos = touch_coords[finger_id]
    screen.draw.circle(pos, 50, 'white')

################### draw ###################

ps = proteinSchemas(schemaIndexPath='/home/ullmer/git/plasma/libPlasma/yaml')
cplasma.init("tcp://localhost/hello")
multitouchDeposit = ps.registerHwSensorDepositor('C2d_generic')

pgzx = enoPgz(["multitouch"])
pgzx.go()

### end ###

