# Interaction panel code
# Brygg Ullmer, Clemson University
# Begun 2024-10-09

import sys, os, yaml, traceback
from ataLabelBlock import *
from enoIpanelYaml import *

############# enodia interaction panel #############

class EnoIpanelLBPgz(EnoIpanelYaml):

  alb          = None #AtaLabelBlock 
  blockWH      = (50, 50)
  blockPad     = ( 3,  3)
  blockBasePos = (1500, 700)
  blockDefaultAlpha = 128
  regions      = None
  region2zones = None
  keyMap       = 'states' #panel attribute used to map cell abbreviations to full names
  verbose      = False

  fontSizePrimary   = 24
  fontSizeSecondary = 10

  ############# constructor #############

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    super().__init__()
    self.alb = AtaLabelBlock(fontSizePrimary   = self.fontSizePrimary, \
                             fontSizeSecondary = self.fontSizeSecondary)

    self.populateBlocksLBPgz()

  ############# int to RGB #############

  def intToRgb(self, hexInt): 
    r = (hexInt >> 16) & 0xFF
    g = (hexInt >>  8) & 0xFF
    b = (hexInt)       & 0xFF
    return (r, g, b)

  ############# draw #############

  def draw(self, screen):
    try:    self.alb.draw(screen)
    except: self.err("draw")

  ############# populate blocks LBgpzname #############

  def populateBlocksLBPgz(self):
    try:
      self.regions      = self.getPanelAttrib('regions')
      self.region2zones = {}
      self.zone2region  = {}
      w, h              = self.blockWH

      for regionKey in self.regions:
        region = self.regions[regionKey]
        self.msg("popBlL: " + str(region))
        regionColorInt = region['col']
        regionColor    = self.intToRgb(regionColorInt)
        key = "region_" + str(regionKey)
        self.alb.createAlphaSurface2(key, w, h, regionColor, self.blockDefaultAlpha)
        zones = region[self.keyMap]
        self.region2zones[regionKey] = zones
        for zone in zones:
          self.zone2region[zone] = regionKey

      elDict = self.getPanelAttrib(self.keyMap)
      bw0,  bh0  = self.blockWH
      padX, padY = self.blockPad
      bw1,  bh1  = bw0 + padX, bh0 + padY
      
      x0, y0 = self.blockBasePos
      for i   in range(self.rows):
        for j in range(self.cols):
          abbrev = self.getMatrixLocus(i,j)
          if abbrev not in elDict: continue
          name   = elDict[abbrev] # e.g., states
          x, y = x0 + bw1*i, y0 + bh1*j
          region = self.zone2region[abbrev]
          regionSurf = "region_" + region
          self.alb.placeAlphaTextSurface(abbrev, regionSurf, x, y, abbrev, name)

    except: self.err("populateBlocksLBPgz")

############# main #############

if __name__ == "__main__":
  eipl  = EnoIpanelLBPgz(panelFn = 'yaml/us-bea2.yaml')
  #print(eipl.regions)
  #my = eipl.expandMatrixYaml()
  #print(my)

  states = eipl.getPanelAttrib('states')
  a0     = eipl.getMatrixLocus(0,0)
  a0n    = states[a0]
  print("A0:", a0, a0n)

### end ###
