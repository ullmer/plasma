# Threaded, callback-based PlasmaListener code
# Original co-implemented by CoPilot and Brygg Ullmer, Clemson University
# Begun 2025-06-08

import threading
import logging
import plasma
import queue
import time

################ PlasmaListener ################ 

class enoPlasmaListener:
  poolName,  hose,  thread = [None]*3
  running, callback, ready = [None]*3
  checkinInterval      = .03 # this should change depending upon many particulars

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs)
    self.running = False
    self.ready = threading.Event()
    self.queue = queue.Queue()
    logging.basicConfig(level=logging.INFO)
    self.logger = logging.getLogger(__name__)

  def _listener(self):
    try:
      if self.poolName is None:
        self.logger.error("No pool name provided!")
        return
      self.hose = plasma.Pool.Participate(self.poolName)
      if self.hose is None:
        self.logger.error(f"Failed to connect to pool: {self.poolName}")
        return
      self.logger.info("Connected to pool, listening for messages...")
      self.ready.set()
    except Exception as e:
      self.logger.error(f"_listener setup issue: {e}")
      return

    try:
      while self.running:
        protein = self.hose.Next(-1)
        if protein.IsNull():
          self.logger.warning("Received null protein")
          continue
        self.queue.put(protein)
    finally:
      self.hose.Withdraw()

  def _worker(self):
    while self.running:
      try:
        protein = self.queue.get(timeout=0.5)
        if self.callback:
          self.callback(protein)
      except queue.Empty:
        continue

  def start(self):
    if not self.running:
      self.running = True
      self.listener_thread = threading.Thread(target=self._listener, daemon=True)
      self.worker_thread = threading.Thread(target=self._worker, daemon=True)
      self.listener_thread.start()
      self.worker_thread.start()
      self.logger.info("enoPlasmaListener started")

  def stop(self):
    self.running = False
    if hasattr(self, 'listener_thread'):
      self.listener_thread.join()
    if hasattr(self, 'worker_thread'):
      self.worker_thread.join()
    self.logger.info("PlasmaListener stopped")

### end ###
