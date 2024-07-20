# Plasma Protein Schemas (mapping of protocols, initially oriented
#  toward sensors and multitouch, but also with an eye toward
#  other hardware and software services)
# Lead by Brygg Ullmer, Clemson University
# Begun 2024-07-20

#import os, sys, pathlib
#LIB_PATH = pathlib.Path(__file__).parents[1] #library in parent directory
#sys.path.append(os.path.join(LIB_PATH, ''))
#import sys; sys.path.append("/home/ullmer/git/plasma/libPlasma/python/")

import os, asyncio, sys, time, traceback, yaml
from   functools import partial # for callback support

#############################################################
###################### plasma protein schemas ###############

class plasmaProteinSchemas:
  schemaIndexPath = None
  indexFn         = 'index.yaml'
  indexYamlD      = None 
  hardwareYamlFn  = None
  hardwareYamlD   = None
  sensorYamlD     = None

  ############# error reporting #############

  #to allow for later non-stdout error redirection
  def err(self, msg):       print("CPlasma error:", msg)          
  def msgUpdate(self, msg): print("CPlasma message update:", msg) 

  ############# constructor #############

  def __init__(self, **kwargs):
    self.msgCallbackDict  = {}

    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
 
    self.loadIndices()
    #self.loadMetaindices()

  ############# load indices #############

  def loadIndices(self):
    if self.schemaIndexPath is None or self.indexFn is None:
      self.err("loadIndices: schemaIndexPath or indexFn is empty! Returning"); return

    fullPath = self.schemaIndexPath + "/" + self.indexFn
    if os.path.exists(fullPath) is False:
      self.err("loadIndices: indices path doesn't exist! : " + fullPath)

    try:
      yf = open(fullPath)
      self.indexYamlD = yaml.safe_load(yf) #index.yaml, primarily containing names of other YAML indices
      yf.close()
    except:
      self.err("loadIndices: error on opening and/or loading " + fullPath); 
      traceback.print_exc(); return

    if 'configs' not in self.indexYamlD:
      self.err("loadIndices: configs (configurations) not found in " + fullPath); return

    pconfigs = self.indexYamlD['configs']
    if 'addressSpace' not in pconfigs:
      self.err("loadIndices: addressSpace not in " + fullPath); return 

    pcas = pconfigs['addressSpace']
    if 'hardware' not in pcas:
      self.err("loadIndices: hardware YAML specification not in " + fullPath); return

    self.hardwareYamlFn = pcas['hardware']
    try:
      fullHwPath = self.schemaIndexPath + "/" + self.hardwareYamlFn 
      yf = open(fullHwPath)
      self.hardwareYamlD  = yaml.safe_load(yf)
      yf.close()
    except:
      self.err("loadIndices: error on opening and/or loading " + fullHwPath);
      traceback.print_exc(); return

    ########### Load hardware yaml info ########### 

    if self.hardwareYamlD is None:
      self.err("loadHwYamlDescr: hardwareYaml data is not yet populated"); return None

    if 'plasma' not in self.hardwareYamlD:
      self.err("loadHwYamlDescr: 'plasma' not in yaml descr!"); return None

    p = self.hardwareYamlD['plasma']

    if 'hw' not in p:
     self.err("loadHwYamlDescr: 'hw' not in yaml descr!"); return None

    phw = p['hw']

    if 'sensors' not in phw:
      self.err("loadHwYamlDescr: 'sensors' not in yaml descr!"); return None

    self.sensorYamlD = phw['sensors'] 

  ############# get hw sensor descr #############

  def getHwSensorDescr(self, hwName):
    if self.sensorYamlD is None: self.err("getHwSensorDescr: no sensor data detected"); return

    if 'contact' in self.sensorYamlD: #search contact-based sensors
      sc = self.sensorYamlD['contact']
      if hwName in sc: return sc[hwName]

    if 'noncontact' in self.sensorYamlD:
      snc = self.sensorYamlD['noncontact']
      if hwName in snc: return snc[hwName]

    self.err("getHwSensorDescr: sensor type " + hwName + " not found in registered contact or non-contact sensor types!")
    return None

  ############# get hw sensor transport descr #############
  def getHwSensorTransportDescr(self, hwEl):
    hwDescr = self.getHwSensorDescr(hwEl)
    if hwDescr is none:      self.err("getHwSensorTransportDescr: no information received for sensor type " + hwEl); return

    if 'fmt' not in hwDescr: self.err("getHwSensorTransportDescr: no format (fmt) information found for sensor " + hwEl); return


###################### main ######################

if __name__ == '__main__':
  pps = plasmaProteinSchemas(schemaIndexPath='/home/bullmer/git/plasma/libPlasma/yaml')
  print(pps.hardwareYamlD)

### end ###

