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
    /home/bullmer/git/plasma/
)

# Add the Python module
pybind11_add_module(plasma
    module.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/plasma_bindings.cc.inc
)

# Link any additional libraries if needed
# target_link_libraries(plasma PRIVATE your_library_name)

find_library(PLASMA_LIB plasma PATHS ../../build/libPlasma/c++)
if(PLASMA_LIB)
  target_link_libraries(plasma PRIVATE ${PLASMA_LIB})
else()
  message(FATAL_ERROR "Could not find plasma library)
endif()

target_include_directories(plasma PRIVATE ../c++)

### end ###
