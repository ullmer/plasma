
import asyncio
import plasma
import logging
import nest_asyncio

nest_asyncio.apply()

class AsyncPlasmaListener:
    def __init__(self, pool_name="tcp://localhost/hello"):
        self.pool_name = pool_name
        self.hose = None
        self.running = False

        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    async def _listen(self):
        self.hose = plasma.Pool.Participate(self.pool_name)
        if self.hose is None:
            self.logger.error(f"Failed to connect to pool: {self.pool_name}")
            return

        self.logger.info("Connected to pool, listening for messages...")

        while self.running:
            print(1)
            protein = self.hose.Next(-1)
            print(2)
            if protein.IsNull():
                self.logger.error("Received null protein")
                break
            print(3)
            self.handle_message(protein)
            print(4)

    def handle_message(self, protein):
        d, i = protein.Descrips(), protein.Ingests()
        print("d ->", d.ToString())
        print("i ->", i.ToString())

    async def start(self):
        self.running = True
        await self._listen()

    async def stop(self):
        self.running = False
        if self.hose:
            self.hose.Withdraw()

# Test harness
async def main_async():
    listener = AsyncPlasmaListener(pool_name="tcp://localhost/hello")
    await listener.start()

if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.get_event_loop().run_until_complete(main_async())
