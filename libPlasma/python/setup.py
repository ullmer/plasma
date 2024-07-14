from setuptools   import Extension, setup
from Cython.Build import cythonize

setup(
  ext_modules = cythonize([Extension("cplasma_cython", ["cplasma_cython.pyx"])])
)

### end ###
