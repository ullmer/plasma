# Plasma Protein Schemas (mapping of protocols, initially oriented
#  toward sensors and multitouch, but also with an eye toward
#  other hardware and software services)
# Lead by Brygg Ullmer, Clemson University
# Begun 2024-07-20

#import os, sys, pathlib
#LIB_PATH = pathlib.Path(__file__).parents[1] #library in parent directory
#sys.path.append(os.path.join(LIB_PATH, ''))
#import sys; sys.path.append("/home/ullmer/git/plasma/libPlasma/python/")

import asyncio, sys, time, traceback, yaml
from   functools import partial # for callback support

#############################################################
###################### plasma protein schemas ###############

class plasmaProteinSchemas:
  schemaIndexPath = None

  ############# error reporting #############

  #to allow for later non-stdout error redirection
  def err(self, msg):       print("CPlasma error:", msg)          
  def msgUpdate(self, msg): print("CPlasma message update:", msg) 

  ############# constructor #############

  def __init__(self, **kwargs):
    self.msgCallbackDict  = {}

    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

### end ###

