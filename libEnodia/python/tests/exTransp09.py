# Simple animation against (on MS Windows) transparent window
# Brygg Ullmer, Clemson University
# Begun 2024-08-26

import sys; sys.path.append("..")

WIDTH, HEIGHT = 300, 300

from enoTranspWinDance import *
from enoWinMgr         import *

################## example transparency 09 ##################

class exTransp09(enoTranspWinDance): 

  def firstFrame(self):
    super().firstFrame()

    for winId in [1, 2]:
      w      = self.winCoordProxies[winId]
      x1, y1 = w.pos
      x2, y2 = x1 + 1000, y1
      animate(w, pos=(x2, y2), tween=self.tween, duration=self.dur1)

################## main ##################
  
ewm = enoWinMgr()
et9 = exTransp09(ewm=ewm)

def draw(): et9.draw()
  
### end ###

