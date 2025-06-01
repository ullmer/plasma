
cmake_minimum_required(VERSION 3.14)
project(plasma_bindings)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)
set(CMAKE_VERBOSE_MAKEFILE ON)

# Get user's home directory and define base project path
set(HOME_DIR $ENV{HOME})
set(GIT_BASE ${HOME_DIR}/git)
set(PLASMA_ROOT ${GIT_BASE}/plasma)

# Define subpaths
set(LOAM_C ${PLASMA_ROOT}/libLoam/c)
set(LOAM_CPP ${PLASMA_ROOT}/libLoam/c++)
set(PLASMA_C ${PLASMA_ROOT}/libPlasma/c)
set(PLASMA_CPP ${PLASMA_ROOT}/libPlasma/c++)
set(BUILD_DIR ${PLASMA_ROOT}/build)

# Include directories
include_directories(
  ${PLASMA_ROOT}
  ${PLASMA_CPP}
  ${LOAM_C}
  ${LOAM_CPP}
)

# Add the Python module
find_package(pybind11 REQUIRED)
pybind11_add_module(plasma module.cpp)

# Link OpenSSL
find_package(OpenSSL REQUIRED)
target_link_libraries(plasma PRIVATE OpenSSL::SSL OpenSSL::Crypto)

# Link ICU
find_package(ICU REQUIRED COMPONENTS uc i18n)
target_link_libraries(plasma PRIVATE ICU::uc ICU::i18n)

# Link Loam and Plasma libraries
set(LOAM_LIB ${BUILD_DIR}/libLoam/c/libLoam.a)
set(LOAMXX_LIB ${BUILD_DIR}/libLoam/c++/libLoam++.a)
set(CPLASMA_LIB ${BUILD_DIR}/libPlasma/c/libPlasma.a)
set(PLASMA_LIB ${BUILD_DIR}/libPlasma/c++/libPlasma++.a)

if(EXISTS ${PLASMA_LIB})
  target_link_libraries(plasma PRIVATE ${PLASMA_LIB})
else()
  message(FATAL_ERROR "Could not find plasma library at ${PLASMA_LIB}")
endif()

target_include_directories(plasma PRIVATE ${PLASMA_CPP})

# Link YAML manually (more reliable than pkg-config here)
find_path(YAML_INCLUDE_DIR yaml.h PATHS /opt/local/include)
find_library(YAML_LIBRARY yaml PATHS /opt/local/lib)

if(YAML_INCLUDE_DIR AND YAML_LIBRARY)
  message(STATUS "Found libyaml: ${YAML_LIBRARY}")
  target_include_directories(plasma PRIVATE ${YAML_INCLUDE_DIR})
  target_link_libraries(plasma PRIVATE ${YAML_LIBRARY})
else()
  message(FATAL_ERROR "Could not find libyaml")
endif()

# Final linking
target_link_libraries(plasma PRIVATE
  ${LOAM_LIB}
  ${LOAMXX_LIB}
  ${CPLASMA_LIB}
  ${SSL_LOCATION}
  ${CRYPTO_LOCATION}
)
