// Adaptation by Brygg Ullmer, Clemson University
// reduction to cython wrapper, initially re JShrake helloWorld example from Animist discord #plasma 

cdef extern from "cplasma-cython.h":

  static slaw    extract_slaw (char *arg)
  pool_cmd_info  plasmaInit(char *pnstr)
  int            plasmaDeposit(pool_cmd_info cmd, char *descripStr, char ingestStr)

/// end ///
