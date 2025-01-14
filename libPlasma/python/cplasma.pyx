# Cython .pyx wrapper around wrapped cplasma functions
# Brygg Ullmer, Clemson University
# Begun 2024-07-14

import  cython 
from libc.string cimport strcpy, strlen
#from libc.stdint cimport uint16_t
#cimport numpy as np
#import numpy as np

cdef extern from "cplasmaWrap.h":
  void   plasmaInit(char *poolnameStr)
  void   plasmaClose() 
  int    plasmaDeposit_StrStr(char *descripStr, char *ingestStr)
  int    plasmaDeposit_Unt16_Unt16Arr(int descripInt, int *ingestIntArr, int arraySize)
  int    plasmaAwait()
  char **plasmaAwaitNextTrio()
  char **plasmaPoolNext(char *formatStr)
  char  *plasmaGetProtFormatStr(char *formatName)
  char  *plasmaGetProtFormatNames()
  #int    plasmaDeposit_Unt16_Unt16Arr(stdint.unt16_t descripInt, stdint.unt16_t *ingestIntArr, int arraySize)

############### plasma init wrapper ###############

def init(str poolnameStr):
  cdef bytes poolnameBytes   = poolnameStr.encode("utf-8")
  cdef char* poolnameCharstr = poolnameBytes #apparently auto-conversion
  plasmaInit(poolnameCharstr)

############### plasma close wrapper ###############

def close():
  plasmaClose() 

############### plasma deposit wrapper ###############

def pDeposit_StrStr(str descripStr, str ingestStr):
  cdef bytes descripStrBytes = descripStr.encode("utf-8")
  cdef bytes ingestStrBytes  = ingestStr.encode("utf-8")

  cdef char* descripCharstr = descripStrBytes #apparently auto-conversion
  cdef char* ingestCharstr  = ingestStrBytes  #apparently auto-conversion

  plasmaDeposit_StrStr(descripCharstr, ingestCharstr)
  
############### plasma deposit wrapper ###############

# to avoid both numpy dependencies and complexities, and cython array + type introspection,
# tentatively exploring an approach involving a series of different Cython bindings specific
# to the number of integers being passed

# I view this as inelegant, and a temporary bootstrapping approach.
# That said, it appears plausible to address a large fraction of the early use examples
# I'm personally targeting, and I cannot easily further defer these until realizing
# some early working progress --BAU

#https://docs.cython.org/en/latest/src/userguide/memoryviews.html
#`arr` is a one-dimensional numpy array
#if not arr.flags['C_CONTIGUOUS']: #per memoryviews docs.cython example
#  arr = np.ascontiguousarray(arr)
#cdef int[::1] arr_memview = arr

############### Plasma Deposit: d: Unt16; i: unt16 array (length 1) ############### 

def pDeposit_Unt16_Unt16A1(int descripInt, int ingestInt):
  plasmaDeposit_Unt16_Unt16Arr(descripInt, &ingestInt, 1)

  #cdef uint16_t descripInt2 = descripInt1
  #cdef uint16_t ingestInt   = ingestInt;

############### Plasma Deposit: d: Unt16; i: unt16 array (length 2) ############### 

def pDeposit_Unt16_Unt16A2(int descripInt, int ingestInt1, int ingestInt2):
  cdef int ingestInts[2]
  ingestInts[0] = ingestInt1
  ingestInts[1] = ingestInt2

  plasmaDeposit_Unt16_Unt16Arr(descripInt, ingestInts, 2)
#  cdef .uint16_t descripInt2 = descripInt1
#  cdef uint16_t ingestInts[2];

############### Plasma Deposit: d: Unt16; i: unt16 array (length 3) ############### 

def pDeposit_Unt16_Unt16A3(int descripInt, int ingestInt1, int ingestInt2, int ingestInt3):
  cdef int ingestInts[3];

  ingestInts[0] = ingestInt1
  ingestInts[1] = ingestInt2
  ingestInts[2] = ingestInt3

  plasmaDeposit_Unt16_Unt16Arr(descripInt, ingestInts, 3)

############### Plasma Deposit: d: Unt16; i: unt16 array (length 4) ############### 

def pDeposit_Unt16_Unt16A4(int descripInt, int ingestInt1, int ingestInt2, int ingestInt3, int ingestInt4):
  cdef int ingestInts[4];

  ingestInts[0] = ingestInt1
  ingestInts[1] = ingestInt2
  ingestInts[2] = ingestInt3
  ingestInts[3] = ingestInt4

  plasmaDeposit_Unt16_Unt16Arr(descripInt, ingestInts, 4)

############### plasma await wrapper ###############

def pAwait():
  plasmaAwait()

############### plasma await wrapper ###############

def pAwaitNextTrio():
  cdef char** nch = plasmaAwaitNextTrio()
  str1 = nch[0].decode("UTF-8")
  str2 = nch[1].decode("UTF-8")
  str3 = nch[2].decode("UTF-8")
  result = [str1, str2, str3]
  return result

############### plasma pool_next wrapper ###############

def pNext(str formatStr):
  cdef bytes formatStrBytes = formatStr.encode("utf-8")
  cdef char* formatCharstr  = formatStrBytes #apparently auto-conversion

  cdef char **nch = plasmaPoolNext(formatCharstr)

  if nch is NULL: 
    return None

  str1 = nch[0].decode("UTF-8")
  str2 = nch[1].decode("UTF-8")
  str3 = nch[2].decode("UTF-8")
  result = [str1, str2, str3]
  return result

############### get plasma protein format string ###############

def getProtFormatStr(str formatName):
  cdef bytes formatNameBytes = formatName.encode("utf-8")
  cdef char *formatNameChars = formatNameBytes #apparently auto-conversion

  cdef char *resultC = plasmaGetProtFormatStr(formatNameChars)
  result   = resultC.decode("UTF-8")
  return result
  
############### get plasma protein format names ###############

def getProtFormatNames():
  cdef char *nameChr = plasmaGetProtFormatNames()
  result = [nameChr.decode("UTF-8")] #hardwired :-)
  return result

### end ###
