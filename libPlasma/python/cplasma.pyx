print("cython cplasma import underway")

from cplasma cimport plasmaInit, plasmaDeposit

cdef extern pool_cmd_info  plasmaInit   (char *pnstr)
cdef extern int            plasmaDeposit(pool_cmd_info cmd, char *descripStr, char ingestStr)

print("cython cplasma import complete ")

#cimport cplasma

#cdef slaw           extract_slaw (char *arg)

#def __cinit__(self):
#  self._c_queue = cqueue.queue_new()

from cplasma cimport plasmaDeposit
### end ###
