# Warmup test
# Brygg Ullmer, Clemson University
# Begun 2025-07-09

import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0' #place window at top-left

import pygame

TITLE         = 'ATA.browser'
WIDTH, HEIGHT =  1920, 1080

import pgzrun
from vizLandsPgz    import *
from ataLabelBlock  import *
from enoIpanelLBPgz import *

#### deal with mac challenges ####
fullscreenSet = False

def fullscreen(): 
  global fullscreenSet
  if not fullscreenSet: 
    pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    fullscreen_set = True

#### main ####

avlp = ADVizLandsPgz()
avlp.yamlFnState    = 'us_nps/az.yaml'
avlp.yamlStatePath1 = 'az:nps:meta'

avlp.loadYaml()
avlp.initPgz()

eil = EnoIpanelLBPgz(panelFn = 'yaml/us-bea2.yaml', firstRow=7) 
eil.alb.printSurfaceCache()

touched = None

def draw(): 
  #fullscreen()
  screen.clear()
  avlp.draw(screen)
  eil.draw(screen)

def on_mouse_down(pos): avlp.on_mouse_down(pos)
def on_mouse_move(rel): avlp.on_mouse_move(rel)
def on_mouse_up():      avlp.on_mouse_up()

pgzrun.go()

### end ###

