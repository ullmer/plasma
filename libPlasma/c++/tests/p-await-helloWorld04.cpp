// C++ version of p-await-helloWorld03.c, as auto-ported by CoPilot
// Continuously reads proteins from a pool using libPlasma++

#include "libPlasma/c++/Pool.h"
#include "libPlasma/c++/Protein.h"
#include "libPlasma/c++/Hose.h"
#include "libLoam/c++/Str.h"

#include <iostream>
#include <memory>

using namespace oblong::plasma;
using namespace oblong::loam;

int main() {
  const char *pool_name = "tcp://localhost/hello";
  ObRetort ret;

  std::unique_ptr<Hose> hose(Pool::Participate(pool_name, &ret));
  if (!hose || ret != OB_OK) {
    std::cerr << "Failed to connect to pool: " << pool_name << std::endl;
    return 1;
  }

  while (true) {
    Protein p = hose->Next();  // waits indefinitely
    if (p.IsNull()) {
      std::cerr << "Error reading from pool: " << ob_error_string(hose->LastRetort().NumericRetort()) << std::endl;
      break;
    }

    std::cout << p.ToSlaw().ToString() << std::endl;
  }

  hose->Withdraw();
  return 0;
}
/// end ///
