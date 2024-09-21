// Py4j Plasma Java support
// Brygg Ullmer, Clemson University
// Begun 2024-09-20

// Generalizing from test/TestClass01.java

import py4j.Gateway;
import py4j.GatewayServer;
import py4j.CallbackClient;

import java.net.InetAddress;
import java.net.UnknownHostException;

import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.TimeUnit;
import java.util.logging.*;

import com.oblong.jelly.Slaw;
import com.oblong.jelly.Protein;
import com.oblong.jelly.Hose;
import com.oblong.jelly.Pool;
import com.oblong.jelly.PoolException;

//////////////////////////////////////////////////////////////
//////////////////// Py4j Plasma ~wrapper ////////////////////

public class P4jPlasma {
  protected String         p4jServerIpAddressStr;
  protected InetAddress    p4jServerIpAddress;
  protected GatewayServer  p4jGwServer;
  protected CallbackClient p4jCbClient;

  protected Logger  logger; 
  protected boolean verbose = true;
  protected Map<String, PlasmaHose> plasmaHoseMap;

  //////////////////// constructor ////////////////////

  public P4jPlasma(String p4jServerIpAddressStr) {
    this.p4jServerIpAddressStr = p4jServerIpAddressStr;

    initP4j();
  }
  //////////////////// error, message wrappers ////////////////////

  public void err(String msg) {System.out.println("P4jPlasma error: " + msg);}
  public void msg(String msg) {System.out.println("P4jPlasma msg: " + msg);}

  //////////////////// create plasma hose ////////////////////

  public PlasmaHose createPlasmaHose(String hoseName, String plasmaAddress) {
    PlasmaHose ph = new PlasmaHose(hoseName, plasmaAddress);
    Gateway gw = p4jGwServer.getGateway(); ph.setGateway(gw);
    plasmaHoseMap.put(hoseName, ph);
    return ph;
  }

  //////////////////// get plasma hose ////////////////////
  
  public PlasmaHose getPlasmaHose(String hoseName) {
    if (!plasmaHoseMap.containsKey(hoseName)) {
      err("getPlasmaHose does not contain hose name " + hoseName); return null;
    }

    PlasmaHose result = plasmaHoseMap.get(hoseName);
    return result;
  }

  //////////////////// initiate py4j gateway server ////////////////////

  public boolean initP4j() {

    try {
      if (verbose) {
        logger = Logger.getLogger("py4j");
        logger.setLevel(Level.ALL);
      }
  
      p4jServerIpAddress = InetAddress.getByName(this.p4jServerIpAddressStr);
      p4jCbClient        = new CallbackClient(GatewayServer.DEFAULT_PYTHON_PORT,
        InetAddress.getByName(CallbackClient.DEFAULT_ADDRESS), 2, TimeUnit.SECONDS);
  
      p4jGwServer = new GatewayServer(this, 25333, this.p4jServerIpAddress, 
         GatewayServer.DEFAULT_CONNECT_TIMEOUT, GatewayServer.DEFAULT_READ_TIMEOUT, 
         null, p4jCbClient);
  
      if (verbose) { p4jGwServer.turnLoggingOn(); }
  
      p4jGwServer.start();
      return true; // successfully started

    } catch (Exception e) {err("initP4j exception: "); e.printStackTrace(System.out); System.exit(-1);}
    return false;  
  }
}

/// end ///
