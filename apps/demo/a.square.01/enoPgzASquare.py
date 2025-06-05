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

  boxSelected       = False
  flangeWidth       = 20
  flangeBoxOffset   = 100
  flangeBaseColor   = (128, 128, 128, 90) #alpha; pygame-targeted (!0)
  flangeSurfaces    = None
  flangeCoordinates = None
  lastBoxPos        = None
  windowDim         = None #screen dimensions tuple, for flange extent calculation
  verbose           = True

  orientedFlangeHandles = ['L', 'R', 'T', 'B']

  ########### constructor ########### 

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    self.prepActors()

  def msg(self, msgstr): print("enoPgzASquare message: " + str(msgstr))
  def err(self, msgstr): print("enoPgzASquare error: "   + str(msgstr)); traceback.print_exc()

  ########### prepare actors ########### 

  def prepActors(self):
    self.actorBox    = Actor(self.imgTBox,               pos=( 500, 500))
    self.actorSq     = enoActorScaled(self.imgSqFn,      pos=(1000, 500), 
                                                   scale=.2, alpha = 220)
  ########### calculate and store flange coordinates ########### 

  def cacheFlangeCoordinates(self):
    try:
      if self.actorBox  is None: self.msg("prepFlange: actor box is None"); return
      if self.windowDim is None: self.msg("prepFlange: windowDim(ensions) must be assigned"); return None

      if self.flangeCoordinates is None: self.flangeCoordinates = {}

      pos                 = self.actorBox.pos
      self.lastBoxPos     = pos

      self.flangeCoordinates['L'] = self.calcFlangeCoordinatesWHXY(pos, -1,  0)
      self.flangeCoordinates['R'] = self.calcFlangeCoordinatesWHXY(pos,  1,  0)
      self.flangeCoordinates['T'] = self.calcFlangeCoordinatesWHXY(pos,  0,  1)
      self.flangeCoordinates['B'] = self.calcFlangeCoordinatesWHXY(pos,  0, -1)
    except: self.err("genFlangeCoordinates")

  ########### drawFlanges ########### 

  def drawFlanges(self, screen):
    try:
      boxPos = self.actorBox.pos
      if self.lastBoxPos is None or boxPos != self.lastBoxPos:
        self.cacheFlangeCoordinates()
        self.genFlangeSurfaces()
        self.lastBoxPos = boxPos

      for orientedFlangeHandle in self.orientedFlangeHandles:
        flangeSurface = self.flangeSurfaces[   orientedFlangeHandle]
        w, h, x, y    = self.flangeCoordinates[orientedFlangeHandle]

        screen.blit(flangeSurface, (x,y))

        if self.verbose: 
          hwhxy = "%s %i %i %i %i" % (orientedFlangeHandle, w, h, x, y)
          self.msg("drawFlanges called: " + hwhxy)
        
    except: self.err("drawFlanges")

  ########## generate flange surfaces ########### 

  def genFlangeSurfaces(self):
    try:
      if self.flangeSurfaces    is None: self.flangeSurfaces = {}
      if self.flangeCoordinates is None: self.calcFlangeCoordinates()

      for orientedFlangeHandle in self.orientedFlangeHandles:
        w, h, x, y = self.flangeCoordinates[orientedFlangeHandle]
        s = pygame.Surface((w,h), pygame.SRCALPHA)
        s.fill(self.flangeBaseColor)
        self.flangeSurfaces[orientedFlangeHandle] = s
   
    except: self.err("genFlangeSurfaces")
  
  ########### calc flange coordinates W_H_TLX_TLY ########### 

  # for transparent rendering w/in pygame, "width,height" and (tl.x, tl.y) are required
  # this could be prudent to calculate this way from outset, but -- for coding 
  # expediency, initially leaving as-is

  def calcFlangeCoordinatesWHXY(self, 
                                basePos: tuple[int, int], 
                                xsign:   int, 
                                ysign:   int):

    try:
      v1, v2 = self.calcFlangeCoordinates(basePos, xsign, ysign)
      v1a, v1b = v1
      v2a, v2b = v2

      xcoords, ycoords = [], []

      for v in [v1a, v1b, v2a, v2b]:
        x, y = v
        xcoords.append(x); ycoords.append(y)

      minX, minY = min(xcoords), min(ycoords)
      maxX, maxY = max(xcoords), max(ycoords)

      w,   h   = maxX - minX, maxY - minY
      tlx, tly = minX, maxY 
      result = [w, h, tlx, tly]
      return result

    except: self.err("calcFlangeCoordinatesWHXY")

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

      else:
        x2 = x1 + xsign * self.flangeBoxOffset  # midpoints
        y2 = y1 + ysign * self.flangeBoxOffset 

      fw2 = self.flangeWidth / 2 # could be better to /2., but promotion to float might cost
      x3, y3 = x2 + ysign * fw2, y2 + xsign * fw2 # believe xsign/ysign inversion appropros; test
      x4, y4 = x2 - ysign * fw2, y2 - xsign * fw2
      result = [(x3, y3), (x4, y4)]
      return result

    except: self.err("calcFlangeCoordinate"); return None

  ########### draw ########### 

  def draw(self, screen): 
    self.drawFlanges(screen)
    self.actorBox.draw()

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
  
