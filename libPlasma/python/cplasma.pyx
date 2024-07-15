# distutils: include_dirs = /home/ullmer/git/plasma/ /home/ullmer/git/plasma/libPlasma/c /home/ullmer/git/plasma/libLoam/c
import cython 

cdef extern from "slaw.h":
  ctypedef slaw

#cdef extern from "pool_cmd.h":
#  ctypedef pool_cmd_info

cdef extern from "cplasmaWrap.h":
  slaw plasmaInit()
  #cdef extern char *poolnameDefault
  #slaw plasmaInit(char *poolnameStr)

#def plasmaInit2(str poolnameStr):

def plasmaInit2():
  #cdef bytes poolnameBytes   = poolnameStr.encode("utf-8")
  #cdef char* poolnameCharstr = poolnameBytes #apparently auto-conversion
  #cdef pool_cmd_info  result = plasmaInit(poolnameCharstr)
  #cdef int result = plasmaInit(poolnameDefault)
  cdef int result = plasmaInit()
  return result

### end ###
