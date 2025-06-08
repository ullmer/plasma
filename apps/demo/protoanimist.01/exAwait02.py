# Example of threaded enoPlasmaListener
# Brygg Ullmer, Clemson University
# Begun 2025-06-08

from enoPlasmaListener import *
import time, sys

def handle_message(protein): logging.info('P')

listener = enoPlasmaListener(poolName="tcp://localhost/hello", callback=handle_message)
listener.start()
listener.ready.wait(timeout=1.0)

for i in range(1000): 
  logging.info(str(i) + " ")
  sys.stdout.flush(); time.sleep(.5)

### end ###
