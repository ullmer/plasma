
import threading
import plasma
import queue
import time
import logging

class PlasmaListener:
    def __init__(self, pool_name="tcp://localhost/hello"):
        self.pool_name = pool_name
        self.hose = None
        self.thread = None
        self.running = False
        self.message_queue = queue.Queue()  # Thread-safe queue for communication

        # Set up logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def _listen(self):
        self.hose = plasma.Pool.Participate(self.pool_name)
        if self.hose is None:
            self.logger.error(f"Failed to connect to pool: {self.pool_name}")
            return

        try:
            while self.running:
                protein = self.hose.Next(-1)
                if protein.IsNull():
                    self.logger.error("Received null protein")
                    break
                self.message_queue.put(protein)  # Pass to main thread or handler
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
        try:
            return self.message_queue.get_nowait()
        except queue.Empty:
            return None

# Test harness
if __name__ == "__main__":
    listener = PlasmaListener(pool_name="tcp://localhost/hello")
    listener.start()

    try:
        while True:
            message = listener.get_message()
            if message:
                d, i = message.Descrips(), message.Ingests()
                print("d ->", d.ToString())
                print("i ->", i.ToString())
            time.sleep(1)
    except KeyboardInterrupt:
        listener.stop()
