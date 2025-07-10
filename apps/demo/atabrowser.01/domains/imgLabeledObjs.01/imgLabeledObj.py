# Image-labeled objects warm-up example
# Brygg Ullmer, Clemson University
# Begun 2025-07-09

import os, yaml
from ataDomain import *
from yamlRc    import *

class ADImgLabeledObj(AtaDomain):
  yamlFnSC   = 'us_nps/sc.yaml'
  yamlFnNPS  = 'us_nps/usNpsParks07.yaml'

  yamlSCrc  = None
  yamlNPSrc = None

  yamlSCPath1 = 'sc:nps:meta'

  imgLabeledMetad = None

  ########## loadYaml ##########
  def loadYaml(self):
    try:
      ys = self.yamlSCrc  = YamlRc(self.yamlFnSC)
      yn = self.yamlNPSrc = YamlRc(self.yamlFnNPS)

      ilmd = self.imgLabeledMetad = ys.getYamlPath(self.yamlSCPath1)
      if ilmd is None: 
        self.msg("loadYaml: not finding anticipated data here: " + str(self.yamlSCPath1))
        return False
      self.msg("loadYaml d: " + str(ilmd))

      return True
    except: self.err("loadYaml"); return False

########## main ##########
if __name__ == "__main__":
  adilo = ADImgLabeledObj()
  adilo.loadYaml()

#Initial key directories
#./domains/imgLabeledObjs.01
#./images/us_nps/meta
#./yaml/us_nps

### end ###
