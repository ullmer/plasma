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

char *poolnameDefault="tcp://localhost/hello";

////////////////// extract slaw ////////////////// 

//slaw extract_slaw (char *arg)
//int extract_slaw (char *arg)
void extract_slaw (char *arg, slaw pair)
{
  char *colon = strchr (arg, ':');
  slaw key, value; //, pair;

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

  pair = slaw_cons_ff (key, value);
  //return (int) pair;
  //return (void *) &pair;
}

////////////////// plasma Initialize ////////////////// 

//pool_cmd_info plasmaInit(char *pnstr) {
//int plasmaInit(char *pnstr) {
//int plasmaInit() {
void plasmaInit() {

  OB_CHECK_ABI ();

  pool_cmd_info cmd;
  int           c;

  memset(&cmd, 0, sizeof(cmd));

  cmd.verbose   = 1;
  //cmd.pool_name = pnstr;
  cmd.pool_name = poolnameDefault;

  pool_cmd_open_pool (&cmd);

  //return (int)cmd;
}

////////////////// plasma deposit ////////////////// 

//int plasmaDeposit(pool_cmd_info cmd, char *descripStr, char *ingestStr) {
/*
int plasmaDeposit(int cmd2, char *descripStr, char *ingestStr) {

  pool_cmd_info cmd  = (pool_cmd_info) cmd2;

  ob_retort pret;
  slaw     ingest;
  protein  prot;
  slabu   *descrips = slabu_new ();
  slabu   *ingests  = slabu_new ();

  extract_slaw (ingestStr, ingest);
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
*/

/// end ///
