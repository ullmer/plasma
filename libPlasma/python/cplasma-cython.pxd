// Adaptation by Brygg Ullmer, Clemson University
// reduction to cython wrapper, initially re JShrake helloWorld example from Animist discord #plasma 

/// Deposit a protein into a pool.


cdef extern from "cplasma-cython.h":

  static slaw        extract_slaw (char *arg); //helper function for plasmaDeposit, copied from p-deposit.c
  plasmaInit(char *pnstr = "tcp://localhost/hello");
  cmdDescripsIngests plasmaDeposit(pool_cmd_info cmd, char *dstr  = "hello", char *istr  = "name:world");

/// end ///
