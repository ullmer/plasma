# Warmup test
# Brygg Ullmer, Clemson University
# Begun 2025-07-09

WIDTH, HEIGHT = 1600, 1000
from vizLandsPgz import *

avlp = ADVizLandsPgz()
avlp.loadYaml()
avlp.initPgz()

def draw(): screen.clear(); avlp.draw(screen)

### end ###
