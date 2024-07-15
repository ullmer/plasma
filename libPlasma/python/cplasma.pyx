# Cython .pyx wrapper around wrapped cplasma functions
# Brygg Ullmer, Clemson University
# Begun 2024-07-14

import cython 
from libc.string cimport strcpy, strlen

#cdef extern from "slaw.h":
#  ctypedef slaw

#cdef extern from "pool_cmd.h":
#  ctypedef pool_cmd_info

cdef extern from "cplasmaWrap.h":
  void plasmaInit(char *poolnameStr)

  #cdef extern char *poolnameDefault
  #slaw plasmaInit(char *poolnameStr)

def init(str poolnameStr):

  cdef bytes poolnameBytes   = poolnameStr.encode("utf-8")
  cdef char* poolnameCharstr = poolnameBytes #apparently auto-conversion
  plasmaInit(poolnameCharstr)

### end ###
