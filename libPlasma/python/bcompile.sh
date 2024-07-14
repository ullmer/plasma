PLASMA_HOME=/home/bullmer/git/plasma

gcc -c -I$PLASMA_HOME/libPlasma/c/ -I$PLASMA_HOME -DABS_TOP_SRCDIR=\"$PLASMA_HOME\" -g cplasma-cython.c 
