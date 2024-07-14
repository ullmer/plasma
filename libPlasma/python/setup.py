from setuptools   import Extension, setup
from Cython.Build import cythonize
 
sourcefiles = ["cplasma.pyx", "cplasmaWrap.c"]
extensions  = [Extension("cplasma", sourcefiles,
  libraries    = ["Plasma", "Loam", "ssl"],
  library_dirs = ["/home/ullmer/git/plasma/build/libPlasma/c",
                  "/home/ullmer/git/plasma/build/libLoam/c",
                  "/usr/local/lib"
                 ])]

setup(
  ext_modules = cythonize(extensions, build_dir="build")
)

### end ###
