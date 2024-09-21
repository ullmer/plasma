# Example of Py4J-wrapped Plasma deposit
# Brygg Ullmer, Clemson University
# Begun 2024-09-20

import sys; sys.path.append("..")
from p4jPlasma import *

addr = '172.25.49.14'
#addr = '127.0.0.1'
#addr = '130.127.48.81'

p4jp = p4jPlasma(hostAddress=addr)
ph   = p4jp.pCreateHose("h1", "tcp://localhost/hello")

while True:
  p = ph.pAwaitNext()
  print(p)
  print("D", p[0])
  print("I", p[1])

### end ###
