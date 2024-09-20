# Cython bindings around libPlasma/c
# Lead by Brygg Ullmer, Clemson University
# Begun 2024-07-13

import sys; sys.path.append("/home/ullmer/git/plasma/libPlasma/python/")
import cplasma
import asyncio, sys, time, traceback

from   functools      import partial # for callback support
from   cplasmaWatcher import *

#############################################################
###################### cplasma dancer ######################

# builds on the monitoring functionalities of CPlasmaWatcher to add emissive capabilities

class CPlasmaDancer(CPlasmaWatcher):
  poolSpecifier   = "tcp://localhost/hello" #default, will benefit from evolution
  msgFormatName   = "prot:simpleKeyVal"
  msgFormatStr    = None
  msgCallbackDict = None
  sleepDuration   = .01
  safeInvocation  = True # slows things slightly, but checks + converts type

  ############# error reporting #############

  #to allow for later non-stdout error redirection
  def err(self, msg):       print("CPlasmaDancer error:", msg)          
  def msgUpdate(self, msg): print("CPlasmaDancer message update:", msg) 

  ############# constructor #############
  def __init__(self, **kwargs):
    self.msgCallbackDict  = {}

    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

    if self.poolSpecifier is None: self.err("constructor: poolSpecifier not provided"); return -1
    self.initPlasma(self.poolSpecifier)
  
  ############# deposit d:str i:str #############
  def pDepositStr_Str(self, str1, str2): cplasma.pDeposit_StrStr(str1, str2) #nothing interesting yet, but will evolve

  ############# deposit d:unt i:unt array #############
  def pDepositUnt16_Unt16A(self, descrInt, ingestsArray):

    #first, replicate array as integers, catching exceptions, in case floats, etc. slipped in
    if self.safeInvocation:
      iiArray = []
      try:
        for el in ingestsArray: iiArray.append((int) el)
      except:
        self.err("pDepositUnt16_Unt16: a payload element couldn't be converted to integer:" + str(ingestsArray)
        return None
    else: iiArray = ingestsArray #no type checking or conversion; faster, but riskier

    descrIntSafe = (int) descrInt
    ilen = len(iiArray)

    # alas, "case" not present until fairly recent Python versions
    if ilen==1: cplasma.pDeposit_Unt16_Unt16A1(descrIntSafe, iiArray[0])
    if ilen==2: cplasma.pDeposit_Unt16_Unt16A2(descrIntSafe, iiArray[0], iiArray[1])
    if ilen==3: cplasma.pDeposit_Unt16_Unt16A3(descrIntSafe, iiArray[0], iiArray[1], iiArray[2])
    if ilen==4: cplasma.pDeposit_Unt16_Unt16A3(descrIntSafe, iiArray[0], iiArray[1], iiArray[2], iiArray[3])

### end ###

