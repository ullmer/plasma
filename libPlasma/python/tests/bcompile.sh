#PLASMA_HOME=/home/ullmer/git/plasma
PLASMA_HOME=/home/bullmer/git/plasma

WSL2_LIB=/usr/lib/x86_64-linux-gnu
RPI_LIB=/usr/lib/aarch64-linux-gnu
#OTHER_LIB=$RPI_LIB
OTHER_LIB=$WSL2_LIB

gcc -I.. -I$PLASMA_HOME/libPlasma/c/ -I$PLASMA_HOME \
    -DABS_TOP_SRCDIR=\"$PLASMA_HOME\" -g cpc_test01.c ../*.o -lc \
$PLASMA_HOME/build/libPlasma/c/libPlasma.a \
$PLASMA_HOME/build/libLoam/c/libLoam.a \
-L$PLASMA_HOME/build \
-o cpc_test01 \
-ldl -lm  -lpthread  -L/lib  -licuuc -licui18n  -lavahi-common -lavahi-client \
$OTHER_LIB/libyaml.a \
$OTHER_LIB/libboost_filesystem.a $OTHER_LIB/libboost_regex.a $OTHER_LIB/libboost_system.a \
-L/usr/local/ssl/lib -lssl -lcrypto -lrt

