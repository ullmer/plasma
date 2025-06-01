import plasma

def main():
    pool_name = "tcp://localhost/hello"
    hose = plasma.Pool.Participate(pool_name)
    if hose is None:
        print(f"Failed to connect to pool: {pool_name}")
        return 1

    try:
        descrips = plasma.Slaw.List(plasma.Slaw("hello"))
        ingests = plasma.Slaw.Map(plasma.Slaw("name"), plasma.Slaw("world"))
        protein = plasma.Protein(descrips, ingests)

        print(f"depositing in {pool_name}")
        protein.ToSlaw().SpewToStderr()

        ret = hose.Deposit(protein)
        if ret.IsError():
            print(f"no luck on the deposit: {ret}")
            return 1
    finally:
        hose.Withdraw()

if __name__ == "__main__":
    main()
