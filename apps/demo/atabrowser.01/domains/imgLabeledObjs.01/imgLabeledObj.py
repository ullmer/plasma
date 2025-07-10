# Image-labeled objects warm-up example
# Brygg Ullmer, Clemson University
# Begun 2025-07-09

import os
from ataDomain import *

class ADImgLabeledObj(AtaDomain):
  yamlPath = '~/git/plasma/apps/demo/atabrowser.01/yaml/'
  yamlFn   = 'us_nps/sc.yaml'

  ########## constructor ##########
  def __init__(self): self.loadYaml()

  ########## loadYaml ##########
  def loadYaml(self):
    if self.yamlPath is None or self.yamlFn is None:
      self.msg("loadYaml: yamlPath or yamlFn presently unassigned"); return

    relPath = self.yamlPath + self.yamlFn
    absPath = os.path.expanduser(relPath)
    if not os.path.isfile(absPath):
      self.msg("loadYaml: file of specified path not found: " + str(absPath))
      return
    else:
      self.msg("loadYaml: file of specified path found: " + str(absPath))

########## main ##########
if __name__ == "__main__":
  adilo = ADImgLabeledObj()

#Initial key directories
#./domains/imgLabeledObjs.01
#./images/us_nps/meta
#./yaml/us_nps

### end ###
