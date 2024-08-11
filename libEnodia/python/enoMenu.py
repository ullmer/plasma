# Enodia menu-like elements -- sometimes backed by Pygame Zero, 
#  sometimes by physical buttons, sometimes by other variants.
# First approximation, albeit too specific to Pygame Zero
# Brygg Ullmer, Clemson University
# Begun 2024-08-11

import yaml
import os
import traceback

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
  dx, dy     = 0, 0

  yamlFn     = None
  yamlD      = None
  yamlMenuD  = None

  drawText   = True
  drawImg    = False
  drawAdapt  = True   # if True, will render text and/or image only when specified

  whichMenuName = "homeMenu"

  autoBuildMenu = True
  verbose       = False

  enoButtonArr  = None

  ############# constructor #############

  def __init__(self, whichMenuName=None, **kwargs): 

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

    if whichMenuName is not None: self.whichMenuName = whichMenuName
    self.loadYaml()

    if self.autoBuildMenu: self.buildMenu()

  ############# error message #############

  def err(self, msg): print("enoMenu error:" + msg)

  ############# load yaml #############

  def loadYaml(self):
    if self.yamlFn is None:                  err("loadYaml: yaml filename undefined"); return
    if os.path.exists(self.yamlFn) == False: err("loadYaml: yaml file not found:" + self.yamlFn); return

    f = open(self.yamlFn, 'rt')
    self.yamlD = yaml.safe_load(f)
    f.close()

    if 'animist' not in self.yamlD:  err("loadYaml: animist not found in yaml" + self.yamlFn); return

    ad = self.yamlD['animist']

    if self.whichMenuName not in ad: err("loadYaml: %s menu not found in yaml %s" % (self.whichMenuName, self.yamlFn)); return

    self.yamlMenuD = ad[self.whichMenuName]

  ############# build menu #############

  def buildMenu(self):
    if self.yamlMenuD is None: err("buildMenu: yaml menu datastructure not found"); return

    textHandles = []; imageFns = []

    for menuEntry in self.yamlMenuD:
      try:    name = menuEntry['name']; imageFn = menuEntry['imageFn']
      except: err("buildMenu: menuEntry parsing issue"); traceback.print_exc(); return
      textHandles.append(name); imageFns.append(imageFn)

    self.enoButtonArr = enoButtonArray(textHandles, imagesFns=imageFns, buttonDim = self.buttonDim,
                          dx = self.dx, dy = self.dy, basePos = self.basePos, 
                          drawText = self.drawText,  drawImg = self.drawImg, drawAdapt = self.drawAdapt,
                          bgcolor1 = self.bgcolor1, bgcolor2 = self.bgcolor2,  fgcolor = self.fgcolor, 
                          alpha    = self.alpha,    fontSize = self.fontSize,    angle = self.angle)

### end ###
