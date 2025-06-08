
import threading
import plasma
import time
import logging

class PlasmaListenerCondition:
    def __init__(self, pool_name="tcp://localhost/hello"):
        self.pool_name = pool_name
        self.hose = None
        self.thread = None
        self.running = False
        self.message = None
        self.condition = threading.Condition()
        self.ready = threading.Event()

        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def _listen(self):
        self.hose = plasma.Pool.Participate(self.pool_name)
        if self.hose is None:
            self.logger.error(f"Failed to connect to pool: {self.pool_name}")
            return

        self.logger.info("Connected to pool, listening for messages...")
        self.ready.set()

        try:
            while self.running:
                print(1)
                protein = self.hose.Next(-1)
                print(2)
                if protein.IsNull():
                    self.logger.error("Received null protein")
                    break
                print(3)
                with self.condition:
                    self.message = protein
                    self.condition.notify()
                print(4)
        finally:
            self.hose.Withdraw()

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._listen, daemon=True)
            self.thread.start()
            self.logger.info("PlasmaListener started")

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()
            self.logger.info("PlasmaListener stopped")

    def get_message(self):
        print(5)
        with self.condition:
            self.condition.wait()
            print(6)
            return self.message

if __name__ == "__main__":
    listener = PlasmaListenerCondition(pool_name="tcp://localhost/hello")
    listener.start()
    listener.ready.wait(timeout=1.0)
    time.sleep(0.5)

    try:
        while True:
            print("A")
            message = listener.get_message()
            print("B")
            if message:
                try:
                    d, i = message.Descrips(), message.Ingests()
                    print("d ->", d.ToString())
                    print("i ->", i.ToString())
                except Exception as e:
                    print("Error processing message:", e)
            time.sleep(0.1)
    except KeyboardInterrupt:
        listener.stop()


