# Image-labeled objects warm-up example
# Brygg Ullmer, Clemson University
# Begun 2025-07-09

class ADImgLabeledObj(AtaDomain):
  yamlPath = '~/git/plasma/apps/demo/atabrowser.01/yaml'
  yamlFn   = 'us_nps/sc.yaml'

  def __init__(self): self.loadYaml()

  ########## loadYaml ##########

  def loadYaml(self):
    if self.yamlPath is None or self.yamlFn is None:
      self.msg("
    fn = self.yamlPath + self.yamlFn
    

#Initial key directories
#./domains/imgLabeledObjs.01
#./images/us_nps/meta
#./yaml/us_nps

### end ###
