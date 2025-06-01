import plasma

def main():
  pool_name = "tcp://localhost/hello"

  # Connect to the pool
  hose = plasma.Pool.Participate(pool_name)
  if hose is None: print(f"Failed to connect to pool: {pool_name}"); return 1

  try:
    while True:
      protein = hose.Next(-1)  # Waits indefinitely
      #if protein.IsNull(): print("Error: received null protein") break

      s1 = protein.ToSlaw()
      s2 = s1.ToString()
      print(str(s2))
  finally: print("add hose.withdraw binding"); #hose.Withdraw()

if __name__ == "__main__":
  main()

### end ###
