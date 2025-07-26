# Enodia Plasma image navigator 
# Brygg Ullmer, Clemson University
# Begun 2025-07-23

import plasma
import time, sys, traceback
from   ataBase           import *
from   enoPlasmaListener import *
from   enoPlasmaLinkMgr  import *
  
###################### enodia plasma image navigator #####################

class EnoPlasmaImgNav(EnoPlasmaLinkMgr):
  defaultObjName    = 'map'
  defaultActionName = 'move'
  mapMoveCb         = None
  verbose           = False

  ###################### constructor #####################

  def __init__(self, **kwargs):
    try:
      self.__dict__.update(kwargs) #allow class fields to be passed in constructor
      super().__init__()
    except: self.err("constructor")

  ###################### deposit map update #####################

  def depositMapSimpleUpdate(self, coords: list[int]):
    try:
      obj    = self.defaultObjName 
      action = self.defaultActionName 
      self.depositMapUpdate(obj, action, coords)
    except: self.err("depositMapSimpleUpdate")

  ###################### deposit map update #####################

  def depositMapUpdate(self, objName: str, action: str, coords: list[int]):
    try:
      if self.pscope is None: self.pscope = plasma.create.string(self.scope)
      x, y = coords
      psObjName    = plasma.create.string(objName)
      psObjAction  = plasma.create.string(action)
      psObjLoc     = plasma.create.v2int32(x,y)
      psObjUpdates = plasma.create.list([psObjName, psObjAction, psObjLoc])

      protein = plasma.Protein(self.pscope, psObjUpdates)
      pn      = self.poolName

      if self.verbose: print(f"depositing in {pn}")
      #if self.verbose: print(protein.ToSlaw().ToString())

      try:    ret = self.hose.Deposit(protein)
      except: self.err("depositMapUpdate: error on hose deposit"); return False

      if ret.IsError():
        self.msg("depositMapUpdate: no luck on the deposit: {ret}"); return False
    except: self.err("depositMapUpdate")

  ###################### handle message #####################

  def registerMapMoveCb(self, mapMoveCb): 
    self.mapMoveCb = mapMoveCb

  ###################### handle message #####################

  def handleMsg(self, protein): 
    try:
      if self.verbose: print("!", end=''); sys.stdout.flush()
      d,  i  = protein.Descrips(), protein.Ingests()
      dl, il = d.getList(), i.getList()
      if self.verbose: self.msg("hm D:" + str(dl[0]))
      if self.verbose: self.msg("hm I:" + str(il))

      try:    self.mapMoveCb(il[2])
      except: self.err("handleMsg challenge in invoking user mapMoveCb")

      #if len(dl) == 1 and d.getStr() == self.scope: 
      #  if self.verbose: self.msg("handleMsg receiving " + self.scope)
      #  if len(il) == 3 and il[1].getStr() == self.defaultActionName:
      #    if self.verbose: self.msg("handleMsg noting action " + self.defaultAction)
      #    if self.mapMoveCb is not None: 
      #      try:    self.mapMoveCb(il[2])
      #      except: self.err("handleMsg challenge in invoking user mapMoveCb")
      #    else: self.msg("handleMsg called, but mapMoveCb not yet registered")
 
    except: self.err("handleMsg")

###################### main #####################

def main():
  epin = EnoPlasmaImgNav()
  epin.startPlasmaListener(epin.handleMsg)

  epin.depositMapUpdate("sq1", "move", (10, 10))
  
  for i in range(1000): 
    print(str(i) + " ", end='')
    sys.stdout.flush(); time.sleep(1.)

if __name__ == "__main__":
  main()

### end ###
