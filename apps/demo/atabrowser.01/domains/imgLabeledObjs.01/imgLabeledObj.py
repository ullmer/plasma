# Image-labeled objects warm-up example
# Brygg Ullmer, Clemson University
# Begun 2025-07-09

import os, yaml
from ataDomain import *

class ADImgLabeledObj(AtaDomain):
  yamlFn   = 'us_nps/sc.yaml'

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
