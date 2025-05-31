// C++ version of p-await-helloWorld03.c, as auto-ported by CoPilot
// Continuously reads proteins from a pool using libPlasma++

#include "libPlasma/c++/Pool.h"
#include "libPlasma/c++/Protein.h"
#include "libPlasma/c++/Slaw.h"
#include "libLoam/c++/Str.h"
#include "libLoam/c++/ObLog.h"

#include <iostream>
#include <memory>

using namespace oblong::plasma;
using namespace oblong::loam;

int main() {
  const Str pool_name("tcp://localhost/hello");

  try {
    // Open the pool
    std::shared_ptr<Pool> pool = Pool::Open(pool_name);

    while (true) {
      // Wait indefinitely for the next protein
      Protein p = pool->Next();

      // Print the protein overview
      std::cout << p.ToSlaw().ToString() << std::endl;
    }

    // Not reached in this loop, but good practice
    pool->Withdraw();
  } catch (const oblong::loam::Exception &e) {
    OB_LOG_ERROR << "Exception: " << e.what();
    return EXIT_FAILURE;
  }

  return EXIT_SUCCESS;
}

/// end ///
