# Warmup test
# Brygg Ullmer, Clemson University
# Begun 2025-07-09

import os

os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0'
WIDTH, HEIGHT = 1600, 1000

import pgzrun

from vizLandsPgz import *

avlp = ADVizLandsPgz()
avlp.loadYaml()
avlp.initPgz()

def draw(): screen.clear(); avlp.draw(screen)

pgzrun.go()

### end ###
