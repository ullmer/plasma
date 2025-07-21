# Warmup test
# Brygg Ullmer, Clemson University
# Begun 2025-07-09

import os
import pygame

os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0' #place window at top-left
TITLE         = 'ATA.browser'
WIDTH, HEIGHT =  1920, 1080

import pgzrun
from vizLandsPgz   import *
from ataLabelBlock import *

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

def draw(): 
  fullscreen(); screen.clear(); 
  avlp.draw(screen); alb.draw(screen)


alb = AtaLabelBlock()
alb.createAlphaSurface("blk100", 100, 100, (80,80,100), 128)
alb.placeAlphaSurface("box1", "blk100", 100, 100)
alb.placeAlphaSurface("box2", "blk100", 150, 150)
alb.placeAlphaSurface("box3", "blk100", 175, 175)


touched = None

def on_mouse_down(pos): 
  x, y = pos
  touchedBlocks = alb.determineBlocksSurroundingPoint(x,y)
  if len(touchedBlocks) > 0: 
    print("touched: " + str(touchedBlocks))
    global touched; touched = touchedBlocks

def on_mouse_move(rel): 
  dx, dy = rel
  if touched is not None and len(touched) > 0: alb.moveBlocks(touched, dx, dy)

def on_mouse_up(): global touched; touched = None

pgzrun.go()

### end ###

