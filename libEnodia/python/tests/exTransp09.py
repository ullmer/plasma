# Simple animation against (on MS Windows) transparent window
# Brygg Ullmer, Clemson University
# Begun 2024-08-26

import sys; sys.path.append("..")

WIDTH, HEIGHT = 300, 300

from enoTranspWinDance import *
from enoWinMgr         import *

class exTransp09(enoTranspWinDance): pass
  
ewm = enoWinMgr()
et9 = exTransp09(ewm=ewm)

def draw(): et9.draw()
  
### end ###

