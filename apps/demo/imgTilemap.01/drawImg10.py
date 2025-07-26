# Navigate a tiled image 
# Brygg Ullmer, Clemson University
# Begun 2023-03-22

import os

os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0' #place window at top-left
WIDTH, HEIGHT = 1920, 1080

import pgzrun

from enoTiledImg     import *
from enoTiledImgNav  import *
from enoPlasmaImgNav import *
import sys

#tmdn = 'rmUS1882a'
#tmdn = 'cuMap2'
tmdn = 'rmUS1882b'

offsetX, offsetY = 0, 0
multiplier = 0
try:
  if len(sys.argv) > 1: # we have a command-line argument; multiplier for offset
    multiplier = int(sys.argv[1])
    offsetX = multiplier * WIDTH
except: print("command-line argument noted, but doesn't seem to be a multiplier")

eti    = EnoTiledImg(verbose=False)
etinav = EnoTiledImgNav(eti)
eti.imgPos = (-1*offsetX, -1*offsetY)

eti.adjustWindowPlacement(WIDTH, HEIGHT)
eti.loadTmap(tmdn)

epin = EnoPlasmaImgNav()
epin.registerMapMoveCb(etinav.plasmaMoveCb)              #listen
etinav.setPlasmaMoveDeposit(epin.depositMapSimpleUpdate) #speak
epin.startPlasmaListener(epin.handleMsg)

############### draw callback ###############

def draw():
  global eti, c1
  screen.clear()
  eti.draw(screen)
  etinav.draw(screen)

############### other interaction callbacks ###############

def on_key_down(key):   etinav.on_key_down(key)
def on_key_up(key):     etinav.on_key_up(key)
def on_mouse_down(pos): etinav.on_mouse_down(pos)
def on_mouse_up():      etinav.on_mouse_up()
def on_mouse_move(rel): etinav.on_mouse_move(rel)
def update():           etinav.update()

pgzrun.go()

### end ###
