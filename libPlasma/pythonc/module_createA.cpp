/// "create" submodule and associated types
/// Brygg Ullmer, Clemson University
/// Initial stub by copilot

py::module_ create = m.def_submodule("create", "Factory functions for libPlasma types");

create.def("v2int32", [](int a, int b) {
  v2int32 vec = {static_cast<int32>(a), static_cast<int32>(b)};
  return oblong::plasma::Slaw(vec);

py::class_<v2int32>(m, "v2int32")
    .def(py::init<>())
    .def_readwrite("x", &v2int32::x)
    .def_readwrite("y", &v2int32::y)
    .def("__repr__",  {
        return "<v2int32 x=" + std::to_string(v[0]) + ", y=" + std::to_string(v[1]) + ">";
//        return "<v2int32 x=" + std::to_string(v.x) + ", y=" + std::to_string(v.y) + ">";
    });


}, "Create a Slaw-wrapped v2int32 from two integers");

//   oblong::plasma::v2int32 vec = {static_cast<oblong::plasma::int32>(a),
//                                  static_cast<oblong::plasma::int32>(b)};

/// end ///
