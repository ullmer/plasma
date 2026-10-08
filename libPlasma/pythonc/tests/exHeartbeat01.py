import plasma
import time
import sys

pool_name = "tcp://localhost/grObjPool" #graphical object pool
hose = plasma.Pool.Participate(pool_name)

if hose is None:
  print(f"Failed to connect to pool: {pool_name}")
  sys.exit(-1)
 
print(f"depositing in {pool_name}")
try:
  i  = 0
  hb = plasma.create.string("hb") #heartbeat

  while True:
    id      = plasma.create.int32(i)
    protein = plasma.Protein(hb, id)
 
    print(protein.ToSlaw().ToString())
 
    ret = hose.Deposit(protein)
    if ret.IsError():
      print(f"no luck on the deposit: {ret}")
      sys.exit(-1)
    time.sleep(10)

finally:
  hose.Withdraw()

if __name__ == "__main__":
  main()
 
### end ###
