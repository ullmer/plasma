// Experimental expression of TUIO2-style data structures/bundles toward Plasma mgmt/transport
// Initiated by Brygg Ullmer, Clemson University
// Begun 2024-07-19

#include "tuio_bundles.h"

int main() {
  tuio2_ptr_12bit tpb;
  tpb.xpos = 100;
  tpb.ypos = 3000;
  print("%x%x%x%x\n", tpb.data[0], tpb.data[1], tpb.data[2], tpb.data[3]);
}

/// end ///
