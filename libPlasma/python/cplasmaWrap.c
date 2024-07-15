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
pool_cmd_info cmd;

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

////////////////// slaw format to string ////////////////// 

#define DEFAULT_VSNPRINTF_BUFFER_LEN 500
#define DEFAULT_VSNPRINTF_BUFFER_MAX_MULTIPLIER 4
char *VSNPRINTF_UNKNOWN_ERROR = "ERROR: vsnprintf unknown error (likely encountered in slaw_format_to_string)";

int slaw_format_to_stringResult;

static void slaw_format_to_string (void *v, const char *fmt, ...)
{
  char *targBuffer = (char *)v;

  va_list vargs;
  va_start  (vargs, fmt);
  slaw_format_to_stringResult = vsnprintf (targBuffer, DEFAULT_VSNPRINTF_BUFFER_LEN, fmt, vargs);
  va_end    (vargs);
}

void slaw_str_overview (bslaw s, char *targBuffer, const char *prolo)
{
  slaw_spew_internal (s, slaw_format_to_string, (void *) targBuffer, prolo);
}


char *slaw_str_overview (bslaw s, const char *prolo)
{
  char *targBuffer = malloc(DEFAULT_VSNPRINTF_BUFFER_LEN);
  slaw_str_overview(s, targBuffer, prolo);

  if (slaw_format_to_stringResult >= 0) {return targBuffer;}

  for (int i=1; i <= DEFAULT_VSNPRINTF_BUFFER_MAX_MULTIPLIER; i++) {
    free(targBuffer)
    targBuffer = malloc(DEFAULT_VSN_PRINTF_BUFFER_LEN * i)
    if (slaw_format_to_stringResult >= 0) {return targBuffer}
  } 

  return VSNPRINTF_UNKNOWN_ERROR;
}

////////////////// plasma initialize ////////////////// 

void plasmaInit(char *pnstr) {
  OB_CHECK_ABI ();
  int           c;

  memset(&cmd, 0, sizeof(cmd));

  cmd.verbose   = 1;
  cmd.pool_name = pnstr;

  pool_cmd_open_pool (&cmd);
}

////////////////// plasma deposit ////////////////// 

//int plasmaDeposit(pool_cmd_info cmd, char *descripStr, char *ingestStr) {
int plasmaDeposit(char *descripStr, char *ingestStr) {
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

char *plasmaAwaitNext() {
  ob_retort pret;
  protein p;
  pool_timestamp ts;

  pret = pool_await_next (cmd.ph, POOL_WAIT_FOREVER, &p, &ts, NULL);
  if (OB_OK != pret)
    {
      pool_withdraw (cmd.ph);
      fprintf (stderr, "problem with pool_await_next(): %s\n",
                        ob_error_string (pret));
      return pool_cmd_retort_to_exit_code (pret);
    }
  //slaw_spew_overview (p, stdout, NULL);
  //fputc ('\n', stdout);
  protein_free (p);
}

/// end ///
