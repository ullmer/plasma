# Cython .pyx wrapper around wrapped cplasma functions
# Brygg Ullmer, Clemson University
# Begun 2024-07-14

import cython 
from libc.string cimport strcpy, strlen

cdef extern from "cplasmaWrap.h":
  void   plasmaInit(char *poolnameStr)
  int    plasmaDeposit(char *descripStr, char *ingestStr)
  int    plasmaAwait()
  char **plasmaAwaitNextTrio()
  char **plasmaPoolNext(char *formatStr)
  char  *plasmaGetProtFmtStr(char *formatName)

############### plasma init wrapper ###############

def init(str poolnameStr):
  cdef bytes poolnameBytes   = poolnameStr.encode("utf-8")
  cdef char* poolnameCharstr = poolnameBytes #apparently auto-conversion
  plasmaInit(poolnameCharstr)

############### plasma deposit wrapper ###############

def pDeposit(str descripStr, str ingestStr):
  cdef bytes descripStrBytes = descripStr.encode("utf-8")
  cdef bytes ingestStrBytes  = ingestStr.encode("utf-8")

  cdef char* descripCharstr = descripStrBytes #apparently auto-conversion
  cdef char* ingestCharstr  = ingestStrBytes  #apparently auto-conversion

  plasmaDeposit(descripCharstr, ingestCharstr)

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
  str1 = nch[0].decode("UTF-8")
  str2 = nch[1].decode("UTF-8")
  str3 = nch[2].decode("UTF-8")
  result = [str1, str2, str3]
  return result

############### plasma pool_next wrapper ###############

def getProtFmtStr(str formatName):
  cdef bytes formatNameBytes = formatName.encode("utf-8")
  cdef char *formatNameChars = formatNameBytes #apparently auto-conversion

  cdef char *resultC = plasmaGetProtFmtStr(formatNameChars)
  result   = resultC.decode("UTF-8")

### end ###
