### Manage an array of labeled tranlucent blocks
# Brygg Ullmer, Clemson University

import pygame
from ataBase import *

################ ata label block ################

class AtaLabelBlock(AtaBase):

  rectSurfaceCache  = None
  rectSurfaceDims   = None
  placedSurfaceDict = None

  labelDictPrimary   = None #"major/title" labels
  labelDictSecondary = None #sublabels

  textPadPrimary     = (10, 10)
  textPadSecondary   = (30, 30)

  fontNamePrimary    = "saira/saira_condensed_black"
  fontNameSecondary  = "saira/saira_condensed_regular"

  fontSizePrimary    = 48
  fontSizeSecondary  = 30

  fontColorPrimary   = (255, 255, 255)
  fontColorSecondary = (255, 255, 255)

  fontAlphaPrimary   = .8
  fontAlphaSecondary = .6

  defaultBgColor = (70, 70, 100)
  defaultBgAlpha = 128

  ################ constructor ################

  def __init__(self):
    super().__init__()
    self.rectSurfaceCache  = {}
    self.rectSurfaceDims   = {}
    self.placedSurfaceDict = {}

    self.labelDictPrimary   = {}
    self.labelDictSecondary = {}
  
  ################ create alpha surface ################

  def createAlphaSurface(self, handle: str, w: int, h: int, rcolor=None, ralpha=None):

    try:
      if rcolor is None: rcolor = self.defaultBgColor
      if ralpha is None: ralpha = self.defaultBgAlpha

      rect_surface = pygame.Surface((w, h), pygame.SRCALPHA)
      r, g, b = rcolor
      rect_surface.fill ((r,g,b,ralpha))
      self.rectSurfaceCache[handle] = rect_surface
      self.rectSurfaceDims[handle]  = [w,h]

    except: self.err("createTranslSurface")

  ################ place alpha surface ################

  def placeAlphaSurface(self, placeHandle: str, surfaceHandle: str, x: int, y: int):
    try:
      placedAlphaSurface = [surfaceHandle, x, y]
      self.placedSurfaceDict[placeHandle] = placedAlphaSurface
    except: self.err("placeAlphaSurface")
  
  ################ create alpha surface ################

  def placeAlphaTextSurface(self, placeHandle: str, surfaceHandle: str, \
                            x: int, y: int, primText, secText = None):
    try:
      if self.labelDictPrimary is None or self.labelDictSecondary is None:
        self.msg("placeAlphaTextSurface issue: dictionaries not properly initiated"); return False

      self.placeAlphaSurface(placeHandle, surfaceHandle, x, y)
      self.labelDictPrimary[placeHandle] = primText

      if secText is not None:
        self.labelDictSecondary[placeHandle] = secText

    except: self.err("placeAlphaTextSurface")

  ################ drawBlockText ################

  def drawBlockText(self, handle: str):
    try:
      if self.labelDictPrimary is None or self.labelDictSecondary is None:
        self.msg("drawBlockText issue: dictionaries not properly initiated"); return False

      txtPrim = txtSec = None

      if handle in self.labelDictPrimary:   txtPrim = self.labelDictPrimary[handle]
      if handle in self.labelDictSecondary: txtSec  = self.labelDictSecondary[handle]

      if (txtPrim is None) and (txtSec is None): return False #nothing to do
      
      if handle not in rectSurfaceDims or handle not in placedSurfaceDict:
        self.msg("drawBlockText issue: difficulty determining coordinates"); return False

      w, h     = self.rectSurfaceDims[handle]
      sh, x, y = self.placedAlphaSurface[handle]

      if txtPrim is not None:
        f, s   = self.fontNamePrimary, self.fontSizePrimary
        c, a   = self.fontColorPrimary, self.fontAlphaPrimary
        px, py = self.textPadPrimary
        x1, y1 = x+px, y+htxtPrim+py
        screen.draw.text(txtPrim, bottomleft = (x1, y1), fontname=f, fontsize=s, color=c, alpha=a)

      if txtSecis not None:
        f, s   = self.fontNameSecondary,  self.fontSizeSecondary
        c, a   = self.fontColorSecondary, self.fontAlphaSecondary
        px, py = self.textPadSecondary
        x1, y1 = x+px, y+htxtPrim+py
        screen.draw.text(txtPrim, topleft = (x1, y1), fontname=f, fontsize=s, color=c, alpha=a)

    except: self.err("drawBlockText")

  ################ determine blocks surrounding point ################

  def determineBlocksSurroundingPoint(self, x: int, y:int):
    try:
      result = []
      for handle in self.placedSurfaceDict:
        ps = self.placedSurfaceDict[handle]
        surfaceHandle, sx1, sy1 = ps

        if surfaceHandle not in self.rectSurfaceDims:
          self.msg("determineBlocksSurroundingPoint: unknown surface handle: " + str(surfaceHandle))
          continue

        w, h = self.rectSurfaceDims[surfaceHandle]
        sx2, sy2 = sx1+w, sy1+h

        if sx1 <= x <= sx2 and sy1 <= y <= sy2: result.append(handle)

      return result

    except: self.err("determineBlocksSurroundingPoint")

  ################ move block ################

  def moveBlock(self, handle: str, dx: int, dy: int):
    try:
      if handle not in self.placedSurfaceDict:
        self.msg("moveBlock: handle not in placed surface dictionary"); return False

      ps = self.placedSurfaceDict[handle]
      surfaceHandle, x, y = ps
      x += dx; y += dy
      placedAlphaSurface = [surfaceHandle, x, y]

      self.placedSurfaceDict[handle] = placedAlphaSurface
    except: self.err("moveBlock")

  ################ move blocks ################

  def moveBlocks(self, handles: list[str], dx: int, dy: int):
    try:
      for handle in handles: self.moveBlock(handle, dx, dy)
    except: self.err("moveBlocks")

  ################ drawBlocks ################

  def drawBlocks(self, screen):
    try:
      for handle in self.placedSurfaceDict:
        ps = self.placedSurfaceDict[handle]
        surfaceHandle, x, y = ps
        if surfaceHandle not in self.rectSurfaceCache:
          self.msg("draw: attempted to draw unknown surface handle: " + str(surfaceHandle))
          continue

        rect_surface = self.rectSurfaceCache[surfaceHandle]
        screen.blit(rect_surface, (x,y))
    except: self.err("drawBlocks")

  ################ draw ################

  def draw(self, screen):
    try:    self.drawBlocks()
    except: self.err("draw")

### end ###
