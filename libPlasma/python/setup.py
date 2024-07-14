from setuptools   import Extension, setup
from Cython.Build import cythonize
 
sourcefiles = ["cplasma.pyx", "cplasmaWrap.c"]
extensions  = [Extension("cplasma", sourcefiles)]

setup(
  ext_modules = cythonize(extensions, build_dir="build")
)

### end ###
