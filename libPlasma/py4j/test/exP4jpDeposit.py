# Initial code commit generated by CoPilot on 2024-09-16, in response to query:
# "please provide example python and java code using py4j.  The java file should include a
#   class testClass with integer variables A and B.  The python file should provide a wrapper
#   that accesses these testClass variables."

# Code evolution by Brygg Ullmer, Clemson University

# test_class_wrapper.py
import sys
import logging

from py4j.java_gateway import JavaGateway, GatewayParameters 

#logger = logging.getLogger("py4j")
#logger.setLevel(logging.DEBUG)
#logger.addHandler(logging.StreamHandler())

gwparam = GatewayParameters(address='172.25.49.14', port=25333)
#gwparam = GatewayParameters(address='127.0.0.1', port=25333)
#gwparam = GatewayParameters(address='130.127.48.81', port=25333)

# Connect to the Java Gateway
try:
  gateway = JavaGateway(gateway_parameters=gwparam)
except Exception as e: print("error:", e); sys.exit(-1)

pj4p = gateway.entry_point # Access the TestClass instance

try:                       # Get the values the plasma address 
  pa = pj4p.getPlasmaAddress()
except Exception as e: print("error:", e); sys.exit(-1)

print(f"Plasma address: {pa}")

try:                       # Get the values the plasma address 
  pj4p.pDeposit_StrStr("hello", "world")
  #pj4p.pClose()
except Exception as e: print("error:", e); sys.exit(-1)

print("ends")

### end ###
