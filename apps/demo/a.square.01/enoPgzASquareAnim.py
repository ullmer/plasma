# Example visual application toward Animist
# Brygg Ullmer, Clemson University
# Begun 2025-06-02

import pygame, traceback
from enoPgzASquare     import *
from pgzero.builtins   import Actor, animate, keyboard, keys
from enoPlasmaListener import *
import plasma

######## enodia pygame zero animist square ######## 

class enoPgzASquareAnim(enoPgzASquare):
  imgSqFn  = 'sspirito01h'
  poolName = 'tcp://localhost/grObjPool'
  plasmaListener   = None
  pscope           = None
  pscopeStr        = "sharedCanvas"
  psq1Str, pmovStr = "sq1", "move"
  psq1, pmov       = [None]*2 

  actorSq = None
  verbose = False

  ########### constructor ########### 

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    super().__init__()
    self.initPlasma()

  def msg(self, msgstr): print("enoPgzASquareAnim message: " + str(msgstr))
  def err(self, msgstr): print("enoPgzASquareAnim error: "   + str(msgstr)); traceback.print_exc()

  ########### init plasma ########### 

  def initPlasma(self):
    self.plasmaListener = enoPlasmaListener(poolName = self.poolName, 
                                            callback = self.plasmaCB)
    self.plasmaListener.start()
    self.pscope = plasma.create.string(self.pscope)

  ########### init plasma ########### 

  def plasmaCB(self, protein):
    try:
      d,  i  = protein.Descrips(), protein.Ingests()
      dl, il = d.getList(), i.getList()
      if self.verbose: print(" D:", str(dl[0]), end='')
      if self.verbose: print(" I:", str(il))
      self.parseMessage(dl[0], il)

    except: self.err("plasmaCB")

  ########### parseMessage ########### 

  def parseMessage(self, d, i):
    try:
      if d != self.pscope: return #self.msg("parseMessage: ignoring " + str(d))

    except: self.err("parseMessage")

  ########### init plasma ########### 

  def broadcastBoxMove(self, pos):
    plist  = []; x, y = pos
    
    if self.psq1 is None: self.psq1 = plasma.create.string(self.psq1Str)
    if self.pmov is None: self.pmov = plasma.create.string(self.pmovStr)

    for i in [self.psq1, self.pmov]: plist.append(i)
    plist.append(plasma.create.v2int32(int(x),int(y)))
    pmsg = plasma.create.list(plist)
    msg  = plasma.Protein(self.pscope, pmsg)
    ret  = self.plasmaListener.deposit(msg)
    if ret.IsError():
      self.msg(f"broadcastBoxMove: deposit challenges: {ret}")

  ########### prepare actors ########### 

  def prepActors(self):
    super().prepActors()
    #self.actorSq     = enoActorScaled(self.imgSqFn,      pos=(1000, 500), 
    #                                               scale=.2, alpha = 220)

  ################## on_mouse_move ##################

  def on_mouse_move(self, rel, buttons):
    super().on_mouse_move(rel, buttons)
    if self.boxSelected:
      pos = self.actorBox.pos
      self.broadcastBoxMove(pos)

### end ###
  
