# https://pygame-zero.readthedocs.io/en/stable/ptext.html
# https://pythonprogramming.altervista.org/pygame-4-fonts/

import sys; sys.path.append("..")

from enoButton import *
import yaml

WIDTH, HEIGHT = 900, 900

panel1Fn = 'yaml/panel1.yaml'
panel1F  = open(panel1Fn, 'r+t')
panel1Y  = yaml.safe_load(panel1F)

print(panel1Y)

global panel
panel = []
dy = 50; idx = 0

for row in panel1Y: #rows
  ba = enoButtonArray(row, buttonDim=(150, 30), dx=160, basePos=(0, dy*idx))
  panel.append(ba); idx += 1

rect1   = Rect((100, 150), (200, 200))
bgcolor = "#aa0000"

def draw(): 
  for ba in panel: ba.draw(screen)
  screen.draw.filled_rect(rect1, bgcolor)

def on_mouse_down(pos):
  for ba in panel: ba.on_mouse_down(pos)

### end ###
