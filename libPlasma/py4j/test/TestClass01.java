// Code generated by CoPilot on 2024-09-16, in response to query:
// "please provide example python and java code using py4j.  The java file should include a 
//   class testClass with integer variables A and B.  The python file should provide a wrapper 
//   that accesses these testClass variables."

// TestClass.java
import py4j.GatewayServer;
import java.net.InetAddress;
import java.net.UnknownHostException;

public class TestClass01 {
    private int A;
    private int B;

    public TestClass01(int A, int B) {
        this.A = A;
        this.B = B;
    }

    public int getA() {
        return A;
    }

    public void setA(int A) {
        this.A = A;
    }

    public int getB() {
        return B;
    }

    public void setB(int B) {
        this.B = B;
    }

    public static void main(String[] args) {
        try {
          TestClass01 testClass = new TestClass01(10, 20);

          InetAddress address = InetAddress.getByName("172.25.49.14");
          GatewayServer server = new GatewayServer(testClass, 25333);
          //GatewayServer server = new GatewayServer(testClass);
	  //server.setAddress(address);
          //GatewayServer server = new GatewayServer(testClass, 25333, address, 
          // GatewayServer.DEFAULT_CONNECT_TIMEOUT, GatewayServer.DEFAULT_READ_TIMEOUT, null);

          server.start();
          System.out.println("Gateway Server Started");
	} catch (UnknownHostException e) {e.printStackTrace();}
    }
}

/// end ///
