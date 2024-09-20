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

public class P4jPlasma {
    private String  defaultP4jServerIpAddress="172.25.49.14");

    private String  p4jServerIpAddress;
    private String  plasmaAddress;

    private boolean verbose =true;

    public P4jPlasma(String p4jServerIpAddress, String plasmaAddress) {
        this.p4jServerIpAddress = p4jServerIpAddress;
        this.plasmaAddress      = plasmaAddress;
    }

    public static void main(String[] args) {

        try {
          P4jPlasma p4jp = new P4jPlasma();

          if (this.verbose) {
            Logger logger = Logger.getLogger("py4j");
            logger.setLevel(Level.ALL);
          }

          //GatewayServer server = new GatewayServer(testClass, 25333);
          //InetAddress address = InetAddress.getByName("130.127.48.81");
          InetAddress address = InetAddress.getByName("172.25.49.14");

          //GatewayServer server = new GatewayServer(testClass);

          CallbackClient cbClient = new CallbackClient(GatewayServer.DEFAULT_PYTHON_PORT,
             InetAddress.getByName(CallbackClient.DEFAULT_ADDRESS), 2, TimeUnit.SECONDS);

          GatewayServer server = new GatewayServer(testClass, 25333, address, 
            GatewayServer.DEFAULT_CONNECT_TIMEOUT, GatewayServer.DEFAULT_READ_TIMEOUT, 
            null, cbClient);

          //server.turnLoggingOn();

          server.start();
          System.out.println("Gateway Server Started");
	} catch (UnknownHostException e) {e.printStackTrace();}
    }
}

/// end ///
