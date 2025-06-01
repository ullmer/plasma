import plasma

def main():
  pool_name = "tcp://localhost/hello"

  # Connect to the pool
  hose = plasma.Pool.Participate(pool_name)
  if hose is None: print(f"Failed to connect to pool: {pool_name}"); return 1

  try:
    while True:
      protein = hose.Next(-1)  # Waits indefinitely
      if protein.IsNull():
        print("Error: received null protein")
        break

      print(protein.ToSlaw().ToString())
  finally: print("add hose.withdraw binding"); #hose.Withdraw()

if __name__ == "__main__":
  main()

### end ###
