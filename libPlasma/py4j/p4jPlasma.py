# Py4J Plasma wrappers
# Brygg Ullmer, Clemson University
# Begun 2024-09-20

# Code evolution from test/test_class_wrapper01b.py

# test_class_wrapper.py
import sys
import logging

from py4j.java_gateway import JavaGateway, GatewayParameters 

class P4jPlasma:
  verbose = False
  logger  = None

  hostAddress = None

  gateway     = None
  remoteClass = None
     

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
