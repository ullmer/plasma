# Enodia PyGame Zero example of simple multitouch
# Brygg Ullmer, Clemson University
# Begun 2022-06-16

import sys; sys.path.append("/home/ullmer/git/plasma/libPlasma/python/")

from enoPgz import *

WIDTH  = 600
HEIGHT = 600

touch_coords = {} # dictionary with coordinates of active touches
  
def normalizePos(x,y): return (int(x*WIDTH), int(y*HEIGHT))

############ finger -- potentially multitouch -- events ##########

def on_finger_down(finger_id, x, y):
  touch_coords[finger_id] = normalizePos(x,y)

def on_finger_move(finger_id, x, y):
  touch_coords[finger_id] = normalizePos(x,y)

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

pgzx = enoPgz(["multitouch"])
pgzx.go()

### end ###
