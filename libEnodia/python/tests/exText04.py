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
  tbox   =  Rect((0, 70), (100, 30))
  tpos1  = (100, -10)
  tpos2  = ( 2,  102)
  font1  = "oswald-medium"
  animPauseDur = 3.

  numSubwins      = 3
  winDimension    = (100, 100)
  #winCoords       = [(0, 0), (0, 300), (0, 600)]

  ################### draw ################### 

  def draw(self):
    super().draw()
    screen.draw.filled_rect(self.tbox, self.mred)
    screen.draw.text("A",       topright  =self.tpos1, fontsize=70, fontname=self.font1, color=self.mwhite, alpha=0.5)
    screen.draw.text("SPATIAL", bottomleft=self.tpos2, fontsize=25, fontname=self.font1, color=self.mwhite, alpha=0.5)

     
  
  ################### subwindow animation pause ################### 

  def subwinAnimPause(self, whichSubwin, nextDest, subsequentDest):
    cb = partial(self.subwinAnimBounce, whichSubwin, nextDest, subsequentDest)
    clock.schedule(cb, self.animPauseDur) # after a pause of animPauseDur seconds, call the bounce
  
  ################### subwindow animation bounce ################### 

  def subwinAnimBounce(self, whichSubwin, nextDest, subsequentDest):
    cb = partial(self.subwinAnimPause, whichSubwin, subsequentDest, nextDest) #callback on completion
    animate(whichSubwin, pos=nextDest, tween=self.tween, duration=self.dur1, on_finished=cb)

  ################### first frame ################### 

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
