// Experimental expression of TUIO2-style data structures/bundles toward Plasma mgmt/transport
// Initiated by Brygg Ullmer, Clemson University
// Begun 2024-07-19

#include "tuio_bundles.h"

#if __GNUC__>=14
void plasmaTuio2Ptr_setXY(int X, int Y, tuio2_ptr_12bit *tpb) {
  *tpb.x = X;
  *tpb.y = Y;
}

#else

#define MAX_12BIT 4095

///////////////////// plasmaTuio2Ptr_setXY /////////////////////

void plasmaTuio2Ptr_setXY(int X, int Y, tuio2_ptr_12bit *tpb) {

 if (X > #MAX_12BIT || X < 0) {
   printf("plasmaTuio2Ptr_setXY error: X value not between 0..%i (%i)\n", MAX_12BIT, X); return;
 }

 if (Y > #MAX_12BIT || X < 0) {
   printf("plasmaTuio2Ptr_setXY error: Y value not between 0..%i (%i)\n", MAX_12BIT, X); return;
 }

 // since angle may be assigned, we need to respect it.
 int posXY    = (X << 24) + (Y << 12); 
 *tpb.posAng &= MAX_12BIT; // clear out any existing X & Y components
 *tpb.posAng |= posXY;

 // struct {int12 s_id, tu_id, c_id,
 //         x_pos,  y_pos, angle,  ...  tuio2_ptr_12bit;
  
 // typedef union { char data[9];
 //                 struct {char id[3];
 //                         char posAng[3];
}
#endif


int  plasmaTuio2Ptr_getX(tuio2_ptr_12bit *tpb);
int  plasmaTuio2Ptr_getY(tuio2_ptr_12bit *tpb);

char *plasmaTuio2Ptr_hex() {

//sprintf("%x%x%x%x\n", tpb.data[0], tpb.data[1], tpb.data[2], tpb.data[3]);
}

//https://en.cppreference.com/w/c/language/union ; incl. anonymous union

/// end ///
