// test of integer vector

#include "libPlasma/c++/Pool.h"
#include "libPlasma/c++/Protein.h"
#include "libPlasma/c++/Hose.h"
#include "libLoam/c++/Str.h"

#include <iostream>
#include <memory>

using namespace oblong::plasma;
using namespace oblong::loam;

int main() {

  v2int32 v2 = { 43, -129 };
  Slaw sv2 (v2);
  v2int32 v22 (sv2.Emit<v2int32> ());
  assert (v2 == v22);

  return 0;
}
/// end ///
