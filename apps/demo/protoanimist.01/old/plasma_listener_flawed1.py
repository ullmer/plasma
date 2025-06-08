import threading
import plasma
import queue
import time
import logging

class PlasmaListener:

  pool_name, hose, thread, running = [None]*4
  message_queue, ready             = [None]*2

  def __init__(self, pool_name="tcp://localhost/hello"):
    self.pool_name = pool_name
    self.hose      = None
    self.thread    = None
    self.running   = False
    self.ready     = threading.Event()

    self.message_queue = queue.Queue()  # Thread-safe queue for communication

    # Set up logging
    logging.basicConfig(level=logging.INFO)
    self.logger = logging.getLogger(__name__)

  def _listen(self):
    self.hose = plasma.Pool.Participate(self.pool_name)
    self.ready.set()

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
        self.logger.debug(f"Received protein: {protein}")
        self.logger.debug(f"Descrips: {protein.Descrips().ToString()}")
        self.logger.debug(f"Ingests: {protein.Ingests().ToString()}")
        print(3)
        self.message_queue.put(protein)
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
    try:
      print(5)
      #result = self.message_queue.get(timeout=0.1)
      result = self.message_queue.get()
      print(6)
      return result
    except queue.Empty:
      return None

# Test harness
if __name__ == "__main__":
  listener = PlasmaListener(pool_name="tcp://localhost/hello")
  listener.start()
  listener.ready.wait(timeout=1.0)  # Wait until listener is ready
  time.sleep(0.5)

  try:
    while True:
      print('A')
      message = listener.get_message()
      print('B')
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

