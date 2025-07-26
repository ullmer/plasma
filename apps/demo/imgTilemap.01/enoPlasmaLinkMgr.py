# Enodia Plasma image navigator 
# Brygg Ullmer, Clemson University
# Begun 2025-07-23

try: import plasma
except: print("import plasma not possible")

import time, sys, traceback
from   ataBase           import *
from   enoPlasmaListener import *
  
###################### enodia plasma image navigator #####################

class EnoPlasmaLinkMgr(AtaBase):
  #poolName = "tcp://localhost/grObjPool" #graphical object pool
  poolName = "tcp://192.168.5.121/grObjPool" #graphical object pool
  hose     = None
  verbose  = True
  scope    = "sharedCanvas"
  pscope   = None
  listener = None
  callback = None

  ###################### constructor #####################

  def __init__(self, **kwargs):
    try:
      self.__dict__.update(kwargs) #allow class fields to be passed in constructor
      super().__init__()
      if self.poolName is not None: self.initPlasmaLink()
    except: self.err("constructor")

  ###################### start plasma listener #####################
   
  def startPlasmaListener(self, cb):
    try:
       pn = self.poolName
       self.listener = EnoPlasmaListener(poolName=pn, callback=cb)
       self.listener.start()
    except: self.err("startPlasmaListener")

  ###################### initiate plasma link #####################
   
  def initPlasmaLink(self):
    try:
      pn = self.poolName
      self.hose = plasma.Pool.Participate(pn)

      if self.hose is None:
        self.msg("initPlasmaLink: Failed to connect to pool: " + pn); return False

      cb = self.callback
      if cb is not None: self.startPlasmaListener(cb)

    except: self.err("initPlasmaLink")

  ###################### initiate plasma link #####################
   
  def closePlasmaLink(self):
    try:
      if self.hose is not None: hose.Withdraw()
    except: self.err("closePlasmaLink")


###################### main #####################

def main():
  eplm = EnoPlasmaLinkMgr()

  for i in range(1000): 
    print(str(i) + " ", end='')
    sys.stdout.flush(); time.sleep(1.)

if __name__ == "__main__":
  main()

### end ###
