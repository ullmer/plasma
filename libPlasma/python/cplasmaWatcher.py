# Cython bindings around libPlasma/c
# Lead by Brygg Ullmer, Clemson University
# Begun 2024-07-13

import sys; sys.path.append("/home/ullmer/git/plasma/libPlasma/python/")
import cplasma
import asyncio, sys, time
from   functools import partial # for callback support

#############################################################
###################### cplasma watcher ######################

#note that name is a bit of a misnomer, as deposits also equally supported
# in celebration of that, contemplating a child class, CPlasmaDancer 
#   (as a slight nod toward Plasma's apparent penchant for wordplay and mixed metaphor :-)

class CPlasmaWatcher:
  poolSpecifier = "tcp://localhost/hello" #default, will benefit from evolution
  msgFormatName = "prot:simpleKeyVal"
  msgFormatStr  = None
  callbackList  = None
  sleepDuration = .01

  ############# error reporting #############

  #to allow for later non-stdout error redirection
  def err(self, msg):       print("CPlasma error:", msg)          
  def msgUpdate(self, msg): print("CPlasma message update:", msg) 

  ############# constructor #############

  def __init__(self, **kwargs):
    self.callbackList = []

    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

    if self.poolSpecifier is None: self.err("constructor: poolSpecifier not provided"); return -1
     
    self.initPlasma(self.poolSpecifier)
  
  ############# plasma watcher #############

  async def plasmaWatcher(self):

    while True:
      try:    strs = cplasma.pNext(self.msgFormatStr)
      except: print("plasmaWatcher: pNext error!"); return

      if strs is None: await asyncio.sleep(self.sleepDuration)
      else: print("<<%s>>" % strs)

  ############# initiate C Plasma #############

  def initPlasma(self, poolSpecifier=None): 
    self.msgUpdate("plasma initiating, pool specifier:" + poolSpecifier)
    cplasma.init("tcp://localhost/hello")
    self.msgFormatStr = cplasma.getProtFormatStr(self.msgFormatName)
    asyncio.run(self.plasmaWatcher())
    
  ############# plasma deposit #############

  def deposit(self, descrips="hello", ingests="world"): 
    cplasma.pDeposit(descrips, ingests)

  ############# plasma deposit #############

  def close(): cplasma.close()
 
################################
############# main #############

if __name__ == '__main__':
  cpw = CPlasmaWatcher()

### end ###

