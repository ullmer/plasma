/// "create" submodule and associated types 
/// Brygg Ullmer, Clemson University
/// Initial stub by copilot

py::module_ create = m.def_submodule("create", "Factory functions for libPlasma types");

create.def("v2int32", [](int a, int b) {
   v2int32 vec = {static_cast<int32>(a), static_cast<int32>(b)};
   return oblong::plasma::Slaw(vec);
}, "Create a Slaw-wrapped v2int32 from two integers");

create.def("int32", [](int a) {
   int32 i = static_cast<int32>(a);
   return oblong::plasma::Slaw(i);
}, "Create a Slaw-wrapped int32 from an integer");

create.def("list", [](py::list plist) { 
  int plen = plist.size();
  switch (plen) { //initially hacked very embarassingly
    case 1: {
      oblong::plasma::Slaw el0 = plist[0].cast<oblong::plasma::Slaw>();
      return oblong::plasma::Slaw::List(el0);
    }
    case 2: {
      oblong::plasma::Slaw el0 = plist[0].cast<oblong::plasma::Slaw>();
      oblong::plasma::Slaw el1 = plist[1].cast<oblong::plasma::Slaw>();
      return oblong::plasma::Slaw::List(el0, el1);
    }
    default: return oblong::plasma::Slaw::List();
  }
}, "Create a Slaw-wrapped List from a python list");

/// end ///
