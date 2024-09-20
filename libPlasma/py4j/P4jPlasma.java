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

public class TestClass01 {
    private int A;
    private int B;

    public TestClass01(int A, int B) {
        this.A = A;
        this.B = B;
    }

    public int  getA()      { return A; }
    public int  getB()      { return B; }

    public void setA(int A) { this.A = A; }
    public void setB(int B) { this.B = B; }

    public static void main(String[] args) {
        try {
          TestClass01 testClass = new TestClass01(10, 20);

          Logger logger = Logger.getLogger("py4j");
          logger.setLevel(Level.ALL);

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
