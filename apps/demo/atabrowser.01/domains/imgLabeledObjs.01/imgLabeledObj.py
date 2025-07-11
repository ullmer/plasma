# Image-labeled objects warm-up example
# Brygg Ullmer, Clemson University
# Begun 2025-07-09

import os, yaml
from ataDomain import *
from yamlRc    import *

class ADImgLabeledObj(AtaDomain):
  yamlFnSC   = 'us_nps/sc.yaml'
  yamlFnNPS  = 'us_nps/usNpsParks08.yaml'

  yamlSCrc  = None
  yamlNPSrc = None

  objDetailsDict   = None
  objDetailsPrefix = 'parkDetails:'
  yamlSCPath1      = 'sc:nps:meta'

  imgLabeledMetad = None

  ########## loadYaml ##########
  def loadYaml(self):
    try:
      ys = self.yamlSCrc  = YamlRc(self.yamlFnSC);  ys.loadYaml()
      yn = self.yamlNPSrc = YamlRc(self.yamlFnNPS); yn.loadYaml()

      ilmd = self.imgLabeledMetad = ys.getYamlPath(self.yamlSCPath1)
      if ilmd is None: 
        self.msg("loadYaml: not finding anticipated data here: " + str(self.yamlSCPath1))
        return False
      self.msg("loadYaml d: " + str(ilmd))

      if 'fn' not in ilmd:
        self.msg("initPgz: filename not present in metadata where expected"); return False

      self.objDetailsDict = {}
      ofns = self.objFns  = ilmd['fn']
      for ofn1 in ofns: 
        # in warmup, postfixed with 2 (relating to pixel density); strip that
        ofn2 = ofn1[:-1]
        self.msg(ofn2)

        yp = self.objDetailsPrefix + ofn2
        od = yn.getYamlPath(yp)
        if od is None: self.msg("loadYaml: obj details not found for path " + str(yp); continue
        self.objDetailsDict[ofn2] = od

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
