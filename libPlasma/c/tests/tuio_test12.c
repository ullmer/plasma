// Experimental expression of TUIO2-style data structures/bundles toward Plasma mgmt/transport
// Initiated by Brygg Ullmer, Clemson University
// Begun 2024-07-19

#include <stdio.h>
#include "tuio_bundles.h"

int main() {
  tuio2_ptr_12bit tpb;

  printf("GCC version number: %i\n", __GNUC__);

  int xpos = 100;
  int ypos = 3000;

  plasmaTuio2Ptr_setXY(xpos, ypos, &tpb);

  int x2 = plasmaTuio2Ptr_getX(&tpb);
  int y2 = plasmaTuio2Ptr_getY(&tpb);

  printf("tpb hex representation: %s\n", plasmaTuio2Ptr_hex())
  printf("xy: %i, %i\n", x2, y2);
}

/// end ///
