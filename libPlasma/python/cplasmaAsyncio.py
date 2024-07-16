#https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor

import asyncio
import concurrent.futures

import sys; sys.path.append("/home/ullmer/git/plasma/libPlasma/python/")
import cplasma

def blocking_io():
  # File operations (such as logging) can block the
  # event loop: run them in a thread pool.
  strs = cplasma.pAwaitNextTrio()
  print("<<" + str(strs) + ">>")

cplasma.init("tcp://localhost/hello")

async def main():
  loop = asyncio.get_running_loop()

  ## Options:
  # 2. Run in a custom thread pool:
  with concurrent.futures.ThreadPoolExecutor() as pool:
    result = await loop.run_in_executor(pool, blocking_io)

  # 3. Run in a custom process pool:
  #with concurrent.futures.ProcessPoolExecutor() as pool:
  #  result = await loop.run_in_executor(
  #    pool, blocking_io)
  #  print('custom process pool', result)

while True:
  asyncio.run(main())

#asyncio.run_forever(main())

#with asyncio.Runner() as runner:
#  runner.run(main())

#loop = asyncio.get_event_loop()
#loop = asyncio.get_running_loop()

#try:
#  asyncio.ensure_future(main())
#  loop.run_forever()
#except KeyboardInterrupt:
#  pass
#finally:
#  print("Closing Loop")
#  loop.close()
### end ###
