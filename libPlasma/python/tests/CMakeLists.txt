# /* (c)  oblong industries */

project(PlasmaTests C CXX)

set(
  PlasmaTests_TESTS

  cpc_test01
)

set(SUFFIX "c")
foreach( test ${PlasmaTests_MANUAL_C_TESTS} )
   add_executable(${test} ${test}.${SUFFIX})
   target_link_libraries(${test} Plasma)
endforeach()
