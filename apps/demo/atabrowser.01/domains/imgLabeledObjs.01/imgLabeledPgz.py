# Image-labeled objects warm-up example
# Brygg Ullmer, Clemson University
# Begun 2025-07-09

import os, yaml
from imgLabeledObj import *
  
########## primary class ##########

class ADImgLabeledObjPgz(ADImgLabeledObj):

  actorDict = None
  actorFns  = None

  ########## initiate pygame zero ##########
  def initPgz(self):
    try:
      ilmd = self.imgLabeledMetad 

      if ilmd is None: 
        self.msg("initPgz expects metadata to be expanded, but isn't so");    return False

      if 'fn' not in ilmd:
        self.msg("initPgz: filename not present in metadata where expected"); return False

      self.actorFns  = ilmd['fn']
      self.actorDict = {}

       for 

      super().loadYaml()
      ilmd = self.imgLabeledMetad = self.getYamlPath(self.yamlPath1)
      if ilmd is None: 
        self.msg("loadYaml: not finding anticipated data here: " + str(self.yamlPath1))
        return False
      self.msg("loadYaml d: " + str(ilmd))

      return True
    except: self.err("loadYaml"); return False

  ########## pgz draw method ##########
  def draw(self, screen):

### end ###
