// Py4j Plasma Java support
// Brygg Ullmer, Clemson University
// Begun 2024-09-20

// Generalizing from test/TextClass01.java


import py4j.GatewayServer;
import py4j.CallbackClient;

import java.net.InetAddress;
import java.net.UnknownHostException;

import java.util.concurrent.TimeUnit;

import java.util.logging.*;

//////////////////////////////////////////////////////////////
//////////////////// Py4j Plasma ~wrapper ////////////////////

public class P4jPlasma {
  protected String         plasmaAddressStr;
  protected String         p4jServerIpAddressStr;

  protected InetAddress    p4jServerIpAddress;
  protected GatewayServer  p4jGwServer;

  protected CallbackClient p4jCbClient;

  protected boolean verbose = true;
  protected Logger  logger;

  //////////////////// constructor ////////////////////

  public P4jPlasma(String p4jServerIpAddressStr, String plasmaAddressStr) {
    this.p4jServerIpAddressStr = p4jServerIpAddressStr;
    this.plasmaAddressStr      = plasmaAddressStr;

    this.initP4j();
    this.initPlasma();
  }

  //////////////////// constructor ////////////////////

  public initP4j() {

    if (this.verbose) {
      this.logger = Logger.getLogger("py4j");
      this.logger.setLevel(Level.ALL);
    }

    this.p4jServerIpAddress = InetAddress.getByName(this.p4jIpAddressStr);
    this.p4jCbClient        = new CallbackClient(GatewayServer.DEFAULT_PYTHON_PORT,
      InetAddress.getByName(CallbackClient.DEFAULT_ADDRESS), 2, TimeUnit.SECONDS);

    this.p4jGwServer = new GatewayServer(testClass, 25333, this.p4jServerIpAddress, 
       GatewayServer.DEFAULT_CONNECT_TIMEOUT, GatewayServer.DEFAULT_READ_TIMEOUT, 
       null, this.p4jCbClient);

    if (this.verbose) { this.p4jServer.turnLoggingOn(); }

    this.p4jGwServer.start();
  }

  //////////////////// main ////////////////////

  public static void main(String[] args) {

    try {
      P4jPlasma p4jp = new P4jPlasma();
      System.out.println("Gateway Server Started");
    } catch (UnknownHostException e) {e.printStackTrace();}
  }
}

/// end ///
