# distutils: include_dirs = /home/bullmer/git/plasma/ /home/bullmer/git/plasma/libPlasma/c

cdef extern from "slaw.h":
  ctypedef slaw

cdef extern from "pool_cmd.h":
  ctypedef pool_cmd_info

cdef extern from "cplasmaWrap.h":
  cpdef slaw                extract_slaw (char *arg)
  cpdef pool_cmd_info       plasmaInit   (char *pnstr)
  cpdef int                 plasmaDeposit(pool_cmd_info cmd, char *descripStr, char ingestStr)

### end ###
