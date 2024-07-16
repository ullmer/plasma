import sys; sys.path.append("/home/ullmer/git/plasma/libPlasma/python/")
import cplasma
import asyncio, sys, time

cplasma.init("tcp://localhost/hello")
time.sleep(4)
#fmtStr        = cplasma.getProtFormatStr('prot:simpleKeyVal')
fmtStr = "{D:[S],I:{S: S}}"

print("watching cplasma for updates of form", fmtStr)
sleepDuration = .01

async def plasmaWatcher():
  global sleepDuration, fmtStr

  try:    strs = cplasma.pNext(fmtStr)
  except: print("plasmaWatcher: pNext error!"); return

  if strs is None: await asyncio.sleep(sleepDuration)
  else: print("<<%s>>" % strs)

#asyncio.run(plasmaWatcher())

cplasma.close()

### end ###

