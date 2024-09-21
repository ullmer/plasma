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

//////////////////// plasma hose ////////////////////

public class PlasmaHose {
  protected String  hoseName;
  protected String  plasmaAddressStr;
  protected Hose    pHose;
  protected Gateway gateway;
  protected boolean verbose = true;

  //////////////////// constructor ////////////////////

  public PlasmaHose(String hoseName, String plasmaAddressStr) {
    this.hoseName         = hoseName;
    this.plasmaAddressStr = plasmaAddressStr;

    initPlasma();
  }

  //////////////////// error, message wrappers ////////////////////

  public void err(String msg) {System.out.println("PlasmaHose error: " + msg);}
  public void msg(String msg) {System.out.println("PlasmaHose msg: " + msg);}

  //////////////////// setters ////////////////////

  public void    setGateway(Gateway gw) {this.gateway = gw;}
  public Gateway getGateway()           {return gateway;}

  //////////////////// getters ////////////////////

  public String getPlasmaAddress() {return plasmaAddressStr;}

  //////////////////// initiate plasma ////////////////////
  public boolean initPlasma() {
    try {
      pHose = Pool.participate(plasmaAddressStr);
      pHose.disengageThreadChecker(); //without this, multi-threaded Py4j & Plasma will complain
    } catch (Exception e) {err("initPlasma exception:"); e.printStackTrace(System.out); System.exit(-1);}

    if (verbose) {msg("Plasma initiated");}
    return true;
  }

  //////////////////// plasma deposit strstr ////////////////////

  public boolean pDeposit_StrStr(String descripStr, String ingestStr) {

    if (verbose) {msg("pDeposit_StrStr called; d: " + descripStr + "; i: " + ingestStr);}

    try {
      Slaw descrips = Slaw.list(Slaw.string(descripStr));
      Slaw ingests  = Slaw.list(Slaw.string(ingestStr));

      Protein p = Slaw.protein(descrips, ingests);
      pHose.deposit(p);

    } catch (PoolException e) {

      err("plasmaDeposit_StrStr pool exception:" + e.getMessage());
      e.printStackTrace(System.out);
      return false;
    }
    if (verbose) {msg("pDeposit_StrStr deposit complete");}

    return true;
  }

  //////////////////// plasma await next ////////////////////

  public Protein pNext() {
    if (verbose) {msg("pAwait called");}
    try {
      //Hashmap<String, Object> map = gateway.jvm.java.util.HashMap()

      Protein p = pHose.next();
      return p;
    } catch (Exception e) {err("pAwaitBlocking: " + e.getMessage());}

    return null;
  }

  //////////////////// plasma await next ////////////////////

  public Map<Slaw, Slaw> pAwaitNext() {
    if (verbose) {msg("pAwaitNext called");}
    try {
      //Hashmap<String, Object> map = gateway.jvm.java.util.HashMap()

      Protein p = pHose.awaitNext();
      Map<Slaw, Slaw> result = p.emitContainedMap();

      return result;
    } catch (Exception e) {err("pAwaitBlocking: " + e.getMessage());}

    return null;
  }

  //////////////////// plasma close ////////////////////

  public boolean pClose() {
    if (verbose) {msg("pClose begins");}
    try {
      pHose.withdraw();
    } catch (Exception e) {
      err("plasma close error: " + e.getMessage());
      return false;
    }
    if (verbose) {msg("pClose ends");}
    return true;
  }

  //////////////////// main ////////////////////

  public static void main(String[] args) {

    String p4jIpAddressStr = "172.25.49.14";
    //String p4jIpAddressStr = "130.127.48.81";
    String plasmaAddress   = "tcp://localhost/hello";

    try {
      P4jPlasma p4jp = new P4jPlasma(p4jIpAddressStr, plasmaAddress);
      System.out.println("Gateway Server Started");
    } catch (Exception e) {System.out.println("main exception:" + e.getMessage());}
  }
}

/// end ///
