/// "create" submodule and associated types 
/// Brygg Ullmer, Clemson University
/// Initial stub by copilot

py::module_ create = m.def_submodule("create", "Factory functions for libPlasma types");

create.def("int32", [](int a) {
   int32 i = static_cast<int32>(a);
   return oblong::plasma::Slaw(i);
}, "Create a Slaw-wrapped int32 from an integer");

create.def("v2int8", [](int a, int b) {
   v2int8 vec = {static_cast<int8>(a), static_cast<int8>(b)};
   return oblong::plasma::Slaw(vec);
}, "Create a Slaw-wrapped v2int8 from two integers");

create.def("v2int32", [](int a, int b) {
   v2int32 vec = {static_cast<int32>(a), static_cast<int32>(b)};
   return oblong::plasma::Slaw(vec);
}, "Create a Slaw-wrapped v2int32 from two integers");

create.def("list", [](py::list plist) { // body from Slaw.h::664-670
  std::vector<oblong::plasma::Slaw> vsl;
  oblong::plasma::Slaw s;
  for (int i = 0; i < plist.size(); i++) {
    s = plist[i].cast<oblong::plasma::Slaw>(); 
    vsl.push_back(s);
  }
  oblong::plasma::Slaw list = oblong::plasma::Slaw::ListCollect (
                                           vsl.begin(), vsl.end());
  return list;
}, "Create a Slaw-wrapped List from a Python list of arbitrary length");

/// end ///

