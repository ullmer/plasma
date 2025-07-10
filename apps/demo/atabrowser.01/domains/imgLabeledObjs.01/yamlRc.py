# YAML resource files
# Brygg Ullmer, Clemson University
# Begun 2025-07-09

import os, traceback, yaml

########## YAML resource file ##########

class YamlRc(AtaBase): 
  yamlPath = '~/git/plasma/apps/demo/atabrowser.01/yaml/'
  yamlFn   = None
  yamlD    = None
  verbose  = True
  yamlPathSeparator = ':' #allowing paths to be expressed like a:b:c

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
      d = self.yamlD
      for key in keys:
        if isinstance(d, dict) and key in d: d = d[key]
        else:                                return None

      return d
    except: self.err("getYamlPath")

  ########## loadYaml ##########
  def printYaml(self): print(self.yamlD)

########## main ##########
if __name__ == "__main__":
  yr = YamlRc()
  yr.msg("hello world")

### end ###
