# Image-labeled objects warm-up example
# Brygg Ullmer, Clemson University
# Begun 2025-07-09

import os, yaml
from vizLands import *
from pgzero.builtins import Actor, animate, keyboard, keys

########## primary class ##########

class ADVizLandsPgz(ADVizLands):

  imgPathPrefix1 = 'us_nps/meta/'
  imgPathPrefix2 = 'us_nps/cache/'

  actorDictMeta  = None
  actorDictThumb = None
  actorFns  = None
  actorWH   = None
  verbose   = True
  basePos      = (460, 110)
  actorPosDiff = (600, 210)
  actRelDiff   = (-500, 0) #clearly inadequate naming, but a start
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
      dx1, dy1       = self.actorPosDiff
      dx2, dy2       = self.actRelDiff

      x, y       = bx, by
      idxX, idxY = 0, 0

      for actorFn in self.actorFns:
        fn1 = self.imgPathPrefix1 + actorFn
        fn2 = self.imgPathPrefix2 + self.img1x
        if self.verbose: self.msg("1+2: " + str([fn1, fn2]))
        a1 = Actor(fn1, pos=(x,y))
        a2 = Actor(fn2, pos=(x+dx2, y+dy2))

        self.actorDictMeta[actorFn]  = a1
        self.actorDictThumb[actorFn] = a2

        idxX += 1; x += dx1
        if idxX >= self.numCols: 
          idxX  = 0
          idxY += 1
          x     = bx
          y    += dy1

        objHandle = actorFn[:-1] 

        if self.objDetailsDict is None:
          self.msg("initPgz: object details dictionary is not populated"); return False

        if objHandle in self.objDetailsDict: # get associated image filename
          pass

      return True
    except: self.err("loadYaml"); return False

  ########## pgz draw method ##########
  def draw(self, screen):
    try:
      if self.actorDictThumb is not None: 
       for an in self.actorDictThumb:
         a1 = self.actorDictThumb[an]
         a1.draw()
        
      if self.actorDictMeta is not None: 
       for an in self.actorDictMeta:
         a1 = self.actorDictMeta[an]
         a1.draw()

    except: self.err("draw")

### end ###
