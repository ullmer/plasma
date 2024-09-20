# Py4J Plasma wrapper
# Brygg Ullmer, Clemson University
# Begun 2024-09-19

import sys; sys.path.append("/home/bullmer/git/plasma/libPlasma/python/")
import sys
import logging

from py4j.java_gateway import JavaGateway, GatewayParameters 

class p4jPlasma:

  def init(self, poolStr):

  def pDeposit_StrStr(self, str1, str2):

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
