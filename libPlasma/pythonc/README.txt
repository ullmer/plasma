building without root or ninja, assuming 6-core system (-j 6):

plasma:
mkdir build; cd build
cmake .. -DCMAKE_C_FLAGS="-Wno-incompatible-pointer-types” \
   -DCMAKE_POSITION_INDEPENDENT_CODE=ON
make -j 6

pybind11: 
mkdir ~/local
mkdir build; cd build
cmake ..   -DCMAKE_PREFIX_PATH=$HOME/local
make -j 6
make install

plasma pythonc:
mkdir build; cd build
cmake .. -DCMAKE_PREFIX_PATH=$HOME/local

