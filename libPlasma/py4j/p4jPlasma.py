# Py4J Plasma wrapper
# Brygg Ullmer, Clemson University
# Begun 2024-09-19

import sys; sys.path.append("/home/bullmer/git/plasma/libPlasma/python/")
import sys
import logging

from py4j.java_gateway import JavaGateway, GatewayParameters 
  
################# py4j plasma wrapper #################

class p4jPlasma:

  verbose = False
  logger  = None

  activateLogging = True
  gwServerAddress = '172.25.49.14'
  gwServerPort    = 25333
  gwParam         = None
  gateway         = None

  ################# constructor #################

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

    if self.activateLogging:
      self.logger = logging.getLogger("py4j")
      self.logger.setLevel(logging.DEBUG)
      self.logger.addHandler(logging.StreamHandler())

  ################# init #################

  def init(self, poolStr):
    self.gwParam = GatewayParameters(address=self.gwServerAddress, 
                                        port=self.gwServerPort)
    try: # Connect to the Java Gateway
      self.gateway = JavaGateway(gateway_parameters=gwparam)
    except Exception as e: print("error:", e); sys.exit(-1)

  ################# pdeposit str str #################

  def pDeposit_StrStr(self, str1, str2):



# Access the TestClass instance
test_class = gateway.entry_point

# Get the values of A and B
try:
  A = test_class.getA()
  B = test_class.getB()
except Exception as e: print("error:", e); sys.exit(-1)

print(f"Value of A: {A}")
print(f"Value of B: {B}")

# Set new values for A and B
test_class.setA(30)
test_class.setB(40)

# Get the updated values of A and B
A = test_class.getA()
B = test_class.getB()

print(f"Updated value of A: {A}")
print(f"Updated value of B: {B}")

### end ###
