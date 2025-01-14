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

#include "cplasmaWrap.h"
#include <stdint.h>

char *poolnameDefault="tcp://localhost/hello";
pool_cmd_info cmd;

int           masterPlasmaCbBlockNumEntries;
plasmaCbBlock masterPlasmaCbBlock;

bool plasmaDualIntCbDbgFirstPrint;


////////////////// extract slaw ////////////////// 

void extract_slaw (char *arg, slaw *pair)
{
  char *colon = strchr (arg, ':');
  slaw key, value; 

  if (colon == NULL) { 
     fprintf (stderr, "error: ingest '%s' needs a colon to separate key and value\n", arg);
     exit (EXIT_FAILURE);
  }

  char *keystr = (char *) malloc (colon - arg + 1);
  strncpy (keystr, arg, colon - arg);
  keystr[colon - arg] = '\0';
  key = slaw_string (keystr);
  free (keystr);

  do { 
    char *endptr;
    int64 int_val = strtol (colon + 1, &endptr, 10);
    if (*endptr == '\0')
      { value = slaw_int64 (int_val);
        break;
      }
    float64 float_val = strtod (colon + 1, &endptr);
    if (*endptr == '\0') { 
      value = slaw_float64 (float_val);
      break;
    }
    value = slaw_string (colon + 1);
  } while (0);

  *pair = slaw_cons_ff (key, value);
}

////////////////// extract slaw ////////////////// 

//void extract_slaw (char *arg, slaw *pair)
//void build_slaw_unt16(uint16_t slawKey, uint16_t *ingestIntArray, int arraySize, slaw *pair)
slaw *build_slaw_unt16_array(int *intArray, int arraySize) {
  if (arraySize <= 0) {
    fprintf(stderr, "build_slaw_unt16: problem array size %i passed!\n", arraySize);
    return NULL;
  }

  unt16 sourceArray[arraySize];

  for (int i=0; i<arraySize; i++) {
    sourceArray[i] = (unt16) intArray[i];
  }

  slaw  *result = slaw_unt16_array(sourceArray, arraySize);
  return result;
}

////////////////// extract protein string payload ////////////////// 

char **extractProteinStrPayload(protein p) {

  // initially, hardwire this to our hello-world style contents.  Evolution will be critical.

  bslaw d = protein_descrips(p);
  bslaw i = protein_ingests(p);

  char *str1 = slaw_list_emit_first(d);
  void *map  = slaw_list_emit_first(i); //appears to work with "map" as well as "list"
  char *str2 = slaw_cons_emit_car(map); //~key   (Lisp-style naming)
  char *str3 = slaw_cons_emit_cdr(map); //~value (Lisp-style naming)

  //printf("ePSP: %s|%s|%s\n", str1, str2, str3);

  char **result = malloc(sizeof(char *) * 3);
  result[0] = str1;
  result[1] = str2;
  result[2] = str3;
  return result;
}

////////////////// plasma initialize ////////////////// 

void plasmaInit(char *pnstr) {
  OB_CHECK_ABI ();
  int           c;

  memset(&cmd, 0, sizeof(cmd));

  cmd.verbose   = 1;
  cmd.pool_name = pnstr;

  pool_cmd_open_pool (&cmd);

  masterPlasmaCbBlockNumEntries = 0;
  masterPlasmaCbBlock.nextBlock = NULL;
  plasmaDualIntCbDbgFirstPrint  = false;

  char  *tmStr = plasmaGetCodeReturnTypeMap();

  //printf("callback typemap string: %s\n", tmStr);
}

////////////////// plasma close ////////////////// 

void plasmaRegisterCb(int callbackCodeType, int callbackSourceType, void *callbackFunc) {
   if (masterPlasmaCbBlockNumEntries < 0) {
     fprintf(stderr, "plasmaRegisterCb: masterPlasmaCbBlockNumEntries has a negative value!\n"); return;
   }

   if (masterPlasmaCbBlockNumEntries >= PLASMA_CB_BLOCKSIZE) {
     fprintf(stderr, "plasmaRegisterCb: masterPlasmaCbBlockNumEntries presently has greater number than supported!\n"); return;
     // super-easy to extend, but not there yet.
   }

   masterPlasmaCbBlock.pcbTable[masterPlasmaCbBlockNumEntries].callbackCodeType   = (int8)     callbackCodeType;
   masterPlasmaCbBlock.pcbTable[masterPlasmaCbBlockNumEntries].callbackSourceType = (uint16_t) callbackSourceType;
   masterPlasmaCbBlock.pcbTable[masterPlasmaCbBlockNumEntries].callbackFunc       = callbackFunc;
   masterPlasmaCbBlockNumEntries += 1;
}

////////////////// plasma close ////////////////// 

void plasmaClose() {
 OB_DIE_ON_ERROR (pool_withdraw (cmd.ph));
}

////////////////// plasma deposit (string, string) ////////////////// 

//int plasmaDeposit(pool_cmd_info cmd, char *descripStr, char *ingestStr) {
int plasmaDeposit_StrStr(char *descripStr, char *ingestStr) {
  ob_retort pret;
  slaw     ingest;
  protein  prot;

  printf("plasma deposit begins\n");

  slabu   *descrips = slabu_new ();
  slabu   *ingests  = slabu_new ();

  extract_slaw (ingestStr, &ingest);
  OB_DIE_ON_ERROR (slabu_list_add_c (descrips, descripStr));
  OB_DIE_ON_ERROR (slabu_list_add_x (ingests, ingest));

  prot = protein_from_ff (slaw_list_f (descrips), slaw_map_f (ingests));
  if (cmd.verbose) { 
     fprintf (stderr, "depositing in %s\n", cmd.pool_name);
     slaw_spew_overview (prot, stderr, NULL);
  }

  pret = pool_deposit (cmd.ph, prot, NULL);
  protein_free (prot);

  if (OB_OK != pret) { 
    fprintf (stderr, "no luck on the deposit: %s\n", ob_error_string (pret));
    exit (pool_cmd_retort_to_exit_code (pret));
  }

  OB_DIE_ON_ERROR (pool_withdraw (cmd.ph));
  return EXIT_SUCCESS;
}

////////////////// plasma deposit (int16, int16 array ) ////////////////////////

//int    plasmaDeposit_Int16_Int16Arr(int16 descripInt, int16 *ingestIntArr, int arraySize);

////////////////// plasma deposit (unt16, unt16 array ) ////////////////////////

int    plasmaDeposit_Unt16_Unt16Arr(int descripInt, int *ingestIntArray, int arraySize) {
  ob_retort pret;
  slaw     ingest;
  protein  prot;

  printf("plasma unt16* deposit begins\n");

  //slabu   *descrips = slabu_new ();
  slaw *descrips = slaw_unt16(descripInt);
  slaw *ingests  = build_slaw_unt16_array(ingestIntArray, arraySize);

  prot = protein_from_ff (descrips, ingests); 
  if (cmd.verbose) { 
     fprintf (stderr, "depositing in %s\n", cmd.pool_name);
     slaw_spew_overview (prot, stderr, NULL);
  }

  pret = pool_deposit (cmd.ph, prot, NULL);
  protein_free (prot);

  if (OB_OK != pret) { 
    fprintf (stderr, "no luck on the deposit: %s\n", ob_error_string (pret));
    exit (pool_cmd_retort_to_exit_code (pret));
  }

  //OB_DIE_ON_ERROR (pool_withdraw (cmd.ph));
  return EXIT_SUCCESS;
}

////////////////// plasma await ////////////////// 

int plasmaAwait() {
  ob_retort pret;
  protein p;
  pool_timestamp ts;

  while (1)
    {
      pret = pool_await_next (cmd.ph, POOL_WAIT_FOREVER, &p, &ts, NULL);
      if (OB_OK != pret)
        {
          pool_withdraw (cmd.ph);
          fprintf (stderr, "problem with pool_await_next(): %s\n",
                   ob_error_string (pret));
          return pool_cmd_retort_to_exit_code (pret);
        }
      slaw_spew_overview (p, stdout, NULL);
      fputc ('\n', stdout);
      protein_free (p);
    }

  // Not reached at present.
  OB_DIE_ON_ERROR (pool_withdraw (cmd.ph));
  pool_cmd_free_options (&cmd);

  return EXIT_SUCCESS;
}

////////////////// plasma await next ////////////////// 

char **plasmaAwaitNextTrio() {
  ob_retort pret;
  protein p;
  pool_timestamp ts;

  //printf("plasmaAwaitNextChars begins\n");

  pret = pool_await_next (cmd.ph, POOL_WAIT_FOREVER, &p, &ts, NULL);
  if (OB_OK != pret)
    {
      pool_withdraw (cmd.ph);
      fprintf (stderr, "problem with pool_await_next(): %s\n",
                        ob_error_string (pret));
      //return pool_cmd_retort_to_exit_code (pret);
      return NULL;
    }

  //slaw_spew_overview (p, stdout, NULL);
  //fputc ('\n', stdout);

  char **payloadExtraction = extractProteinStrPayload(p);

  //printf("S1: %s\n", payloadExtraction[0]);
  //printf("S2: %s\n", payloadExtraction[1]);
  //printf("S3: %s\n", payloadExtraction[2]);

  //char *result = slaw_str_overview (p, NULL);
  //protein_free (p); // this was segfaulting; commenting it probably introduces a memory leak
  return payloadExtraction;
}

////////////////// plasmaGetProtFmtStr ////////////////// 

//migrate soon to .h file

#define PROTF_FRMT_SIMPLEKEYVAL "{D:[S],I:{S: S}}" //YAML descriptor of jshrake hello-world
#define PROTF_NAME_SIMPLEKEYVAL "prot:simpleKeyVal"

char *plasmaGetProtFormatNames() {
  //hardwired initially :-)
  return PROTF_NAME_SIMPLEKEYVAL;
}

char *plasmaGetProtFormatStr(char *formatName) {

  if (formatName == NULL || 
      strcmp(formatName, "")==0 || 
      strcmp(formatName, PROTF_NAME_SIMPLEKEYVAL)==0) {
    return PROTF_FRMT_SIMPLEKEYVAL;
  } 

  fprintf(stderr, "plasmaGetProtFormatStr: presently unsupported format requested: %s\n", formatName);
  return NULL;
}

////////////////// plasma code return types size ////////////////// 

char *plasmaMapCbCode2Str(int cbCode) {
  switch (cbCode) {
    case PLASMA_CB_CODE_TYPE_C_ID:       return PLASMA_CB_CODE_TYPE_C_STR;
    case PLASMA_CB_CODE_TYPE_PYTHON_ID:  return PLASMA_CB_CODE_TYPE_PYTHON_STR;
    case PLASMA_CB_CODE_TYPE_HASKELL_ID: return PLASMA_CB_CODE_TYPE_HASKELL_STR;
    case PLASMA_CB_CODE_TYPE_SWIFT_ID:   return PLASMA_CB_CODE_TYPE_SWIFT_STR;
    case PLASMA_CB_CODE_TYPE_PROLOG_ID:  return PLASMA_CB_CODE_TYPE_PROLOG_STR;
    case PLASMA_CB_CODE_TYPE_JAVA_ID:    return PLASMA_CB_CODE_TYPE_JAVA_STR;
  }
  return NULL;
}

////////////////// plasma code return type size ////////////////// 
int plasmaCodeReturnTypeSize(int typeId) {
  if (typeId < 0) return 0;

  int result    = 2;
  char *typeStr = plasmaMapCbCode2Str(typeId);

  if (typeStr != NULL) result += strlen(typeStr);

  if      (typeId < 10)   result += 1;
  else if (typeId < 100)  result += 2;
  else if (typeId < 1000) result += 3;
  else result = 0;

  return result;
}

////////////////// plasma code return types size ////////////////// 

int plasmaCodeReturnTypesSize() {
  int result = 0;

  for (int i=1; i<=PLASMA_CB_CODE_NUM_TYPES; i++) result += plasmaCodeReturnTypeSize(i);
  return result;
}

////////////////// plasma get code return type map ////////////////// 

void *plasmaUnt16CbDbg(protein *p, int num) { 
  bslaw ing = protein_ingests(p);
  
  if (plasmaDualIntCbDbgFirstPrint) {
    printf("plasmaDualIntCbDbg: [");
    plasmaDualIntCbDbgFirstPrint = false;
  } else printf("[");

  for (int i=0; i<num; i++) {
    unt16 val = slaw_unt16_array_emit_nth(ing, i);
    printf("%i ", (int)val);
  }

  printf("] ");
  fflush(stdout);

  return NULL;
}

////////////////// plasma get code return type map ////////////////// 

char  *plasmaGetCodeReturnTypeMap() { 
  int   typeMapSize = plasmaCodeReturnTypesSize();
  char *result      = malloc(typeMapSize + 1);
  char *idx         = result;
  int   len;

  for (int i=1; i<=PLASMA_CB_CODE_NUM_TYPES; i++) {
    char *typeStr = plasmaMapCbCode2Str(i);
    sprintf(idx, "%s:%i;", typeStr, i); 
    len = strlen(idx); idx += len;
  }

  return result;
}

////////////////// plasma next ////////////////// 

char **plasmaPoolNextStr(char *formatStr) {
  ob_retort pret;
  protein p;
  pool_timestamp ts;

  pret = pool_next (cmd.ph, &p, &ts, NULL);

  if (OB_OK != pret) {
    //return pool_cmd_retort_to_exit_code (pret);
    return NULL;
  }

  if (formatStr==NULL || strcmp(formatStr, "")==0) {
    formatStr = plasmaGetProtFormatStr(NULL);
  }

  if (strcmp(formatStr, PROTF_FRMT_SIMPLEKEYVAL) == 0) { // perhaps a bit redundant, but safer
    char **payloadExtraction = extractProteinStrPayload(p);
    return payloadExtraction;
  } else {
    fprintf(stderr, "plasmaPoolNext: presently unsupported formatStr received: %s\n", formatStr);
  }

  return NULL;
}

/*
void *plasmaPoolNextFlex(char *formatStr) {
  ob_retort pret;
  protein p;
  pool_timestamp ts;

  pret = pool_next (cmd.ph, &p, &ts, NULL);

  if (OB_OK != pret) {
    //return pool_cmd_retort_to_exit_code (pret);
    return NULL;
  }

  if (formatStr==NULL || strcmp(formatStr, "")==0) {
    formatStr = plasmaGetProtFormatStr(NULL);
  }

  if (strcmp(formatStr, PROTF_FRMT_SIMPLEKEYVAL) == 0) { // perhaps a bit redundant, but safer
    //char **payloadExtraction = extractProteinStrPayload(p);
    //return payloadExtraction;
    return NULL;
  } else {
    fprintf(stderr, "plasmaPoolNext: presently unsupported formatStr received: %s\n", formatStr);
  }
  return NULL;
}
*/
/// end ///
