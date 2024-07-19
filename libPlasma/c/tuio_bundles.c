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

void plasmaTuio2Ptr_setXY(int X, int Y, tuio2_ptr_12bit *tpb) {
 // warming up to careful bitshifting and bitsetting
 // struct {int12 s_id, tu_id, c_id,
 //         x_pos,  y_pos, angle,  ...  tuio2_ptr_12bit;
  
 // typedef union { char data[9];
 //                 struct {char id[3];
 //                         char posAng[3];

}
#endif


int  plasmaTuio2Ptr_getX(tuio2_ptr_12bit *tpb);
int  plasmaTuio2Ptr_getY(tuio2_ptr_12bit *tpb);

//https://en.cppreference.com/w/c/language/union ; incl. anonymous union

/// end ///
