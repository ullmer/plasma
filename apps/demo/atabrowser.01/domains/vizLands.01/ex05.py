# Warmup test
# Brygg Ullmer, Clemson University
# Begun 2025-07-09

import os

os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0' #place window at top-left
WIDTH, HEIGHT = 1920, 1080

import pgzrun
from vizLandsPgz import *

avlp = ADVizLandsPgz()
avlp.yamlFnState    = 'us_nps/az.yaml'
avlp.yamlStatePath1 = 'az:nps:meta'

avlp.loadYaml()
avlp.initPgz()

def draw(): screen.clear(); avlp.draw(screen)

pgzrun.go()

### end ###
