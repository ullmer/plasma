#https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor

import asyncio
import concurrent.futures

def blocking_io():
  # File operations (such as logging) can block the
  # event loop: run them in a thread pool.
  with open('/dev/urandom', 'rb') as f:
    return f.read(100)

async def main():
  loop = asyncio.get_running_loop()

  ## Options:
  # 2. Run in a custom thread pool:
  with concurrent.futures.ThreadPoolExecutor() as pool:
    result = await loop.run_in_executor(
      pool, blocking_io)
    print('custom thread pool', result)

  # 3. Run in a custom process pool:
  #with concurrent.futures.ProcessPoolExecutor() as pool:
  #  result = await loop.run_in_executor(
  #    pool, cpu_bound)
  #  print('custom process pool', result)

if __name__ == '__main__':
  asyncio.run(main())

### end ###
