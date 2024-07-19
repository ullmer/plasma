// Experimental expression of TUIO2-style data structures/bundles toward Plasma mgmt/transport
// Initiated by Brygg Ullmer, Clemson University
// Begun 2024-07-19

#define int12 _BitInt(12)

struct tuio2_ptr_12bit { //https://en.cppreference.com/w/c/language/union ; incl. anonymous union
  union { char data[8];
          struct {int12 s_id, tu_id, c_id, 
                        x_pos, y_pos,
                        angle, shear, 
                        radius, press;}
        }
}

/// end ///
