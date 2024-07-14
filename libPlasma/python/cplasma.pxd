# Adaptation by Brygg Ullmer, Clemson University
# reduction to cython wrapper, initially re JShrake helloWorld example from Animist discord #plasma 

cdef extern from "cplasma.h":
  ctypedef slaw
  ctypedef pool_cmd_info
  slaw                extract_slaw (char *arg)
  pool_cmd_info       plasmaInit   (char *pnstr)
  int                 plasmaDeposit(pool_cmd_info cmd, char *descripStr, char ingestStr)
  
 #ctypedef void* slaw           
 #ctypedef void* pool_cmd_info  

### end ###
