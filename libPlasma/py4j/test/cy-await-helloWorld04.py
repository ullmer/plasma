import sys; sys.path.append("/home/ullmer/git/plasma/libPlasma/python/")
import cplasma
import asyncio, sys, time

cplasma.init("tcp://localhost/hello")
fmtStr        = cplasma.getProtFormatStr('prot:simpleKeyVal')
sleepDuration = .01

async def plasmaWatcher():
  global sleepDuration, fmtStr

  while True:
    try:    strs = cplasma.pNext(fmtStr)
    except: print("plasmaWatcher: pNext error!"); return

    if strs is None: await asyncio.sleep(sleepDuration)
    else: print("<<%s>>" % strs)

asyncio.run(plasmaWatcher())

cplasma.close()

### end ###

