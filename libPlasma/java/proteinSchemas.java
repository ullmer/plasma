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
  List<String>        sensorTypesEngaged          = null;
  //ProteinDancer                           pDancer = null;

  ///////////// error reporting /////////////

  //to allow for later non-stdout error redirection
  public void err(msg)       {System.err.println("ProteinSchemas error: %s", msg); }
  public void msgUpdate(msg) {System.out.println("ProteinSchemas message update: %s", msg);}

  ///////////// constructor /////////////

  public ProteinSchemas() {
    synthHwSensorDepositorCache = new HashMap<>();
    sensorTypeId2Name           = new HashMap<>();
    sensorTypeName2Id           = new HashMap<>();
    sensorTypesEngaged          = new ArrayList<>();
 
    loadIndices()
    //self.loadMetaindices()

  ///////////// load indices /////////////

  public boolean loadIndices() {
    if (schemaIndexPath == null or indexFn == null) {
      err("loadIndices: schemaIndexPath or indexFn is empty! Returning"); return false;
    }

    String fullPath(schemaIndexPath + "/" + indexFn);
    File   fullPathF(fullPath);

    if (fullPathF.exists() == false) err("loadIndices: indices path doesn't exist! : %s", fullPath);

    indexYamlD = loadYamlFn(fullPath, 'configs');

    if (indexYamlD == null || indexYamlD.containsKey('addressSpace') == false) {
      err("loadIndices: configs (configurations) not found in %s", fullPath); return false;
    }

    Map<String, String> pcas = pconfigs.get('addressSpace''); //protein configs address space
							     
    hardwareYamlD = loadPCASYaml(pcas, 'hardware');
    softwareYamlD = loadPCASYaml(pcas, 'software');

    sensorYamlD = retrieveYamlSubset(hardwareYamlD, {"plasma", "hw", "sensors"});
  }

  /////////// retrieve yaml subset /////////// 
  //
  public Map<String,Object> retrieveYamlSubset(Map<String,Object> m, String[] keys) {
    Map<String,Object> drillDownHandle = m;

    for (int i=0; i<keylist.len; i++) {
      String key = keys[i];
      if (key != null and drillDownHandle.containsKey(key)) {
        drillDownHandle = drillDownHandle.get(key);
      } else { err("retrieveYamlSubset error" + keys + str(i)); return null; }
    }

    return drillDownHandle;
  }

  ///////////// load PCAS Yaml /////////////
  public Map<String, Object> loadPCASYaml(Map<String, String> pcas, String resourceHandle) {
    if (pcas == null || pcas.containsKey(resourceHandle) == false) {
      err("loadPCASYaml: YAML specification not in %s", resourceHandle); return false;
    }

    yamlFn = pcas.get(resourceHandle);
    Map<String, Object> result = loadYamlFn(yamlFn, resourceHandle);
    return result;
  
  }
  ///////////// load load yaml fn /////////////

  public Map<String, Object> loadYamlFn(String yamlFn, String resourceHandle) {

    try {
      String fullPath = schemaIndexPath + "/" + yamlFn;
      File   fullPathF(fullPath);
      if (fullPathF.exists() == false) {
        err("loadYamlFn: full yaml path doesn't exist! : %s", fullPath);
      }

      InputStream inputStream = new FileInputStream(fullPath);
      Yaml iy                 = new Yaml();
      result                  = iy.load(inputStream);
    } catch (IOException e) {err("loadYamlFn: error opening and/or loading %s", fullPath); e.printStackTrace(); }

    try { if (inputStream!= null) inputStream.close()
    } catch (IOException e)       err("loadYamlFn: Failed to close yaml filehandle");

    if (result == null) {err("loadYamlFn " + yamlFn + resourceHandle + "returns null!");}

    return result;
  }

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

    if (verbose) {System.out.println("active sensor fields:");}

    for (String sensorTypeId : sensorTypesEngaged) printSensorArgs(sensorTypeId);
  }

  ///////////// print sensor args /////////////

  public void printSensorArgs(int sensorTypeId) { 
    if (sensorTypeId2Name == null) {err("printSensorArgs: sensorTypeId2Name is null!"); return;}
    if (sensorTypeId2Name.containsKey(sensorTypeId)) {
      String sensorTypeName = sensorTypeId2Name(sensorTypeId);
      printSensorArgs(sensorTypeName);
    }
  }

  public void printSensorArgs(String sensorTypeName) { 
    if (sensorTypeName == null)     {err("printSensorArgs: sensorTypeId is empty!"); return;}
    if (sensorTypesEngaged == null) {err("printSensorArgs: sensorTypesEngaged is empty!"); return;}

    if (sensorTypesEngaged.containsKey(sensorTypeName) == false)} {
	 err("printSensorArgs: " + sensorTypeName + " not currently engaged!"); return;}

    Map<String, Object> hwDescr = getHwSensorDescr(sensorTypeName);

    try {
      if (hwDescr.containsKey('fields') == false) {
	 err("printSensorArgs: " + sensorTypeName + " does not contain apropos fields!"); return;}
         List<String> =  hwDescr.get('fields');

         String resultStr = String.format("Sensor %s : fields %s (%s)\n", sensorTypeName, String(fields), String(hwDescr));
         msgUpdate(resultStr);
    } catch (Exception e) {err("printSensorArgs: unknown error"); e.printStackTrace(); return;}
  }

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

