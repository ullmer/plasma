cmake .. -GNinja \
  -DPython3_EXECUTABLE=/Applications/FreeCAD.app/Contents/Resources/bin/python \
  -DPython3_INCLUDE_DIR=/opt/local/Library/Frameworks/Python.framework/Versions/3.11/include/python3.11 \
  -DPython3_LIBRARY=/Applications/FreeCAD.app/Contents/Resources/lib/libpython3.11.dylib \
  -DCMAKE_PREFIX_PATH="/opt/local;../../build"
