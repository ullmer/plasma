# Adaptation by Brygg Ullmer, Clemson University
# reduction to cython wrapper, initially re JShrake helloWorld example from Animist discord #plasma 

cdef extern from "cplasma_cython.h":

  ctypedef slaw           extract_slaw (char *arg)
  ctypedef pool_cmd_info  plasmaInit(char *pnstr)
  int                     plasmaDeposit(ctypedef pool_cmd_info cmd, char *descripStr, char ingestStr)

### end ###
