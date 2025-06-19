# Example visual application toward Animist
# Brygg Ullmer, Clemson University
# Begun 2025-06-02

import pygame, traceback, sys
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
  glyphActorDict   = None
  glyphDeltaDict   = None
  glyphList        = None
  activatePlasma   = False

  glyphs = 'b1,b2,b3,bl,l1,l2,l3,' + \
           'r1,r2,r3,t1,t2,t3,tr,' + \
           'br1,br2,sb1,sb2,sl1,sl2,sr1,' + \
           'sr2,st1,st2,stl,hl1,hl2,fr'

  delta1, delta2 = 350, 50 
  dxDict, dyDict = None, None
  cx, cy         = 400, 400

  glyphPrefix = 'deco/tbox02n_'

  actorSq = None
  verbose = False

  ########### constructor ########### 

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    super().__init__()
    self.buildDeltas()
    self.buildActors()
 
    if self.activatePlasma: self.initPlasma()

  def msg(self, msgstr): print("enoPgzASquareAnim message: " + str(msgstr))
  def err(self, msgstr): print("enoPgzASquareAnim error: "   + str(msgstr)); traceback.print_exc()
  ########### build actors ########### 

  def buildActors(self):
    gdd = self.glyphDeltaDict 
    if gdd is None: self.msg("buildActors: please call buildDeltas first"); return

    self.glyphActorDict      = {}
    self.glyphList           = self.glyphs.split(',')
    self.dxDict, self.dyDict = {}, {}

    self.msg("buildActors gl: " + str(self.glyphList))

    for glyphFn in self.glyphList:
      fn = self.glyphPrefix + glyphFn
      self.msg("buildActors fn: " + fn) 
      a  = Actor(fn)
      self.glyphActorDict[fn] = a
      if glyphFn in gdd:
        pos = gdd[glyphFn]
        a.pos = pos

  ########### build deltas ########### 

  def buildDeltas(self):
     d1, d2 = self.delta1, self.delta2
     cx, cy = self.cx,     self.cy

     bx, by = cx, cy - d1
     tx, ty = cx, cy + d1
     rx, ry = cx + d1, cy
     lx, ly = cx - d1, cy

     bx1, bx2, bx3 = bx - d2, bx, bx + d2
     ly1, ly2, ly3 = ly - d2, ly, ly + d2
     tx1, tx2, tx3 = bx1, bx2, bx3
     ry1, ry2, ry3 = ly1, ly2, ly3

     gdd = self.glyphDeltaDict = {}

     glyphL1     = 'b1,b2,b3,t1,t2,t3'.split(',')
     glyphCoords1 = [(bx1, by), (bx2, by), (bx3, by), (tx1, ty), (tx2, ty), (tx3, ty)]
     for glyphN, glyphCoord in zip(glyphL1, glyphCoords1): gdd[glyphN] = glyphCoord

     glyphL2      = 'l1,l2,l3,r1,r2,r3'.split(',')
     glyphCoords2 = [(lx, ly1), (lx, ly2), (lx, ly3), (rx, ry1), (rx, ry2), (rx, ry3)]
     for glyphN, glyphCoord in zip(glyphL2, glyphCoords2): gdd[glyphN] = glyphCoord

     gdd['bl'] = [cx-d1, cy+d1]
     gdd['tr'] = [cx+d1, cy-d1]

#           'br1,br2,sb1,sb2,sl1,sl2,sr1,' +
#           'sr2,st1,st2,stl,hl1,hl2,fr'

  ########### draw ########### 

  def draw(self, screen):
    super().draw(screen)

    for glyphFn in self.glyphList:
      a = self.glyphActorDict[fn] 
      if glyphFn in gdd: a.draw()

  ########### init plasma ########### 

  def initPlasma(self):
    self.plasmaListener = enoPlasmaListener(poolName = self.poolName, 
                                            callback = self.plasmaCB)
    self.plasmaListener.start()
    self.pscope = plasma.create.string(self.pscopeStr)

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

  def parseMessage(self, d, il):
    try:
      if d != self.pscopeStr: return #ignore if not for us
      obj, cmd, x1, y1 = il

      if obj != self.psq1Str: return
      if cmd != self.pmovStr: return

      x0, y0 = self.actorBox.pos
      if x1 != x0 or y1 != y0: 
        self.actorBox.pos = (x1, y1)

    except: self.err("parseMessage")

  ########### init plasma ########### 

  def broadcastBoxMove(self, pos):
    plist = []; x, y = pos
    
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
  
