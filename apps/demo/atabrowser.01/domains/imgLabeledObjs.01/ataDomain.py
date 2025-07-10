# Animist Tangible Allomorphs Domain
# Brygg Ullmer, Clemson University
# Begun 2025-07-09

import os, traceback, yaml
from ataBase import *

# Presently rather minimal; may call for later refactoring

########## animist tangible allomorphs domain ##########

class AtaDomain(AtaBase):
  yamlPath = '~/git/plasma/apps/demo/atabrowser.01/yaml/'
  verbose  = True

########## main ##########
if __name__ == "__main__":
  ad = AtaDomain()
  ad.msg("hello world")

### end ###
