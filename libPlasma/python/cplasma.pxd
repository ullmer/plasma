cdef extern from "cplasma.h":
  ctypedef slaw
  ctypedef pool_cmd_info
  slaw                extract_slaw (char *arg)
  pool_cmd_info       plasmaInit   (char *pnstr)
  int                 plasmaDeposit(pool_cmd_info cmd, char *descripStr, char ingestStr)
  
 #ctypedef void* slaw           
 #ctypedef void* pool_cmd_info  

### end ###
