/* Original (c) oblong industries */

// Adaptation by Brygg Ullmer, Clemson University
// reduction to cython wrapper, initially re JShrake helloWorld example from Animist discord #plasma 

/// Deposit a protein into a pool.

#include "pool_cmd.h"
#include "libLoam/c/ob-log.h"
#include "libLoam/c/ob-sys.h"
#include "libLoam/c/ob-vers.h"
#include "libPlasma/c/protein.h"
#include "libPlasma/c/slaw.h"

static slaw        extract_slaw (char *arg); //helper function for plasmaDeposit, copied from p-deposit.c
cmdDescripsIngests plasmaInit(char *pnstr = "tcp://localhost/hello");
cmdDescripsIngests plasmaDeposit(pool_cmd_info cmd, char *dstr  = "hello", char *istr  = "name:world");

/// end ///