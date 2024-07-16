#https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor
#https://pymotw.com/3/asyncio/executors.html

import asyncio
import concurrent.futures

import sys; sys.path.append("/home/ullmer/git/plasma/libPlasma/python/")
import cplasma

from concurrent.futures import ThreadPoolExecutor

def plasmaAwait():
  strs = cplasma.pAwaitNextTrio()
  print("<<" + str(strs) + ">>")

async def runPlasma(executor):
  loop = asyncio.get_running_loop()
  await loop.run_in_executor(executor, plasmaAwait)
  #await asyncio.Future()

cplasma.init("tcp://localhost/hello")
eloop = asyncio.get_event_loop()

executor = ThreadPoolExecutor(max_workers=1)

asyncio.ensure_future(runPlasma(executor))

try:
  eloop.run_forever()
finally:
  eloop.close()

### end ###
