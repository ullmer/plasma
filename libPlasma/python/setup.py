from setuptools   import Extension, setup
from Cython.Build import cythonize
 
sourcefiles = ["cplasma.pyx", "cplasma.c", "cplasma.h", "slaw.h", "pool_cmd.h"]
extensions  = [Extension("cplasma", sourcefiles)]

#module  = Extension("temp", "temp.pyx")
#module.cython_c_in_temp = True 

setup(
  ext_modules = cythonize(extensions, build_dir="build/cython")
)

### end ###
