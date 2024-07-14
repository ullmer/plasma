# distutils: include_dirs = /home/ullmer/git/plasma/ /home/ullmer/git/plasma/libPlasma/c
import cython 

cdef extern from "slaw.h":
  ctypedef slaw

cdef extern from "pool_cmd.h":
  ctypedef pool_cmd_info


cdef extern from "cplasmaWrap.h":
  cdef extern poolnameDefault
  slaw plasmaInit(char *poolnameStr)

def plasmaInit2(str poolnameStr):
  #cdef bytes poolnameBytes   = poolnameStr.encode("utf-8")
  #cdef char* poolnameCharstr = poolnameBytes #apparently auto-conversion
  #cdef pool_cmd_info  result = plasmaInit(poolnameCharstr)
  cdef pool_cmd_info  result = plasmaInit(poolnameDefault)
  return result

### end ###
