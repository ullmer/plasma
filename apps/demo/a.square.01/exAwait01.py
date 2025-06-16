# Example of threaded enoPlasmaListener
# Brygg Ullmer, Clemson University
# Begun 2025-06-08

from enoPlasmaListener import *
import time, sys

def handle_message(protein): 
  print("!", end=''); sys.stdout.flush()

listener = enoPlasmaListener(poolName="tcp://localhost/hello", callback=handle_message)
listener.start()

for i in range(1000): 
  print(str(i) + " ", end='')
  sys.stdout.flush(); time.sleep(.5)

### end ###
