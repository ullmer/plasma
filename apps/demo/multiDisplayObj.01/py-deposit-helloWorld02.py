# Warmup toward graphical multi-display hello world functionality
# Brygg Ullmer, Clemson University
# Begun 2025-06-01

import plasma

def main():
  pool_name = "tcp://localhost/grObjPool" #graphical object pool
  hose = plasma.Pool.Participate(pool_name)
  if hose is None:
    print(f"Failed to connect to pool: {pool_name}")
    return 1

  try:
    descrips = plasma.Slaw.List(plasma.Slaw("sharedCanvas"))
    objName   = "sq1"
    objAction = "move"
    objCoords = [10, 10]

    psObjName, psObjAction    = plasma.Slaw(objName),   plasma.Slaw(objAction)
    psObjCoords               = plasma.Slaw.List(objCoords)
    psObjUpdates              = plasma.Slaw.List(psObjAction, psObjCoords)

    ingests = plasma.Slaw.Map(psObjName, psObjUpdates)
    protein = plasma.Protein(descrips, ingests)

    print(f"depositing in {pool_name}")
    print(protein.ToSlaw().ToString())

    ret = hose.Deposit(protein)
    if ret.IsError():
      print(f"no luck on the deposit: {ret}")
      return 1
  finally:
    hose.Withdraw()

if __name__ == "__main__":
  main()

### end ###
