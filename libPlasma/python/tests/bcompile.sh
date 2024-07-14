PLASMA_HOME=/home/ullmer/git/plasma
WSL2_LIB=/usr/lib/x86_64-linux-gnu
RPI_LIB=/usr/lib/aarch4-linux-gnu

gcc -I.. -I$PLASMA_HOME/libPlasma/c/ -I$PLASMA_HOME \
    -DABS_TOP_SRCDIR=\"$PLASMA_HOME\" -g cpc_test01.c ../*.o -lc \
$PLASMA_HOME/build/libPlasma/c/libPlasma.a \
$PLASMA_HOME/build/libLoam/c/libLoam.a \
-L$PLASMA_HOME/build \
-o cpc_test01 \
-ldl -lm  -lpthread  -L/lib  -licuuc -licui18n  -lavahi-common -lavahi-client \
/usr/lib/x86_64-linux-gnu/libyaml.a \
/usr/lib/x86_64-linux-gnu/libboost_filesystem.a \
/usr/lib/x86_64-linux-gnu/libboost_regex.a \
/usr/lib/x86_64-linux-gnu/libboost_system.a \
-L/usr/local/ssl/lib -lssl -lcrypto -lrt

/usr/lib/aarch64-linux-gnu/
