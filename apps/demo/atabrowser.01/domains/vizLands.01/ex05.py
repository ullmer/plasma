# Warmup test
# Brygg Ullmer, Clemson University
# Begun 2025-07-09

import os
import pygame

os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0' #place window at top-left
TITLE         = 'ATA.browser'
WIDTH, HEIGHT =  1920, 1080

import pgzrun
from vizLandsPgz import *

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

def draw(): fullscreen(); screen.clear(); avlp.draw(screen)

pgzrun.go()

### end ###
