//plasma.create-specific bindings

    handle.def("as_v2int32",  {
      return s.Emit<v2int32>();
    });
    handle.def("as_v3int32",  {
      return s.Emit<v3int32>();
    });
    handle.def("as_v4int32",  {
      return s.Emit<v4int32>();
    });

    handle.def("__getitem__",  {
      if (s.CanEmit<v2int32>()) {
        auto vec = s.Emit<v2int32>();
        if (index == 0) return Slaw(vec.x);
        if (index == 1) return Slaw(vec.y);
        throw py::index_error("v2int32 index out of range");
      }
      if (s.CanEmit<v3int32>()) {
        auto vec = s.Emit<v3int32>();
        if (index == 0) return Slaw(vec.x);
        if (index == 1) return Slaw(vec.y);
        if (index == 2) return Slaw(vec.z);
        throw py::index_error("v3int32 index out of range");
      }
      if (s.CanEmit<v4int32>()) {
        auto vec = s.Emit<v4int32>();
        if (index == 0) return Slaw(vec.x);
        if (index == 1) return Slaw(vec.y);
        if (index == 2) return Slaw(vec.z);
        if (index == 3) return Slaw(vec.w);
        throw py::index_error("v4int32 index out of range");
      }
      if (s.IsList() || s.IsArray()) {
        if (index >= static_cast<size_t>(s.Count()))
          throw py::index_error("Slaw index out of range");
        return s.Nth(index);
      }
      throw py::type_error("Unsupported Slaw type for indexing");
    });

    handle.def("Find", static_cast<Slaw (Slaw::*)(const Slaw &) const>(&Slaw::Find));
    handle.def("__getitem__",  {
      return s.Find(key);
    });

    handle.def_static("List",  { return Slaw::List(); });
    handle.def_static("List",  { return Slaw::List(s); });
    handle.def_static("Map",  {
      return Slaw::Map(k, v);
    });
    handle.def_static("Cons",  {
      return Slaw::Cons(car, cdr);
    });
  }

  void Update() override {}
  pybind11_weaver::EntityScope AsScope() override {
    return pybind11_weaver::EntityScope(handle);
  }
  static const char *Key() { return "oblong_plasma_Slaw"; }
};

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

