# Enodia home menu
# First approximation, albeit too specific to Pygame Zero
# Brygg Ullmer, Clemson University
# Begun 2024-08-11

import yaml
import os
import traceback

from   enoMenu import *

##################### enodia animist home menu #####################

class enoAnimistHomeMenu(enoMenu):

  ############# constructor #############

  def __init__(self, whichMenuName=None, **kwargs): 

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

    if whichMenuName is not None: self.whichMenuName = whichMenuName
    self.loadYaml()

    if self.autoBuildMenu: self.buildMenu()

  ############# error message #############

  def err(self, msg): print("enoAnimistHomeMenu error:" + msg)
  def msg(self, msg): print("enoAnimistHomeMenu msg:  " + msg)

### end ###
