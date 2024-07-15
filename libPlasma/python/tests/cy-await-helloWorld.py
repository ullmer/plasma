import sys; sys.path.append("/home/ullmer/git/plasma/libPlasma/python/")
import cplasma

cplasma.init("tcp://localhost/hello")
cplasma.pAwait()

