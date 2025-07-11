# Image-labeled objects warm-up example
# Brygg Ullmer, Clemson University
# Begun 2025-07-09

import os, yaml
from imgLabeledObj import *
from pgzero.builtins import Actor, animate, keyboard, keys

########## primary class ##########

class ADImgLabeledObjPgz(ADImgLabeledObj):

  imgPathPrefix = 'us_nps/meta/'

  actorDict = None
  actorFns  = None
  actorWH   = None
  actors    = None
  verbose   = True
  basePos      = (460, 110)
  actorPosDiff = (600, 210)
  numCols      =  2

  ########## initiate pygame zero ##########
  def initPgz(self):
    try:
      ilmd = self.imgLabeledMetad 

      if ilmd is None: 
        self.msg("initPgz expects metadata to be expanded, but isn't so");    return False

      if 'fn' not in ilmd:
        self.msg("initPgz: filename not present in metadata where expected"); return False

      if 'dim' not in ilmd:
        self.msg("initPgz: image dimension not present in metadata where expected"); return False

      self.actorFns  = ilmd['fn']
      self.actorWH   = ilmd['dim']
      self.actorDict = {}
      self.actors    = []
      bx, by         = self.basePos
      dx, dy         = self.actorPosDiff

      x, y       = bx, by
      idxX, idxY = 0, 0

      for actorFn in self.actorFns:
        fn = self.imgPathPrefix + actorFn
        a = Actor(fn, pos=(x,y))
        self.actorDict[actorFn] = a
        self.actors.append(a) #space-inefficient to store in both a lookup and a list; 
                              # but easier to follow for some

        idxX += 1; x += dx
        if idxX >= self.numCols: 
          idxX  = 0
          idxY += 1
          x     = bx
          y    += dy

      return True
    except: self.err("loadYaml"); return False

  ########## pgz draw method ##########
  def draw(self, screen):
    try:
      if self.actors is None: 
        if self.verbose: self.msg("draw called, but no actors present"); return
      for a in self.actors: a.draw()
    except: self.err("draw")

### end ###
