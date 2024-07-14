# distutils: include_dirs = /home/bullmer/git/plasma/ /home/bullmer/git/plasma/libPlasma/c

cdef extern from "slaw.h":
  ctypedef slaw

cdef extern from "pool_cmd.h":
  ctypedef pool_cmd_info

cdef extern from "cplasmaWrap.h":
  cdef slaw                extract_slaw (char *arg)
  cdef pool_cmd_info       plasmaInit   (char *pnstr)
  cdef int                 plasmaDeposit(pool_cmd_info cmd, char *descripStr, char ingestStr)

### end ###
