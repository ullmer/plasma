# Interaction panel code
# Brygg Ullmer, Clemson University
# Begun 2024-10-09

import sys, os, yaml, traceback
from ataLabelBlock import *

############# enodia interaction panel #############

class enoIpanelLBPgz(enoIpanelYaml):

  alb          = None #AtaLabelBlock 
  blockWH      = (50, 50)
  blockPad     = ( 3,  3)
  blockBasePos = (10, 100)

  verbose      = False

  ############# constructor #############

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    super().__init__()
    self.alb = AtaLabelBlock()
    self.populateBlocksLBPgz()

  ############# get panel name #############

  def populateBlocksLBPgz(self):

  def getPanelAttrib(self, attrib):

### end ###
