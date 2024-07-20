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
  
  ############# get hw yaml descr #############

  def getHwYamlDescr(self, hwName):
    if self.hardwareYamlD is None:
      self.err("getHwYamlDescr: hardwareYaml data is not yet populated"); return None

    if hwName not in self.hardwareYamlD:
      self.err("getHwYamlDescr: specified hardware " + hwName + " not found!"); return None

    result = self.hardwareYamlD[hwName]
    return result

###################### main ######################

if __name__ == '__main__':
  pps = plasmaProteinSchemas(schemaIndexPath='/home/bullmer/git/plasma/libPlasma/yaml')
  print(pps.hardwareYamlD)

### end ###

