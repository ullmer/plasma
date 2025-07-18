# Warmup test
# Brygg Ullmer, Clemson University
# Begun 2025-07-09

WIDTH, HEIGHT = 1600, 1000
from imgLabeledPgz import *

ilp = ADImgLabeledObjPgz()
ilp.loadYaml()
ilp.initPgz()

def draw(): screen.clear(); ilp.draw(screen)

### end ###
