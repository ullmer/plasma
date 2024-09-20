# Py4J bindings around libPlasma/java
# Originally expressed as cplasma Cython bindings around libPlasma/c
# Lead by Brygg Ullmer, Clemson University
# cplasma bindings begun 2024-07-13
# py4jplasma bindings begun 2024-09-20

import sys; sys.path.append("/home/ullmer/git/plasma/libPlasma/python/")
import p4jPlasma
import asyncio, sys, time, traceback
from   functools import partial # for callback support

#############################################################
###################### cplasma watcher ######################

#note that name is a bit of a misnomer, as deposits also equally supported
# in celebration of that, contemplating a child class, CPlasmaDancer 
#   (as a slight nod toward Plasma's apparent penchant for wordplay and mixed metaphor :-)

class p4jPlasmaWatcher:
  poolSpecifier = "tcp://localhost/hello" #default, will benefit from evolution
  msgFormatName = "prot:simpleKeyVal"
  msgFormatStr  = None
  msgCallbackDict  = None
  sleepDuration    = .01
  p4jp          = None #handle for instances of p4jPlasma

  ############# error reporting #############

  #to allow for later non-stdout error redirection
  def err(self, msg):       print("p4jPlasmaWatcher error:", msg)          
  def msgUpdate(self, msg): print("p4jPlasmaWatcher message update:", msg) 

  ############# constructor #############

  def __init__(self, **kwargs):
    self.msgCallbackDict  = {}

    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

    if self.poolSpecifier is None: self.err("constructor: poolSpecifier not provided"); return -1
     
    self.initPlasma(self.poolSpecifier)
  
  ############# plasma watcher #############

  async def plasmaWatcher(self):

    while True:
      try:    strs = p4jplasma.pNext(self.msgFormatStr)
      except: print("plasmaWatcher: pNext error!"); return

      if strs is None: await asyncio.sleep(self.sleepDuration)
      else: 
        try:    self.evalMsgCallbacks(strs)
        except: self.err("plasmaWatcher message callback error:"); traceback.print_exc();           

  ############# initiate C Plasma #############

  def initPlasma(self, poolSpecifier=None): 
    self.msgUpdate("plasma initiating, pool specifier:" + poolSpecifier)

    self.p4jp = p4jPlasma()

    self.p4jp.init("tcp://localhost/hello")
    self.msgFormatStr = self.p4jp.getProtFormatStr(self.msgFormatName)
    asyncio.run(self.plasmaWatcher())
    
  ############# plasma deposit #############

  #def deposit(self, descrips="hello", ingests="world"): 
  def deposit(self, descrips, ingests): 
    self.p4jp.pDeposit(descrips, ingests)

  ############# plasma close #############

  def close(): self.p4jp.close()

  ############# register callback #############

  #perhaps should key these on protein signature

  def registerMsgCallback(self, callbackName, callbackFunc): 
    if self.msgCallbackDict == None: self.msgCallbackDict = {}

    # https://www.geeksforgeeks.org/partial-functions-python/
    # cb = partial(callback, controlName)
    self.msgCallbackDict[callbackName] = callbackFunc

  ############# default message callback #############

  def defaultMsgCallback(self, msg):
    self.msgUpdate("default msg cb:" + str(msg))

  ############# register callback #############

  def evalMsgCallbacks(self, msg):
    if len(self.msgCallbackDict) == 0:
      self.defaultMsgCallback(msg)

    for callbackName in self.msgCallbackDict:
      callbackFunc = self.msgCallbackDict[callbackName]
      callbackFunc(msg)

  ############# debug callback #############

  #def debugCallback(self, control, arg):
  #  print("enoMidiController debugCallback: ", str(control), str(arg))
  #  self.msgUpdate(self, msg): print("debugCallback CPlasma message update:", msg) 
 
################################
############# main #############

if __name__ == '__main__':
  cpw = CPlasmaWatcher()

### end ###

