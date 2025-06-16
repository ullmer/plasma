# Example of threaded enoPlasmaListener
# Brygg Ullmer, Clemson University
# Begun 2025-06-08

from enoPlasmaListener import *
import time, sys, traceback

def handle_message(protein): 
  #print("!", end=''); sys.stdout.flush()
  try:
    d, i = protein.Descrips(), protein.Ingests()
    print(1)
    dstr, ilst = d.getStr(), i.getList()
    print(2)
    print("D:", dstr)
    print("I:", str(ilst))
  except: print("exception"); traceback.print_exc()

pn = 'tcp://localhost/grObjPool'

listener = enoPlasmaListener(poolName=pn, callback=handle_message)
listener.start()

for i in range(1000): 
  print(str(i) + " ", end='')
  sys.stdout.flush(); time.sleep(1.)

### end ###
