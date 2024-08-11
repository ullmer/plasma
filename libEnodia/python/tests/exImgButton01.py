# https://pygame-zero.readthedocs.io/en/stable/ptext.html
# https://pythonprogramming.altervista.org/pygame-4-fonts/

import sys; sys.path.append("..")

from enoButton import *

WIDTH, HEIGHT = 900, 900

b1 = enoButton("animist", imageFn="glyphs/animist01a_100", basePos=(100, 100), drawText=False)
b2 = enoButton("BOS",     imageFn="glyphs/map_bos01a_100", basepos=(100, 225), drawText=False)
b3 = enoButton("BOS",     imageFn="glyphs/map_mit01a_100", basepos=(100, 355), drawText=False)
buttons = [b1,b2,b3]

def draw():             
  for b in buttons: b.draw(screen)

def on_mouse_down(pos): 
  for b in buttons: b.on_mouse_down(pos)

### end ###
