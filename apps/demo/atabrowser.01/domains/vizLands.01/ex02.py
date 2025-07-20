### Manage an array of labeled tranlucent blocks
# Brygg Ullmer, Clemson University

WIDTH, HEIGHT = 800, 800
from ataLabelBlock import *

alb = AtaLabelBlock()
alb.createAlphaSurface("blk100", 100, 100, (80,80,100), 128)
alb.placeAlphaSurface("box1", "blk100", 100, 100)
alb.placeAlphaSurface("box2", "blk100", 150, 150)
alb.placeAlphaSurface("box3", "blk100", 175, 175)

def draw(): screen.clear(); alb.draw(screen)

def on_mouse_down(pos): 
  x, y = pos
  touchedBlocks = alb.determineBlocksSurroundingPoint(x,y)
  if len(touchedBlocks) > 0: print("touched: " + str(touchedBlocks))

### end ###

