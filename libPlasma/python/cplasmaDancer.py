# Cython bindings around libPlasma/c
# Lead by Brygg Ullmer, Clemson University
# Begun 2024-07-13

import sys; sys.path.append("/home/ullmer/git/plasma/libPlasma/python/")
import cplasma
import asyncio, sys, time, traceback

from   functools      import partial # for callback support
from   cplasmaWatcher import *

#############################################################
###################### cplasma dancer ######################

# builds on the monitoring functionalities of CPlasmaWatcher to add emissive capabilities

class CPlasmaDancer(CPlasmaWatcher):
  poolSpecifier = "tcp://localhost/hello" #default, will benefit from evolution
  msgFormatName = "prot:simpleKeyVal"
  msgFormatStr  = None
  msgCallbackDict  = None
  sleepDuration = .01

  ############# error reporting #############

  #to allow for later non-stdout error redirection
  def err(self, msg):       print("CPlasmaDancer error:", msg)          
  def msgUpdate(self, msg): print("CPlasmaDancer message update:", msg) 

  ############# constructor #############

  def __init__(self, **kwargs):
    self.msgCallbackDict  = {}

    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

    if self.poolSpecifier is None: self.err("constructor: poolSpecifier not provided"); return -1
    self.initPlasma(self.poolSpecifier)

### end ###

