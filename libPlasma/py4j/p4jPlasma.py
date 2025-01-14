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

  hostAddress   = None
  plasmaAddress = None
  gwparam       = None
  gateway       = None
  remoteClass   = None

  ################# constructor ################# 

  def __init__(self, **kwargs):
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

    if self.verbose: 
      self.logger = logging.getLogger("py4j")
      self.logger.setLevel(logging.DEBUG)
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
    except Exception as e: self.err("p4jPlasma:", e.getMessage()); return None

  ################# create plasma hose ################# 

  def pCreateHose(self, hoseName, plasmaAddress):

    try: ph = self.remoteClass.pCreateHose(hoseName, plasmaAddress);
    except Exception as e: self.err("pCreateHose:" + str(e)); return None
    return ph

  ################# get hose side ################# 

  def pGetHose(self, hoseName):

    try: ph = self.remoteClass.pGetHose(hoseName);
    except Exception as e: self.err("pCreateHose:" + str(e)); return None
    return ph

  ################# get plasma address from Java side ################# 

  def getPlasmaAddress(self, hoseName):

    try: pa = self.remoteClass.getPlasmaAddress(hoseName)
    except Exception as e: self.err("getPlasmaAddress:" + str(e)); return None
    return pa

  ################# deposit a string, string pair ################# 

  def pDeposit_StrStr(self, hoseName, a, b):
    try: self.remoteClass.pDeposit_StrStr(hoseName, a,b)
    except Exception as e: self.err("pDeposit_StrStr:" + str(e)); return False
    return True

  ################# pawait ################# 

  def pNext(self, hoseName):
    try:   result = self.remoteClass.pNext(hoseName)
    except Exception as e: self.err("pDeposit_StrStr:" + str(e)); return None
    return result

  ################# pawait ################# 

  def pAwaitNext(self, hoseName):
    try:   result = self.remoteClass.pAwaitNext(hoseName)
    except Exception as e: self.err("pDeposit_StrStr:" + str(e)); return None
    return result

### end ###
