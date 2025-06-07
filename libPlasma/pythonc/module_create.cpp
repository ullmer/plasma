/// "create" submodule and associated types 
/// Brygg Ullmer, Clemson University
/// Initial stub by copilot

py::module_ create = m.def_submodule("create", "Factory functions for libPlasma types");

create.def("v2int32", [](int a, int b) {
   v2int32 vec = {static_cast<int32>(a),
                                  static_cast<int32>(b)};
   return oblong::plasma::Slaw(vec);
}, "Create a Slaw-wrapped v2int32 from two integers");

//   oblong::plasma::v2int32 vec = {static_cast<oblong::plasma::int32>(a),
//                                  static_cast<oblong::plasma::int32>(b)};

/// end ///
