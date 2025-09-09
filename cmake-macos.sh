cmake .. -GNinja  -DOPENSSL_ROOT_DIR=/opt/local/libexec/openssl3  -DOPENSSL_INCLUDE_DIR=/opt/local/libexec/openssl3/include  -DCMAKE_CXX_STANDARD=17  -DCMAKE_EXE_LINKER_FLAGS="-L/opt/local/libexec/openssl3/lib"  -DCMAKE_SHARED_LINKER_FLAGS="-L/opt/local/libexec/openssl3/lib"   -DCMAKE_CXX_FLAGS="-std=c++17" -DCMAKE_INSTALL_PREFIX=/usr/local -DPKGCONFIG_INSTALL_DIR=/usr/local/lib/pkgconfig -DCMAKE_INSTALL_LIBDIR=lib -DCMAKE_INSTALL_DATAROOTDIR=share



