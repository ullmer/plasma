# Example visual application toward Animist
# Brygg Ullmer, Clemson University
# Begun 2025-06-02

import pygame, traceback
from enoActorScaled  import *
from pgzero.builtins import Actor, animate, keyboard, keys

######## enodia pygame zero animist square ######## 

class enoPgzASquare:
  imgSqFn, imgTBox  = 'sspirito01h', 'transp_box01b'
  actorSq, actorBox = None, None

  boxSelected     = False
  flangeWidth     = 20
  flangeBoxOffset = 100
  flangeBaseColor = (128, 128, 128, 128) #alpha; pygame-targeted (!0)
  flangeSurfaces  = None
  lastBoxPos      = None
  windowDim       = None #screen dimensions tuple, for flange extent calculation

  ########### constructor ########### 

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    self.prepActors()
    self.prepFlange()

  def msg(self, msgstr): print("enoPgzASquare message: " + str(msgstr))
  def err(self, msgstr): print("enoPgzASquare error: "   + str(msgstr)); traceback.print_exc()

  ########### prepare actors ########### 

  def prepActors(self):
    self.actorBox    = Actor(self.imgTBox,               pos=( 500, 500))
    self.actorSq     = enoActorScaled(self.imgSqFn,      pos=(1000, 500), 
                                                   scale=.2, alpha = 220)
  ########### prepare flange ########### 

  def prepFlange(self):
    self.flangeSurfaces = {}
    if self.actorBox  is None: self.msg("prepFlange: actor box is None"); return
    if self.screenDim is None: self.msg("prepFlange: screenDim(ensions) must be assigned"); return None

    self.lastBoxPos = self.actorBox.pos
  
  ########### calc flange coordinates ########### 

  def calcFlangeCoordinates(self, 
                            basePos: tuple[int, int], 
                            xsign:   int, 
                            ysign:   int):
   
    try:
      v1 = self.calcFlangeCoordinate(basePos, xsign, ysign, True)  # box-adjacent
      v2 = self.calcFlangeCoordinate(basePos, xsign, ysign, False) # edge-of-window
      return [v1, v2]
    except: self.err("calcFlangeCoordinates")

  ########### calc flange coordinate ########### 

  def calcFlangeCoordinate(self, 
                           basePos: tuple[int, int], 
                           xsign:   int, 
                           ysign:   int, 
                           boxAdjacent : bool):

    try:
      x1, y1 = basePos

      if boxAdjacent is False: #calculate relative to ends of window
        if   xsign == -1: x2=0
        elif xsign ==  1: x2=self.windowDim[0]
        else:             x2=x1

        if   ysign == -1: y2=0
        elif ysign ==  1: y2=self.windowDim[1]
        else:             y2=y1
        return (x2, y2)

      x2 = x1 + xsign * self.flangeBoxOffset 
      y2 = y1 + ysign * self.flangeBoxOffset 
     return (x2, y2)

    except: self.err("calcFlangeCoordinate"); return None

  ########### draw ########### 

  def draw(self, screen): 
    self.drawFlange(screen)
    self.actorBox.draw()
  
  ########### drawFlange ########### 

  def drawFlange(self, screen): 

  ########### on mouse down ########### 

  def on_mouse_down(self, pos):
    if self.actorBox.collidepoint(pos): 
      self.boxSelected = True
      print("box selected"); return

  ################## on_mouse_move ##################

  def on_mouse_move(self, rel, buttons):
    if self.boxSelected:
      x1, y1 = self.actorBox.pos
      dx, dy = rel
      x2, y2 = x1+dx, y1+dy
      self.actorBox.pos = (x2, y2)

  ################## on_mouse_up ##################

  def on_mouse_up(self): self.boxSelected = False

### end ###
