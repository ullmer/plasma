import sys; sys.path.append("/home/ullmer/git/plasma/libPlasma/python/")
import cplasma

cplasma.init("tcp://localhost/hello")
while True:
  str = cplasma.pAwaitNextStr()
  print("<<%s>>" % str)

### end ###

