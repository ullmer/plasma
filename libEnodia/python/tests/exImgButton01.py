# https://pygame-zero.readthedocs.io/en/stable/ptext.html
# https://pythonprogramming.altervista.org/pygame-4-fonts/

import sys; sys.path.append("..")

from enoButton import *

WIDTH, HEIGHT = 900, 900
bd = (100, 100)

b1 = enoButton("animist", imageFn="glyphs/animist01a_100", basePos=(50,  50), drawText=False, buttonDim=bd)
b2 = enoButton("BOS",     imageFn="glyphs/map_bos01a_100", basePos=(50, 155), drawText=False, buttonDim=bd)
b3 = enoButton("MIT",     imageFn="glyphs/map_mit01a_100", basePos=(50, 260), drawText=False, buttonDim=bd)
buttons = [b1,b2,b3]

def draw():             
  screen.clear()
  for b in buttons: b.draw(screen)

def on_mouse_down(pos): 
  for b in buttons: b.on_mouse_down(pos)

### end ###
