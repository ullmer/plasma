# Py4J Plasma wrappers
# Brygg Ullmer, Clemson University
# Begun 2024-09-20

# Code evolution from test/test_class_wrapper01b.py

# test_class_wrapper.py
import sys
import logging

from py4j.java_gateway import JavaGateway, GatewayParameters 

class p4jPlasma:
  verbose = False
  logger  = None

  hostAddress = None
  gwparam     = None
  gateway     = None
  remoteClass = None

  ################# constructor ################# 

  def __init__(self, **kwargs):
    self.msgCallbackDict  = {}

    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

    if self.verbose: 
      self.logger = logging.getLogger("py4j")
      selflogger.setLevel(logging.DEBUG)
      self.logger.addHandler(logging.StreamHandler())

    if hostAddress is not None: self.startGateway()

  ################# err, msg ################# 

  def err(self, msg): print("p4jPlasma error:", msg)
  def msg(self, msg): print("p4jPlasma message:", msg)

  ################# start gateway ################# 

  def startGateway(self):

    try:
      self.gwparam = GatewayParameters(address=self.hostAddress, port=25333)

      self.gateway = JavaGateway(gateway_parameters=self.gwparam)
    except Exception as e: self.err("p4jPlasma:", e); return None

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
