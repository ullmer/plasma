// Adaptation by Brygg Ullmer, Clemson University
// reduction to cython wrapper, initially re JShrake helloWorld example from Animist discord #plasma 

/// Deposit a protein into a pool.


cdef extern from "cplasma-cython.h":

  static slaw        extract_slaw (char *arg); //helper function for plasmaDeposit, copied from p-deposit.c
  pool_cmd_info      plasmaInit(char *pnstr = "tcp://localhost/hello");
  int                plasmaDeposit(pool_cmd_info cmd, char *dstr  = "hello", char *istr  = "name:world");

/// end ///
