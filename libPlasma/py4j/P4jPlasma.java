// Py4j Plasma Java support
// Brygg Ullmer, Clemson University
// Begun 2024-09-20

// Generalizing from test/TestClass01.java

import py4j.GatewayServer;
import py4j.CallbackClient;

import java.net.InetAddress;
import java.net.UnknownHostException;

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
  protected String         plasmaAddressStr;
  protected String         p4jServerIpAddressStr;

  protected InetAddress    p4jServerIpAddress;
  protected GatewayServer  p4jGwServer;

  protected CallbackClient p4jCbClient;

  protected Hose           pHose;

  protected boolean verbose = true;
  protected Logger  logger;

  //////////////////// getters ////////////////////

  public String getPlasmaAddress() {return this.plasmaAddress;}

  //////////////////// constructor ////////////////////

  public P4jPlasma(String p4jServerIpAddressStr, String plasmaAddressStr) {
    this.p4jServerIpAddressStr = p4jServerIpAddressStr;
    this.plasmaAddressStr      = plasmaAddressStr;

    this.initP4j();
    this.initPlasma();
  }

  //////////////////// error, message wrappers ////////////////////

  public void err(String msg) {System.out.println("P4jPlasma error: " + msg);}
  public void msg(String msg) {System.out.println("P4jPlasma msg: " + msg);}

  //////////////////// initiate py4j gateway server ////////////////////

  public boolean initP4j() {

    try {
      if (this.verbose) {
        this.logger = Logger.getLogger("py4j");
        this.logger.setLevel(Level.ALL);
      }
  
      this.p4jServerIpAddress = InetAddress.getByName(this.p4jServerIpAddressStr);
      this.p4jCbClient        = new CallbackClient(GatewayServer.DEFAULT_PYTHON_PORT,
        InetAddress.getByName(CallbackClient.DEFAULT_ADDRESS), 2, TimeUnit.SECONDS);
  
      this.p4jGwServer = new GatewayServer(this, 25333, this.p4jServerIpAddress, 
         GatewayServer.DEFAULT_CONNECT_TIMEOUT, GatewayServer.DEFAULT_READ_TIMEOUT, 
         null, this.p4jCbClient);
  
      if (this.verbose) { this.p4jGwServer.turnLoggingOn(); }
  
      this.p4jGwServer.start();
      return true; // successfully started

    } catch (Exception e) {this.err("initP4j exception: " + e.getMessage());}
    return false;  
  }

  //////////////////// initiate plasma ////////////////////

  public boolean initPlasma() {
    try {
      this.pHose = Pool.participate(this.plasmaAddressStr);
    } catch (Exception e) {this.err("initPlasma exception: " + e.getMessage());}
    if (this.verbose) {this.msg("Plasma initiated");}
  }

  //////////////////// main ////////////////////

  public static void main(String[] args) {

    //String p4jIpAddressStr = "172.25.49.14";
    String p4jIpAddressStr = "130.127.48.81";
    String plasmaAddress   = "tcp://localhost/hello";

    try {
      P4jPlasma p4jp = new P4jPlasma(p4jIpAddressStr, plasmaAddress);
      System.out.println("Gateway Server Started");
    } catch (Exception e) {System.out.println("main exception:" + e.getMessage());}
  }
}

/// end ///
