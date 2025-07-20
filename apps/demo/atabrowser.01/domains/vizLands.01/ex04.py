### Manage an array of labeled tranlucent blocks
# Brygg Ullmer, Clemson University

WIDTH, HEIGHT = 800, 800
from ataLabelBlock import *

alb = AtaLabelBlock()
alb.createAlphaSurface2("blk100", 100, 100, (80,80,100), 128)
alb.placeAlphaTextSurface("box1", "blk100", 100, 100, "foo", "foofoo")
alb.placeAlphaTextSurface("box2", "blk100", 150, 150, "bar", "barbar")
alb.placeAlphaTextSurface("box3", "blk100", 175, 175, "wah", "wahwah")

def draw(): screen.clear(); alb.draw(screen)

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

### end ###

