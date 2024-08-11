# Enodia menu-like elements -- sometimes backed by Pygame Zero, 
#  sometimes by physical buttons, sometimes by other variants.
# First approximation, albeit too specific to Pygame Zero
# Brygg Ullmer, Clemson University
# Begun 2024-08-11

import yaml
import os

from   enoButton import *

##################### enodia menu #####################

class enoMenu:
  basePos    = (0,0)
  buttonDim  = (100, 100)
  bgcolor1   = (0, 0, 130)
  bgcolor2   = (50, 50, 250)
  fgcolor    = "#bbbbbb"
  alpha      = .8
  fontSize   = 36
  angle      = 0

  yamlFn     = None
  yamlD      = None

  drawText   = True
  drawImg    = False
  drawAdapt  = True   # if True, will render text and/or image only when specified

  verbose     = False

  ############# constructor #############

  def __init__(self, **kwargs): 

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

    self.loadYaml()

  ############# error message #############

  def err(self, msg): print("enoMenu error:" + msg)

  ############# load yaml #############

  def loadYaml(self):
    if self.yamlFn is None:             err("loadYaml: yaml filename undefined"); return
    if os.path.exists(yamlFn) == False: err("loadYaml: yaml file not found:" + self.yamlFn); return
    

### end ###
