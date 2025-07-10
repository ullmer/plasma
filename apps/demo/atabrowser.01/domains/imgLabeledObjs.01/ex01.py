# Warmup test
# Brygg Ullmer, Clemson University
# Begun 2025-07-09

WIDTH, HEIGHT = 800, 800
from imgLabeledPgz import *

ilp = ADImgLabeledObjPgz()
ilp.loadYaml()
ilp.initPgz()

def draw(): screen.clear(); ilp.draw(screen)

### end ###
