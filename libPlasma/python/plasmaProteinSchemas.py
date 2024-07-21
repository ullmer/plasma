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
import cplasma 

#############################################################
###################### plasma protein schemas ###############

class plasmaProteinSchemas:
  schemaIndexPath = None
  indexFn         = 'index.yaml'
  indexYamlD      = None 
  hardwareYamlFn  = None
  hardwareYamlD   = None
  sensorYamlD     = None
  synthHwSensorDepositorCache = None
  sensorTypeId2Name  = None
  sensorTypeName2Id  = None
  sensorTypesEngaged = None
  pDancer            = None

  ############# error reporting #############

  #to allow for later non-stdout error redirection
  def err(self, msg):       print("CPlasma error:", msg)          
  def msgUpdate(self, msg): print("CPlasma message update:", msg) 

  ############# constructor #############

  def __init__(self, **kwargs):
    self.msgCallbackDict  = {}

    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

    self.synthHwSensorDepositorCache = {}
    self.sensorTypeId2Name           = {}
    self.sensorTypesEngaged          = []
 
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
    if hwDescr is None:      self.err("getHwSensorTransportDescr: no information received for sensor type " + hwEl); return

    if 'fmt' not in hwDescr: self.err("getHwSensorTransportDescr: no format (fmt) information found for sensor " + hwEl); return

    fmt = hwDescr['fmt']

    if '*' in fmt: #array
     protType, arrCnt = fmt.split('*')
     return [protType, arrCnt]

    return fmt

  ############# print active sensor fields #############
  def printActiveSensorFields(self):
    if len(self.sensorTypesEngaged) == 0: self.err("printActiveSensorFields: no sensor types engaged"); return

    print("active sensor fields:")

    for sensorTypeId in self.sensorTypesEngaged:
      self.printSensorArgs(sensorTypeId)

  ############# sensor depostor #############

  def printSensorArgs(self, sensorTypeId): #accepts either integer ID or string ID
    if sensorTypeId == None: self.err("printSensorArgs: sensorTypeId is None"); return

    if isinstance(sensorTypeId, int) and sensorTypeId in self.sensorTypeId2Name: hwEl = self.sensorTypeId2Name[sensorTypeId]
    else: hwEl = sensorTypeId

    if hwEl not in self.sensorTypesEngaged: self.err("printSensorArgs: sensor type not found engaged: ", str(hwEl)); return

    hwDescr = self.getHwSensorDescr(hwEl)
    try:
      fields  = hwDescr['fields']
      resultStr = "Sensor %s : fields %s (%s)\n" % (hwEl, str(fields), str(hwDescr))
      print(resultStr)
    except: self.err("printSensorArgs: unknown error"); traceback.print_exc(); return

  ############# sensor depostor #############

  def sensorDepositor(self, sensorTypeId, numFields, fieldArgs):
    if len(fieldArgs) != numFields:
      self.err("sensorDepositor: number of arguments in list does not match expectations")
      self.printSensorArgs(sensorTypeId); return

    # alas, "case" not present until fairly recent Python versions
    if numFields==1: cplasma.pDeposit_Unt16_Unt16A1(descrIntSafe, fieldArgs[0])
    if numFields==2: cplasma.pDeposit_Unt16_Unt16A2(descrIntSafe, fieldArgs[0], fieldArgs[1])
    if numFields==3: cplasma.pDeposit_Unt16_Unt16A3(descrIntSafe, fieldArgs[0], fieldArgs[1], fieldArgs[2])
    if numFields==4: cplasma.pDeposit_Unt16_Unt16A3(descrIntSafe, fieldArgs[0], fieldArgs[1], fieldArgs[2], fieldArgs[3])

  ############# register hw sensor depositor #############

  #def synthHwSensorDepositor(self, hwEl):
  def registerHwSensorDepositor(self, hwEl):
    if hwEl in self.synthHwSensorDepositorCache: return self.synthHwSensorDepositorCache[hwEl]

    hwDescr            = self.getHwSensorDescr(hwEl)
    if hwDescr is None:  self.err("synthHwSensorDepositor: no information received for sensor type " + hwEl); return
    hwTransportDescr =   self.getHwSensorTransportDescr(hwEl)

    if 'fields' not in hwDescr:
      self.err("registerHwSensorDepositor: 'fields' not in: "+ str(hwDescr)); return

    numFields    = len(hwDescr['fields'])
    if len(hwTransportDescr) == 1: lenTransport = 1 #heuristic, may not be correct
    else:                          lenTransport = hwTransportDescr[1] #also a heuristic, toward bootstrapping :-)

    if numFields != lenTransport:
      self.err("synthHwSensorDepositor: number of sensor fields different from inferred transport length. punting;" + str(hwDescr)); return

    if 'bv' not in hwDescr: self.err("synthHwSensorDepositor: sensor ID class not found in hw descr"); return
    sensorTypeId = hwDescr['bv'] #binary value; probably should be renamed
    self.sensorTypeId2Name[sensorTypeId] = hwEl
    self.sensorTypeName2Id[hwEl]         = sensorTypeId
    self.sensorTypesEngaged.append(hwEl)

    depositorFunc = partial(self.sensorDepositor, sensorTypeId, numFields)
    self.synthHwSensorDepositorCache[hwEl] = depositorFunc
    return depositorFunc

#C2d_generic : ['unt16', '3']
#NFC_125k01 : ['unt16', '3']
#NFC_13m01 : ['unt16', '4']
#IMU_ST01 : ['unt16', '2']
#C2d_generic : {'bv': 38401, 'nm': 'multitouch', 'fmt': 'unt16*3', 'layout': 'AB CC DD', 'fields': ['device', 'touch', 'x', 'y']}
#NFC_125k01 : {'bv': 39425, 'nm': 'HiTag2', 'fmt': 'unt16*3', 'layout': 'AA AA AA', 'fields': ['serial']}
#NFC_13m01 : {'bv': 39441, 'nm': 'NTAG213', 'fmt': 'unt16*4', 'layout': 'AA AA AA A0', 'fields': ['serial']}
#IMU_ST01 : {'bv': 40705, 'nm': 'ST LSM6DS3TR_C IMU Ac Gy', 'fmt': 'unt16*2', 'layout': 'AA BB', 'fields': ['Ac', 'Gy']}

###################### main ######################

if __name__ == '__main__':
  pps = plasmaProteinSchemas(schemaIndexPath='/home/bullmer/git/plasma/libPlasma/yaml')
  print(pps.hardwareYamlD)

### end ###

