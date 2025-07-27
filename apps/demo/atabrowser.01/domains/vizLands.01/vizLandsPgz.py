# Image-labeled objects warm-up example
# Brygg Ullmer, Clemson University
# Begun 2025-07-09

import os, yaml
from vizLands import *
from ataFileCache  import *
from ataLabelBlock import *

from pgzero.builtins import Actor, animate, keyboard, keys

########## primary class ##########

class ADVizLandsPgz(ADVizLands):

  imgPathPrefix1 = 'us_nps/meta/'
  #imgPathPrefix2 = 'us_nps/cache1/'
  imgPathPrefix2 = ''

  actorDictMeta  = None
  actorDictThumb = None
  afCache        = None
  alb            = None #AtaLabelBlock()

  actorFns  = None
  actorWH   = None
  verbose   = False
  basePos      = ( 800, 150)
  labelOffset  = (-300, -85)
  actorPosDiff = ( 775, 245)
  actRelDiff   = (-410,  10) #clearly inadequate naming, but a start
  numCols      =  2
  firstActor   = 8
  currentActor = 0

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

      self.alb = AtaLabelBlock()

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
      lox, loy   = self.labelOffset  
      self.alb.createAlphaSurface2("blk100", 275, 100, (80,80,100), 128)

      for actorFn in self.actorFns:
        if self.firstActor is not None and \
           self.firstActor > self.currentActor: 
              self.currentActor += 1; continue

        if self.verbose: self.msg("initPgz: " + str(actorFn))
        fn1 = self.imgPathPrefix1 + actorFn

        i1x, i1xFn = 'image1x', None
        if actorFn[-1] == '2': af = actorFn[:-1]
        else:                  af = actorFn #so hacky, sigh; race toward functionality
        #self.msg("foo: " + af)

        if af in od:
          entry = od[af]
          if i1x in entry:
            i1xFn = entry[i1x]

        if i1xFn is not None: 
          fn2 = self.imgPathPrefix2 + i1xFn
          fn3 = self.afCache.cachePath(fn2)
          fn4, ext = os.path.splitext(fn3)
          fn5 = fn4[7:] # skip "images/" prefix"

          if self.verbose: self.msg("1+2+5: " + str([fn1, fn2, fn5]))

        try:    a1 = Actor(fn1, pos=(x,y))
        except: a1 = None

        try:    a2 = Actor(fn5, pos=(x+dx2, y+dy2))
        except: a2 = None

        self.actorDictMeta[actorFn]  = a1
        self.actorDictThumb[actorFn] = a2

        try:    name = od[af]['name']
        except: name=''

        atsName = 'box_' + af

        self.alb.placeAlphaTextSurface(atsName, "blk100", x+lox, y+loy, af, name)

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
          #if 'kimo2' == an: continue
          a1 = self.actorDictThumb[an]
          if a1 is not None: a1.draw()
        
      if self.actorDictMeta is not None: 
        for an in self.actorDictMeta:
          a1 = self.actorDictMeta[an]
          if a1 is not None: a1.draw()

      self.alb.draw(screen)

    except: self.err("draw")

  ########## pgz mouse events ##########

  def on_mouse_down(self, pos): pass
  def on_mouse_move(self, rel): pass
  def on_mouse_up(self):        pass

### end ###
