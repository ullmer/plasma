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
  plasmaListener = None

  actorSq = None

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
        
  ########### init plasma ########### 

  def plasmaCB(self, protein):
    try:
      d,  i  = protein.Descrips(), protein.Ingests()
      dl, il = d.getList(), i.getList()
      print("D:", str(dl[0]))
      print("I:", str(il))
    except: print("exception"); traceback.print_exc()

  ########### init plasma ########### 

  def broadcastBoxMove(self, pos):
    pscope = plasma.create.string("sharedCanvas")
    plist  = []; x, y = pos
    plist.append(plasma.create.string("sq1"))
    plist.append(plasma.create.string("move"))
    plist.append(plasma.create.v2int32(x,y))
    pmsg = plasma.create.list(plist)
    msg  = plasma.Protein(pscope, pmsg)
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
  
