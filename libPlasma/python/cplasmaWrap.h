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

char *poolnameDefault="tcp://localhost/hello";

void extract_slaw (char *arg, slaw ingest); //helper function for plasmaDeposit, copied from p-deposit.c
void plasmaInit();
//void plasmaDeposit(int cmd2, char *descripStr, char *ingestStr);

//int plasmaDeposit(pool_cmd_info cmd, char *descripStr, char *ingestStr);
//slaw   extract_slaw (char *arg); //helper function for plasmaDeposit, copied from p-deposit.c
//pool_cmd_info plasmaInit(char *pnstr);

/// end ///
