import sys; sys.path.append("/home/ullmer/git/plasma/libPlasma/python/")
import cplasma
import asyncio

cplasma.init("tcp://localhost/hello")

def awaitPlasmaTrio()
  strs = cplasma.pAwaitNextTrio()
  return strs

async def plasma_client():
  strs = await cplasma.pAwaitNextTrio()
  print("<<%s>>" % strs)

asyncio.run(plasma_client())

### end ###

