cdef extern from "slaw.h":
  ctypedef slaw
  ctypedef pool_cmd_info

cdef extern from "cplasma.h":
  cpdef slaw                extract_slaw (char *arg)
  cpdef pool_cmd_info       plasmaInit   (char *pnstr)
  cpdef int                 plasmaDeposit(pool_cmd_info cmd, char *descripStr, char ingestStr)

 #ctypedef void* slaw           
 #ctypedef void* pool_cmd_info  

### end ###
