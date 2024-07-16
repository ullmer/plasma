import sys; sys.path.append("/home/ullmer/git/plasma/libPlasma/python/")
import cplasma
import asyncio

cplasma.init("tcp://localhost/hello")
fmtStr        = cplasma.getProtFormatStr('prot:simpleKeyVal')
print("watching cplasma for updates of form", fmtStr)
sleepDuration = .01

async def plasmaWatcher():
  global sleepDuration
  strs = cplasma.pNext(fmtStr)

  if strs is None: await asyncio.sleep(sleepDuration)
  else: print("<<%s>>" % strs)

asyncio.run(plasmaWatcher())

### end ###

