# https://pygame-zero.readthedocs.io/en/stable/ptext.html
# https://pythonprogramming.altervista.org/pygame-4-fonts/

import sys; sys.path.append("..")
from enoMenu import *

WIDTH, HEIGHT = 900, 900
bd = (100, 100)

em = enoMenu(yamlFn = "yaml/animistHomeMenu01.yaml", requestAnim=True)

def draw(): screen.clear(); em.draw(screen)
def on_mouse_down(pos):     em.on_mouse_down(pos)

### end ###
