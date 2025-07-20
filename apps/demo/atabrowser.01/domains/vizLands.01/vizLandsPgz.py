# Image-labeled objects warm-up example
# Brygg Ullmer, Clemson University
# Begun 2025-07-09

import os, yaml
from vizLands import *
from ataFileCache import *

from pgzero.builtins import Actor, animate, keyboard, keys

########## primary class ##########

class ADVizLandsPgz(ADVizLands):

  imgPathPrefix1 = 'us_nps/meta/'
  #imgPathPrefix2 = 'us_nps/cache1/'
  imgPathPrefix2 = ''

  actorDictMeta  = None
  actorDictThumb = None
  afCache        = None

  actorFns  = None
  actorWH   = None
  verbose   = True
  basePos      = (760,  150)
  actorPosDiff = (890,  250)
  actRelDiff   = (-410,  10) #clearly inadequate naming, but a start
  numCols      =  2

  ########## constructor ##########

  def __init__(self):
    self.actorDictMeta  = {}
    self.actorDictThumb = {}
    self.afCache = AtaFileCache()

  ########## initiate pygame zero ##########
  def initPgz(self):
    try:
      ilmd = self.imgLabeledMetad 
      od   = self.objDetailsDict

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

        i1x, i1xFn = 'image1x', None
        af = actorFn[:-1]
        self.msg("foo: " + af)
        if af in od:
          entry = od[af]
          if i1x in entry:
            i1xFn = entry[i1x]
 
        fn2 = self.imgPathPrefix2 + i1xFn
        fn3 = self.afCache.cachePath(fn2)

        fn4, ext = os.path.splitext(fn3)
        fn5 = fn4[7:] # skip "images/" prefix"
        if self.verbose: self.msg("1+2+5: " + str([fn1, fn2, fn5]))

        a1 = Actor(fn1, pos=(x,y))
        a2 = Actor(fn5, pos=(x+dx2, y+dy2))

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
         if 'kimo2' == an: continue
         a1 = self.actorDictThumb[an]
         a1.draw()
        
      if self.actorDictMeta is not None: 
       for an in self.actorDictMeta:
         a1 = self.actorDictMeta[an]
         a1.draw()

    except: self.err("draw")

### end ###
