cmake .. -GNinja \
  -DPYTHON_EXECUTABLE=/Applications/FreeCAD.app/Contents/Resources/bin/python \
  -DPYTHON_INCLUDE_DIR=/opt/local/Library/Frameworks/Python.framework/Versions/3.11/include/python3.11 \
  -DPYTHON_LIBRARY=/Applications/FreeCAD.app/Contents/Resources/lib/libpython3.11.dylib \
  -DPYBIND11_FINDPYTHON=OFF \
  -DCMAKE_PREFIX_PATH="/opt/local;../../build" \
  -DCMAKE_CXX_FLAGS="-I/opt/local/Library/Frameworks/Python.framework/Versions/3.11/include/python3.11"
