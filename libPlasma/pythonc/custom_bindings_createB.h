#ifndef PB11_WEAVER_DISABLE_Entity_oblong_plasma_Slaw
using Entity_oblong_plasma_Slaw = Bind_oblong_plasma_Slaw<>;
#endif
// Bind vector types
inline void Bind_VectorTypes(py::module_ &m) {
  py::class_<v2int32>(m, "v2int32")
    .def(py::init<>())
    .def_readwrite("x", &v2int32::x)
    .def_readwrite("y", &v2int32::y)
    .def("__repr__",  {
      return "<v2int32 x=" + std::to_string(v.x) + ", y=" + std::to_string(v.y) + ">";
    });

  py::class_<v3int32>(m, "v3int32")
    .def(py::init<>())
    .def_readwrite("x", &v3int32::x)
    .def_readwrite("y", &v3int32::y)
    .def_readwrite("z", &v3int32::z)
    .def("__repr__",  {
      return "<v3int32 x=" + std::to_string(v.x) + ", y=" + std::to_string(v.y) + ", z=" + std::to_string(v.z) + ">";
    });

  py::class_<v4int32>(m, "v4int32")
    .def(py::init<>())
    .def_readwrite("x", &v4int32::x)
    .def_readwrite("y", &v4int32::y)
    .def_readwrite("z", &v4int32::z)
    .def_readwrite("w", &v4int32::w)
    .def("__repr__",  {
      return "<v4int32 x=" + std::to_string(v.x) + ", y=" + std::to_string(v.y) +
             ", z=" + std::to_string(v.z) + ", w=" + std::to_string(v.w) + ">";
    });
}

