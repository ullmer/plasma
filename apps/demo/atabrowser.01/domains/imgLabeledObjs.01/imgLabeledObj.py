# Image-labeled objects warm-up example
# Brygg Ullmer, Clemson University
# Begun 2025-07-09

import os, yaml
from ataDomain import *

class ADImgLabeledObj(AtaDomain):
  yamlPath = '~/git/plasma/apps/demo/atabrowser.01/yaml/'
  yamlFn   = 'us_nps/sc.yaml'
  yamlD    = None

  ########## constructor ##########
  def __init__(self): self.loadYaml()

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
    except: self.err("exception")

  ########## loadYaml ##########
  def printYaml(self): print(self.yamlD)

########## main ##########
if __name__ == "__main__":
  adilo = ADImgLabeledObj()
  print("yaml:")
  adilo.printYaml()

#Initial key directories
#./domains/imgLabeledObjs.01
#./images/us_nps/meta
#./yaml/us_nps

### end ###
