### Manage an array of labeled tranlucent blocks
# Brygg Ullmer, Clemson University

import pygame
from ataBase import *

################ ata label block ################

class AtaLabelBlock(AtaBase):

  rectSurfaceCache  = None
  rectSurfaceDims   = None
  placedSurfaceDict = None

  defaultColor = (70, 70, 100)
  defaultAlpha = 128

  ################ constructor ################

  def __init__(self):
    super().__init__()
    self.rectSurfaceCache  = {}
    self.rectSurfaceDims   = {}
    self.placedSurfaceDict = {}
  
  ################ create alpha surface ################

  def createAlphaSurface(self, handle: str, w: int, h: int, rcolor=None, ralpha=None):

    try:
      if rcolor is None: rcolor = self.defaultColor
      if ralpha is None: ralpha = self.defaultAlpha

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

### end ###

  ################ draw ################

  def draw(self, screen):
    try:
      for handle in self.placedSurfaceDict:
        ps = self.placedSurfaceDict[handle]
        surfaceHandle, x, y = ps
        if surfaceHandle not in self.rectSurfaceCache:
          self.msg("draw: attempted to draw unknown surface handle: " + str(surfaceHandle))
          continue

        rect_surface = self.rectSurfaceCache[surfaceHandle]
        screen.blit(rect_surface, (x,y))
    except: self.err("draw")

### end ###

