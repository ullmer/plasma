from setuptools   import Extension, setup
from Cython.Build import cythonize

#PLASMA_HOME = "/home/bullmer/git/plasma/"
PLASMA_HOME = "/home/ullmer/git/plasma/"
#PLASMA_HOME = "/home/brygg/git/plasma/"
WSL2_LIBD   = "/usr/lib/x86_64-linux-gnu"
RPI_LIBD    = "/usr/lib/aarch64-linux-gnu"
UB_LIBD     = "/usr/local/anaconda3/lib"

OTHER_LIB  = RPI_LIBD
#OTHER_LIB = UB_LIBD
#OTHER_LIB = WSL2_LIBD

SSL_LIBD    = "/usr/local/lib"
 
sourcefiles    = ["cplasma.pyx", "cplasmaWrap.c"]

extensions  = [Extension("cplasma", sourcefiles,
  libraries    = ["Plasma", "Loam", "ssl", "crypto", "yaml", "boost_filesystem", "boost_regex", "boost_system"],
  library_dirs = [PLASMA_HOME + "build/libPlasma/c", PLASMA_HOME + "build/libLoam/c", SSL_LIBD, OTHER_LIB],
  include_dirs = [PLASMA_HOME, PLASMA_HOME+"/libPlasma/c", PLASMA_HOME+"libLoam/c"],
  extra_compile_args = ["-fPIC"],
  extra_link_args    = ["-fPIC"],
  compile_args       = ["-fPIC"], #this is likely ignored
  link_args          = ["-fPIC"]  #this is likely ignored
                 )]

setup(
  ext_modules = cythonize(extensions, build_dir="build")
)

### end ###
