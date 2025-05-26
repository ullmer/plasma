# This is the last subdirectory included by the
# top level CMakeLists.txt, so the tests it
# adds come last.

# FindPlasma.cmake is a legacy file; new apps should use samples/FindOblong.cmake
#configure_file(FindPlasma.cmake.in "${plasma_BINARY_DIR}/FindPlasma.cmake" @ONLY)
configure_file(FindPlasma.cmake.in "${plasma_BINARY_DIR}/FindPlasma.cmake" @ONLY)

#  FILES ${plasma_BINARY_DIR}/FindPlasma.cmake
install(
  FILES ${plasma_BINARY_DIR}/FindPlasma.cmake
        ObCheckCFlags.cmake
        ObCheckCxxFlags.cmake
        ObBoilerplate.cmake
        ObCommonOpts.cmake
        ObFindLibs.cmake
        ObGeneratePC.cmake
        ObGenerateProject.cmake
        ObGetSettings.cmake
  DESTINATION lib/cmake
)

#---- begin debian alternatives magic for cmake ----
# When cmake sees 'find_package(Oblong)', it evaluates
# ../lib/cmake/Oblong/OblongConfig.cmake 
# from each directory in PATH.  
# In Ubuntu, we register symlinks in /usr/bin for peek, poke, etc., and
# a symlink in /usr/lib/cmake for OblongConfig.cmake.
# See ../../debian/oblong-loam4.3.postinst
# OblongConfig.cmake just includes $PLASMA_HOME/src/FindOblong.cmake.
configure_file(Oblong/OblongConfig.cmake.in "${plasma_BINARY_DIR}/OblongConfig.cmake" @ONLY)
install(
  FILES ${plasma_BINARY_DIR}/OblongConfig.cmake
  DESTINATION lib/cmake/Oblong
)
#---- end debian alternatives magic for cmake ----

IF(EXISTS "${plasma_SOURCE_DIR}/.git/config")
  # This test should be the last one run, so it can check that configure,
  # build, and test did not leave files behind that are not ignored by
  # .gitignore.
  add_test(
    NAME diffGitStatusTest
    COMMAND "${SHELL}" "${plasma_SOURCE_DIR}/bld/cmake/diff-git-status-test.sh" "test" "${plasma_BINARY_DIR}"
    WORKING_DIRECTORY "${plasma_SOURCE_DIR}"
  )
ENDIF()

