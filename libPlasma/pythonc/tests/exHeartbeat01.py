import plasma
import time

pool_name = "tcp://localhost/grObjPool" #graphical object pool
hose = plasma.Pool.Participate(pool_name)
if hose is None:
  print(f"Failed to connect to pool: {pool_name}")
  return 1
 
try:
  i  = 0
  hb = plasma.create.string("hb") #heartbeat

  while True:
    id      = plasma.create.int32(i)
    protein = plasma.Protein(hb, id)
 
    print(f"depositing in {pool_name}")
    print(protein.ToSlaw().ToString())
 
    ret = hose.Deposit(protein)
    if ret.IsError():
      print(f"no luck on the deposit: {ret}")
      return 1
    time.sleep(10)

finally:
  hose.Withdraw()

if __name__ == "__main__":
  main()
 
### end ###
