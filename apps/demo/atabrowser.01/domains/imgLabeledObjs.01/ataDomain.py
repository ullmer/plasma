# Animist Tangible Allomorphs Domain
# Brygg Ullmer, Clemson University
# Begun 2025-07-09

import os, traceback, yaml

########## animist tangible allomorphs domain ##########

class AtaDomain:
  yamlPath = '~/git/plasma/apps/demo/atabrowser.01/yaml/'
  yamlFn   = None
  yamlD    = None
  verbose  = True
  yamlPathSeparator = ':' #allowing paths to be expressed like a:b:c

  ########## constructor ##########
  def __init__(self): self.loadYaml()

  ########## message ##########
  def msg(self, mstr: str): 
    mstr2 = self.getClassName() + ' msg: ' + mstr; print(mstr2)

  def getClassName(self): return self.__class__.__name__

  ########## error ##########
  def err(self, estr: str):
    estr2 = self.getClassName() + ' err: ' + estr; print(estr2)
    traceback.print_exc(); 

  ########## loadYaml ##########
  def loadYaml(self):
    if self.yamlPath is None or self.yamlFn is None:
      self.msg("loadYaml: yamlPath or yamlFn presently unassigned"); return

    try:
      relPath = self.yamlPath + self.yamlFn
      absPath = os.path.expanduser(relPath)
      if not os.path.isfile(absPath):
        self.msg("loadYaml: file of specified path not found: " + str(absPath))
        return
      else:
        f = open(absPath)
        self.yamlD = yaml.safe_load(f)
        f.close()

      return True
    except: self.err("loadYaml"); return False

  ########## loadYaml ##########
  def getYamlPath(self, path: str):
    if self.yamlD is None:
      self.msg("getYamlPath: yamlD not yet assigned!"); return None

    try:
      keys = path.split(self.yamlPathSeparator)
      if self.verbose: self.msg("getYamlPath " + str(keys))
      yd = self.yamlD
      for key in keys:
        if isinstance(yd, dict) and key in yd: data = yd[key]
        else:                                  return None

      return data
    except: self.err("getYamlPath")

  ########## loadYaml ##########
  def printYaml(self): print(self.yamlD)

########## main ##########
if __name__ == "__main__":
  ad = AtaDomain()
  ad.msg("hello world")

### end ###
