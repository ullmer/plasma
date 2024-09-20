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
  classWrapper    = None

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

    except Exception as e: self.err("init catch:", str(e)); return None

    self.classWrapper = self.gateway.entry_point
    self.classWrapper.init(poolStr)

  ################# error, message handlers #################

  def err(self, msg): print("p4jPlasma error:", str(msg)) 
  def msg(self, msg): print("p4jPlasma msg:",   str(msg)) 

  ################# pdeposit str str #################

  def pDeposit_StrStr(self, str1, str2):
    if self.classWrapper is Null:
      self.err("pDeposit_StrStr called, but Java proxy not yet initiated"); return None

    try:
      self.classWrapper.pDeposit_StrStr(str1, str2)
    except Exception as e: self.err("pDeposit_StrStr catch:" + str(e)); return None

  ################# pnext fmtStr #################

  def pNext(self, formatStr):
    if self.classWrapper is Null:
      self.err("pNext called, but Java proxy not yet initiated"); return None

    try:
      self.classWrapper.pNext(str1, str2)
    except Exception as e: print("pNext:", e); sys.exit(-1)

### end #
