# Simple animation against (on MS Windows) transparent window
# Brygg Ullmer, Clemson University
# Begun 2024-08-26

import sys; sys.path.append("..")

WIDTH, HEIGHT = 300, 300

from enoTranspWinDance import *
from enoWinMgr         import *
  
ewm  = enoWinMgr()
etwd = enoTranspWinDance(ewm=ewm)

def draw(): etwd.draw()
  
### end ###

