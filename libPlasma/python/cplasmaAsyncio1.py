#https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor

import asyncio
import concurrent.futures

import sys; sys.path.append("/home/ullmer/git/plasma/libPlasma/python/")
import cplasma

def plasma_io():
  strs = cplasma.pAwaitNextTrio()
  print("<<" + str(strs) + ">>")

cplasma.init("tcp://localhost/hello")

async def main():
  loop = asyncio.get_running_loop()

  with concurrent.futures.ThreadPoolExecutor() as pool:
    result = await loop.run_in_executor(pool, plasma_io)

while True:
  asyncio.run(main())

### end ###
