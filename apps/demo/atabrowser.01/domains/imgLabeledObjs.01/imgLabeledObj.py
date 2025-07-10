# Image-labeled objects warm-up example
# Brygg Ullmer, Clemson University
# Begun 2025-07-09

import os, yaml
from ataDomain import *

class ADImgLabeledObj(AtaDomain):
  yamlFn    = 'us_nps/sc.yaml'
  yamlPath1 = 'sc:nps:meta'

  ########## loadYaml ##########
  def loadYaml(self):
    try:
      super().loadYaml()
      data = self.getYamlPath(self.yamlPath1)
      if data is None: 
        self.msg("loadYaml: not finding anticipated data here: " + str(self.yamlPath1))
        return False
      return True
    except: self.err("loadYaml"); return False

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
