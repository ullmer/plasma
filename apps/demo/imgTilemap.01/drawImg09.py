# Navigate a tiled image 
# Brygg Ullmer, Clemson University
# Begun 2023-03-22

import os

os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0' #place window at top-left
WIDTH, HEIGHT = 1600, 1000

import pgzrun

from enoTiledImg     import *
from enoTiledImgNav  import *
from enoPlasmaImgNav import *
import sys

WIDTH, HEIGHT=1920, 1080

#tmdn = 'rmUS1882a'
#tmdn = 'cuMap2'
tmdn = 'rmUS1882b'

eti    = EnoTiledImg(verbose=False)
etinav = EnoTiledImgNav(eti)
#eti.imgPos = (-10000, 0)

eti.adjustWindowPlacement(WIDTH, HEIGHT)
eti.loadTmap(tmdn)

epin = EnoPlasmaImgNav()
epin.registerMapMoveCb(etinav.plasmaMoveCb)              #listen
etinav.setPlasmaMoveDeposit(epin.depositMapSimpleUpdate) #speak

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
