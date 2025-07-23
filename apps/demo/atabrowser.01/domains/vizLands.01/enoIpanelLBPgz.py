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
  blockBasePos = (10, 100)
  blockDefaultAlpha = 128
  regions      = None
  keyMap       = 'states' #panel attribute used to map cell abbreviations to full names

  verbose      = False

  ############# constructor #############

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    super().__init__()
    self.alb = AtaLabelBlock()
    self.populateBlocksLBPgz()

  ############# get panel name #############

  def populateBlocksLBPgz(self):
    try:
      self.regions = self.getPanelAttrib('regions')
      w, h = self.blockWH
      for regionKey in self.regions:
        region = self.regions[regionKey]
        self.msg("popBlL: " + str(region))
        regionColor = region['col']
        self.alb.createAlphaSurface2("region", w, h, regionColor, self.blockDefaultAlpha)

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
