# Simple animation against (on MS Windows) transparent window
# Brygg Ullmer, Clemson University
# Begun 2024-08-26

import sys; sys.path.append("..")

WIDTH, HEIGHT = 300, 300

import pygame
import pgzero.game

from functools         import partial
from enoWinMgr         import *
from enoTranspWinDance import *

pgzero.game.DISPLAY_FLAGS = pygame.NOFRAME #"use wisely"

################## example transparency 09 ##################

class exText04(enoTranspWinDance): 

  mred   = "#773540"
  mwhite = "#ffffff"
  tbox   =  Rect((0, 70), (100, 100))
  tpos1  = (100, -10)
  tpos2  = ( 2,  102)
  font1  = "oswald-medium"

  def draw(self):
    screen.draw.filled_rect(tbox, mred)
    screen.draw.text("A",       topright  =tpos1, fontsize=70, fontname=font1, color=mwhite, alpha=0.5)
    screen.draw.text("SPATIAL", bottomleft=tpos2, fontsize=25, fontname=font1, color=mwhite, alpha=0.5)

  def subwinAnimBounce(self, whichSubwin, nextDest, subsequentDest):
    cb = partial(self.subwinAnimBounce, whichSubwin, subsequentDest, nextDest) #callback on completion
    animate(whichSubwin, pos=nextDest, tween=self.tween, duration=self.dur1, on_finished=cb)

  def firstFrame(self): # invoked on rendering of first frame
    super().firstFrame()

    for winId in [1, 2]:
      w      = self.getWinCoordProxies(winId)
      x1, y1 = w.pos
      x2, y2 = x1 + 1700, y1

      cb = partial(self.subwinAnimBounce, w, (x1, y1), (x2, y2)) #callback on animation completion
      animate(w, pos=(x2, y2), tween=self.tween, duration=self.dur1, on_finished=cb)

################## main ##################
  
ewm = enoWinMgr()
et4 = exText04(ewm=ewm)

def draw(): et4.draw() #requires invocation via pgzrun, per its ~simplification of scope
  
### end ###
