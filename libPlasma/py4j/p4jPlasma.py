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
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

    if self.verbose: 
      self.logger = logging.getLogger("py4j")
      selflogger.setLevel(logging.DEBUG)
      self.logger.addHandler(logging.StreamHandler())

    if self.hostAddress is not None: self.startGateway()

  ################# err, msg ################# 

  def err(self, msg): print("p4jPlasma error:", msg)
  def msg(self, msg): print("p4jPlasma message:", msg)

  ################# start gateway ################# 

  def startGateway(self):

    try:
      self.gwparam = GatewayParameters(address=self.hostAddress, port=25333)

      self.gateway = JavaGateway(gateway_parameters=self.gwparam)
      self.remoteClass = self.gateway.entry_point
    except Exception as e: self.err("p4jPlasma:", e); return None

  ################# get plasma address from Java side ################# 

  def getPlasmaAddress(self):

    try: pa = self.remoteClass.getPlasmaAddress()
    except Exception as e: err("getPlasmaAddress:", e); return None
    return pa

  ################# deposit a string, string pair ################# 

  def pDeposit_StrStr(self, a, b):
    try: self.remoteClass.pDeposit_StrStr(a,b)
    except Exception as e: err("pDeposit_StrStr:", e); return False
    return True

  ################# pawait ################# 

  def pAwait(self);
    try:   result = self.remoteClass.pAwait()
    except Exception as e: err("pDeposit_StrStr:", e); return None
    return result

### end ###
