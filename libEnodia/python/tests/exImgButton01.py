# https://pygame-zero.readthedocs.io/en/stable/ptext.html
# https://pythonprogramming.altervista.org/pygame-4-fonts/

import sys; sys.path.append("..")

from enoButton import *

WIDTH, HEIGHT = 900, 900

b1 = enoButton("animist", imgFn="glyphs/animist01a_100", basePos=(50,  50))
b2 = enoButton("BOS",     imgFn="glyphs/map_bos01a_100", basepos=(50, 125))
buttons = [b1,b2]

def draw():             
  for b in buttons: b.draw()

def on_mouse_down(pos): 
  for b in buttons: b.on_mouse_down(pos)

### end ###
