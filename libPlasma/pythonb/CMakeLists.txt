cmake_minimum_required(VERSION 3.14)
project(plasma_bindings)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# Find pybind11
find_package(pybind11 REQUIRED)

# Include directories from your config
include_directories(
  /home/bullmer/git/plasma/libPlasma/c++/
  /home/bullmer/git/plasma/libLoam/
  /home/bullmer/git/plasma/libLoam/c/
  /home/bullmer/git/plasma/libLoam/c++/
  /home/bullmer/git/plasma/
)

# Add the Python module (no longer includes the weaver-generated .inc)
pybind11_add_module(plasma
  module.cpp
  #custom_bindings.h
  #binding_infra.h
)

# Link OpenSSL
find_package(OpenSSL REQUIRED)
target_link_libraries(plasma PRIVATE OpenSSL::SSL OpenSSL::Crypto)

# Link Loam and Plasma libraries
set(LOAM_LIB /home/bullmer/git/plasma/build/libLoam/c/libLoam.a)
target_link_libraries(plasma PRIVATE ${LOAM_LIB})

set(CPLASMA_LIB /home/bullmer/git/plasma/build/libPlasma/c/libPlasma.a)
set(PLASMA_LIB /home/bullmer/git/plasma/build/libPlasma/c++/libPlasma++.a)
find_library(PLASMA_LIB plasma PATHS /home/bullmer/git/plasma/build/libPlasma/c++)

if(PLASMA_LIB)
  target_link_libraries(plasma PRIVATE ${PLASMA_LIB})
else()
  message(FATAL_ERROR "Could not find plasma library")
endif()

target_include_directories(plasma PRIVATE ../c++)

# Verbose output and diagnostics
get_target_property(SSL_LOCATION OpenSSL::SSL IMPORTED_LOCATION)
get_target_property(CRYPTO_LOCATION OpenSSL::Crypto IMPORTED_LOCATION)
target_link_libraries(plasma PRIVATE
  ${LOAM_LIB}
  ${CPLASMA_LIB}
  ${PLASMA_LIB}
  ${SSL_LOCATION}
  ${CRYPTO_LOCATION}
)

message(STATUS "OpenSSL::SSL location: ${SSL_LOCATION}")
message(STATUS "OpenSSL::Crypto location: ${CRYPTO_LOCATION}")

set(CMAKE_VERBOSE_MAKEFILE ON)
