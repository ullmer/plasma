import plasma
import asyncio
import time
import logging

class AsyncPlasmaListener:
    def __init__(self, pool_name="tcp://localhost/hello"):
        self.pool_name = pool_name
        self.hose = None
        self.message_queue = asyncio.Queue()
        self.running = False

        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    async def _listen(self):
        self.hose = plasma.Pool.Participate(self.pool_name)
        if self.hose is None:
            self.logger.error(f"Failed to connect to pool: {self.pool_name}")
            return

        self.logger.info("Connected to pool, listening for messages...")

        try:
            while self.running:
                print(1)
                protein = self.hose.Next(-1)
                print(2)
                if protein.IsNull():
                    self.logger.error("Received null protein")
                    break
                print(3)
                await self.message_queue.put(protein)
                print(4)
        finally:
            self.hose.Withdraw()

    async def start(self):
        self.running = True
        asyncio.create_task(self._listen())
        self.logger.info("AsyncPlasmaListener started")

    async def stop(self):
        self.running = False

    async def get_message(self):
        print(5)
        result = await self.message_queue.get()
        print(6)
        return result

# Test harness for asyncio version
async def main_async():
    listener = AsyncPlasmaListener(pool_name="tcp://localhost/hello")
    await listener.start()
    await asyncio.sleep(0.5)

    try:
        while True:
            print("A")
            message = await listener.get_message()
            print("B")
            if message:
                try:
                    d, i = message.Descrips(), message.Ingests()
                    print("d ->", d.ToString())
                    print("i ->", i.ToString())
                except Exception as e:
                    print("Error processing message:", e)
            await asyncio.sleep(0.1)
    except KeyboardInterrupt:
        await listener.stop()

if __name__ == "__main__":
    asyncio.run(main_async())
