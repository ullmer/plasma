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

extern char *poolnameDefault;
extern pool_cmd_info cmd;

char *slaw_str_overview (bslaw s, const char *prolo);

void  extract_slaw (char *arg, slaw *ingest); //helper function for plasmaDeposit, copied from p-deposit.c

void   plasmaInit(char *poolnameStr);
void   plasmaClose(); 
int    plasmaDeposit_StrStr(char *descripStr, char *ingestStr);
int    plasmaAwait();
char **plasmaAwaitNextChars();
char **plasmaAwaitNextTrio();
char **plasmaPoolNext(char *formatStr);
char  *plasmaGetProtFormatStr(char *formatName);
char  *plasmaGetProtFormatNames();

/// end ///
