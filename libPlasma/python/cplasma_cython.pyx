# Adaptation by Brygg Ullmer, Clemson University
# reduction to cython wrapper, initially re JShrake helloWorld example from Animist discord #plasma 

cimport cplasma_cython:

  static slaw    extract_slaw (char *arg)
  pool_cmd_info  plasmaInit(char *pnstr)
  int            plasmaDeposit(pool_cmd_info cmd, char *descripStr, char ingestStr)


  cdef class Queue:
  cdef cqueue.Queue* _c_queue

  def __cinit__(self):
    self._c_queue = cqueue.queue_new()

/// end ///
