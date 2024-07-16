# Cython bindings around libPlasma/c
# Lead by Brygg Ullmer, Clemson University
# Begun 2024-07-13

import sys; sys.path.append("/home/ullmer/git/plasma/libPlasma/python/")
import cplasma
import asyncio, sys, time

class CPlasmaWatcher:
  poolSpecifier = "tcp://localhost/hello" #default, will benefit from evolution

  ############# error reporting #############

  #to allow for later non-stdout error redirection
  def err(self, msg):       print("CPlasma error:", msg)          
  def msgUpdate(self, msg): print("CPlasma message update:", msg) 

  ############# constructor #############

  def __init__(self, **kwargs):
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

    if self.poolSpecifier is None: self.err("constructor: poolSpecifier not provided"); return -1
     
    self.initPlasma(self.poolSpecifier)
  
  ############# initiate C Plasma #############

  def initPlasma(self, poolSpecifier=None): 
    self.msgUpdate("plasma initiating, pool specifier:", poolSpecifier)
    cplasma.init("tcp://localhost/hello")
    
  ############# plasma deposit #############

  def deposit(self, descrips="hello", ingests="world"): 
    cplasma.pDeposit(descrips, ingests)

  ############# plasma deposit #############

  def close(): cplasma.close()
 

################################
############# main #############

if __name__ == "__main__":
  p = CPlasma("tcp://localhost/hello")

### end ###

fmtStr        = cplasma.getProtFormatStr('prot:simpleKeyVal')
sleepDuration = .01

async def plasmaWatcher():
  global sleepDuration, fmtStr

  while True:
    try:    strs = cplasma.pNext(fmtStr)
    except: print("plasmaWatcher: pNext error!"); return

    if strs is None: await asyncio.sleep(sleepDuration)
    else: print("<<%s>>" % strs)

asyncio.run(plasmaWatcher())

cplasma.close()

### end ###

