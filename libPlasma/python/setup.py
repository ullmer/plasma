from setuptools   import Extension, setup
from Cython.Build import cythonize
 
sourcefiles = ["cplasma.pyx", "cplasma.c", "cplasma.h", "slaw.h", "pool_cmd.h"]
extensions  = [Extension("cplasma", sourcefiles)]

setup(
  ext_modules = cythonize(extensions, build_dir="build")
)

### end ###
