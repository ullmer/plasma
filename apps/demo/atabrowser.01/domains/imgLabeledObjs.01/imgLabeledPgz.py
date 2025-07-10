# Image-labeled objects warm-up example
# Brygg Ullmer, Clemson University
# Begun 2025-07-09

import os, yaml
from imgLabeledObj import *
  
########## primary class ##########

class ADImgLabeledObjPgz(ADImgLabeledObj):

  actorDict = None
  actorFns  = None
  actorWH   = None
  actors    = None
  basePos      = ( 50,  50)
  actorPosDiff = (300, 210)
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
      bx, by         = self.basePos
      dx, dy         = self.actorPosDiff

      x, y = bx, by
      for actorFn in self.actorFns:
        a = Actor(actorFn, pos=(x,y))
        self.actorDict[actorFn] = a
        actors.append(a) #space-inefficient to store in both a lookup and a list; but easier to follow for some
        x += dx; y += dy

      return True
    except: self.err("loadYaml"); return False

  ########## pgz draw method ##########
  def draw(self, screen):

### end ###
