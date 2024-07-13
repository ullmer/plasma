#include "cplasma-cython.h"

int main (int argc, char **argv)
{
  cmdDescripsIngests cmd = plasmaInit("tcp://localhost/hello");
  plasmaDeposit(cmd, "hello", "name:world");
}

/// end ///
