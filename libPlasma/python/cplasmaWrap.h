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
#include <stdint.h>

extern char *poolnameDefault;
extern pool_cmd_info cmd;

char  *slaw_str_overview (bslaw s, const char *prolo);

void   extract_slaw (char *arg, slaw *ingest); //helper function for plasmaDeposit, copied from p-deposit.c
slabu *slabu_from_slaw (bslaw list);

void   plasmaInit(char *poolnameStr);
void   plasmaClose(); 

int    plasmaDeposit_StrStr        (char *descripStr, char *ingestStr);
int    plasmaDeposit_Unt16_Unt16Arr(int descripInt, int *ingestIntArr, int arraySize);
int    plasmaAwait();
char **plasmaAwaitNextChars();
char **plasmaAwaitNextTrio();
char **plasmaPoolNextStr(char *formatStr);
void  *plasmaPoolNextFlex(char *formatStr);
char  *plasmaGetProtFormatStr(char *formatName);
char  *plasmaGetProtFormatNames();

#define PLASMA_CB_CODE_TYPE_C       1
#define PLASMA_CB_CODE_TYPE_PYTHON  2
#define PLASMA_CB_CODE_TYPE_HASKELL 3
#define PLASMA_CB_CODE_TYPE_SWIFT   4 
#define PLASMA_CB_TYPE_PROLOG       5 

typedef struct {
   int8  callbackCodeType;   //PLASMA_CB_CODE_TYPE_C, PLASMA_CB_CODE_TYPE_PYTHON, etc.
   int16 callbackSourceType;
   void* callbackFunc;
}

//int    plasmaDeposit_Int16_Int16Arr(int16_t  descripInt,  int16_t *ingestIntArr, int arraySize);
//int    plasmaDeposit_Unt16_Unt16Arr(uint16_t descripInt, uint16_t *ingestIntArr, int arraySize);

/// end ///
