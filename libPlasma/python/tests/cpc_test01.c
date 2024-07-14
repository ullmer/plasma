#include "cplasma_cython.h"

int main (int argc, char **argv)
{
  pool_cmd_info cmd = plasmaInit("tcp://localhost/hello");
  plasmaDeposit(cmd, "hello", "name:world");
}

/// end ///
