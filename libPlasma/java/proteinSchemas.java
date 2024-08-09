// Plasma Protein Schemas (mapping of protocols, initially oriented
//  toward software, sensors, and multitouch, but also with an eye toward
//  other hardware and software services)
//
// Lead by Brygg Ullmer, Clemson University
// Python variant begun 2024-07-20
// Java port begun 2024-08-09

import org.yaml.snakeyaml.reader;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStream;
import java.io.File;

import java.util.Map;

/////////////////////////////////////////////////////////////
////////////////////// plasma protein schemas ///////////////

public class ProteinSchemas {
  String schemaIndexPath = null;
  String indexFn         = "index.yaml";
  String hardwareYamlFn  = null;
  String softwareYamlFn  = null;

  Boolean verbose        = true;

  Map<String, Object> indexYamlD, hardwareYamlD, sensorYamlD, swYamlD;
  Map<Int, String>    sensorTypeId2Name  = null;
  Map<String, Int>    sensorTypeName2Id  = null;

  Map<String, Object> synthHwSensorDepositorCache = null;
  Map<String, boolean> sensorTypesEngaged         = null;
  ProteinDancer      pDancer = null;

  ///////////// error reporting /////////////

  //to allow for later non-stdout error redirection
  public void err(msg)       {System.err.println("ProteinSchemas error: %s", msg); }
  publiv void msgUpdate(msg) {System.out.println("ProteinSchemas message update: %s", msg);}

  ///////////// constructor /////////////

  public ProteinSchemas() {
    self.synthHwSensorDepositorCache = {}
    self.sensorTypeId2Name           = {}
    self.sensorTypeName2Id           = {}
    self.sensorTypesEngaged          = []
 
    self.loadIndices()
    //self.loadMetaindices()

  ///////////// load indices /////////////

  public boolean loadIndices() {
    if (schemaIndexPath == null or indexFn == null) {
      err("loadIndices: schemaIndexPath or indexFn is empty! Returning"); return false;
    }

    String fullPath(schemaIndexPath + "/" + indexFn);
    File   fullPathF(fullPath);

    if (fullPathF.exists() == false) {
      err("loadIndices: indices path doesn't exist! : %s", fullPath);
    }

    try {
      fullPath.open();
      InputStream inputStream = new FileInputStream(fullPath);
      Yaml iy                 = new Yaml();
      indexYamlD              = iy.load(inputStream);

      if (verbose) System.out.println(indexYamlD);

    } catch (FileNotFoundException e) { 
      err("loadIndices: error on opening and/or loading %s", fullPath); 
      e.printStackTrace(); 
      return false;
    }

    if (indexYamlD.containsKey('configs') == false) {
      err("loadIndices: configs (configurations) not found in %s", fullPath); return false;
    }

    Map<String, Object> pconfigs = indexYamlD.get('configs'); //protein configs

    if (pconfigs == null || pconfigs.containsKey('addressSpace') == false) {
      err("loadIndices: configs (configurations) not found in %s", fullPath); return false;
    }

    Map<String, String> pcas = pconfigs.get('addressSpace''); //protein configs address space
							      //
    if (pcas == null || pcas.containsKey('hardware') == false) {
      err("loadIndices: hardware YAML specification not in %s", fullPath); return false;
    }

    hardwareYamlFn = pcas.get('hardware');

    try {
      fullHwPath = self.schemaIndexPath + "/" + self.hardwareYamlFn 
      yf = open(fullHwPath)
      self.hardwareYamlD  = yaml.safe_load(yf)
      yf.close()
    except:
      self.err("loadIndices: error on opening and/or loading " + fullHwPath);
      traceback.print_exc(); return

    /////////// Load hardware yaml info /////////// 

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

  ///////////// get hw sensor descr /////////////

  def getHwSensorDescr(self, hwName):
    if self.sensorYamlD is None: self.err("getHwSensorDescr: no sensor data detected"); return

    if 'contact' in self.sensorYamlD: /search contact-based sensors
      sc = self.sensorYamlD['contact']
      if hwName in sc: return sc[hwName]

    if 'noncontact' in self.sensorYamlD:
      snc = self.sensorYamlD['noncontact']
      if hwName in snc: return snc[hwName]

    self.err("getHwSensorDescr: sensor type " + hwName + " not found in registered contact or non-contact sensor types!")
    return None

  ///////////// get hw sensor transport descr /////////////

  def getHwSensorTransportDescr(self, hwEl):
    hwDescr = self.getHwSensorDescr(hwEl)
    if hwDescr is None:      self.err("getHwSensorTransportDescr: no information received for sensor type " + hwEl); return

    if 'fmt' not in hwDescr: self.err("getHwSensorTransportDescr: no format (fmt) information found for sensor " + hwEl); return

    fmt = hwDescr['fmt']

    if '*' in fmt: /array
     protType, arrCnt = fmt.split('*')
     return [protType, int(arrCnt)]

    return fmt

  ///////////// print active sensor fields /////////////
  def printActiveSensorFields(self):
    if len(self.sensorTypesEngaged) == 0: self.err("printActiveSensorFields: no sensor types engaged"); return

    print("active sensor fields:")

    for sensorTypeId in self.sensorTypesEngaged:
      self.printSensorArgs(sensorTypeId)

  ///////////// sensor depostor /////////////

  def printSensorArgs(self, sensorTypeId): /accepts either integer ID or string ID
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

  ///////////// sensor depostor /////////////

  def sensorDepositor(self, sensorTypeId, numFields, fieldArgs):
    if len(fieldArgs) != numFields:
      self.err("sensorDepositor: number of arguments in list does not match expectations")
      self.printSensorArgs(sensorTypeId); return

    // alas, "case" not present until fairly recent Python versions
    if numFields==1: cplasma.pDeposit_Unt16_Unt16A1(sensorTypeId, fieldArgs[0])
    if numFields==2: cplasma.pDeposit_Unt16_Unt16A2(sensorTypeId, fieldArgs[0], fieldArgs[1])
    if numFields==3: cplasma.pDeposit_Unt16_Unt16A3(sensorTypeId, fieldArgs[0], fieldArgs[1], fieldArgs[2])
    if numFields==4: cplasma.pDeposit_Unt16_Unt16A4(sensorTypeId, fieldArgs[0], fieldArgs[1], fieldArgs[2], fieldArgs[3])

  ///////////// register hw sensor depositor /////////////

  //def synthHwSensorDepositor(self, hwEl):
  def registerHwSensorDepositor(self, hwEl):
    if hwEl in self.synthHwSensorDepositorCache: return self.synthHwSensorDepositorCache[hwEl]

    hwDescr            = self.getHwSensorDescr(hwEl)
    if hwDescr is None:  self.err("synthHwSensorDepositor: no information received for sensor type " + hwEl); return
    hwTransportDescr =   self.getHwSensorTransportDescr(hwEl)

    if 'fields' not in hwDescr:
      self.err("registerHwSensorDepositor: 'fields' not in: "+ str(hwDescr)); return

    numFields    = len(hwDescr['fields'])
    if len(hwTransportDescr) == 1: lenTransport = 1 /heuristic, may not be correct
    else:                          lenTransport = hwTransportDescr[1] /also a heuristic, toward bootstrapping :-)

    if numFields != lenTransport:
      self.err("synthHwSensorDepositor: number of sensor fields different from inferred transport length. punting;")
      self.err("%i : %i; %s" % (numFields, lenTransport, str(hwDescr))); return

    if 'bv' not in hwDescr: self.err("synthHwSensorDepositor: sensor ID class not found in hw descr"); return
    sensorTypeId = hwDescr['bv'] /binary value; probably should be renamed
    self.sensorTypeId2Name[sensorTypeId] = hwEl
    self.sensorTypeName2Id[hwEl]         = sensorTypeId
    self.sensorTypesEngaged.append(hwEl)

    depositorFunc = partial(self.sensorDepositor, sensorTypeId, numFields)
    self.synthHwSensorDepositorCache[hwEl] = depositorFunc
    return depositorFunc

//C2d_generic: ['unt16', '3']
//NFC_125k01:  ['unt16', '3']
//NFC_13m01:   ['unt16', '4']
//IMU_ST01:    ['unt16', '2']
//C2d_generic: {'bv': 38401, 'nm': 'multitouch', 'fmt': 'unt16*3', 'layout': 'AB CC DD', 'fields': ['device', 'touch', 'x', 'y']}
//NFC_125k01:  {'bv': 39425, 'nm': 'HiTag2', 'fmt': 'unt16*3', 'layout': 'AA AA AA', 'fields': ['serial']}
//NFC_13m01:   {'bv': 39441, 'nm': 'NTAG213', 'fmt': 'unt16*4', 'layout': 'AA AA AA A0', 'fields': ['serial']}
//IMU_ST01:    {'bv': 40705, 'nm': 'ST LSM6DS3TR_C IMU Ac Gy', 'fmt': 'unt16*2', 'layout': 'AA BB', 'fields': ['Ac', 'Gy']}

////////////////////// main //////////////////////

  public static void main(String[] args) {
    try {
      InputStream inputStream = new FileInputStream("config.yaml");
      Yaml yaml = new Yaml();
      Map<String, Object> data = yaml.load(inputStream);
      System.out.println(data);
     } catch (FileNotFoundException e) { e.printStackTrace(); }

    ps = ProteinSchemas(schemaIndexPath='/home/ullmer/git/plasma/libPlasma/yaml')
    print(ps.hardwareYamlD)
  }
}

/// end ///

