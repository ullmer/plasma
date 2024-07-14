from setuptools   import Extension, setup
from Cython.Build import cythonize
 
sourcefiles = ["cplasma.pyx", "cplasmaWrap.c"]
extensions  = [Extension("cplasma", sourcefiles,
  libraries    = ["libPlasma"],
  library_dirs = ["/home/bullmer/git/plasma/build/libPlasma/c/"])]

setup(
  ext_modules = cythonize(extensions, build_dir="build")
)

### end ###
