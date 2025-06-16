//plasma.create-specific bindings

handle.def("as_v2int32",  [](const oblong::plasma::Slaw &s){ return s.Emit<v2int32>(); });
handle.def("as_v3int32",  [](const oblong::plasma::Slaw &s){ return s.Emit<v3int32>(); });
handle.def("as_v4int32",  [](const oblong::plasma::Slaw &s){ return s.Emit<v4int32>(); });

/*
    handle.def("__getitem__",  [](const oblong::plasma::Slaw &s, 
                                                    unsigned  gindex) {
      if (s.CanEmit<v2int32>()) {
        auto vec = s.Emit<v2int32>();
        if (gindex == 0) return vec.x;
        if (gindex == 1) return vec.y;
        throw py::index_error("v2int32 index out of range");
      }
      if (s.CanEmit<v3int32>()) {
        auto vec = s.Emit<v3int32>();
        if (gindex == 0) return vec.x;
        if (gindex == 1) return vec.y;
        if (gindex == 2) return vec.z;
        throw py::index_error("v3int32 index out of range");
      }
      if (s.CanEmit<v4int32>()) {
        auto vec = s.Emit<v4int32>();
        if (gindex == 0) return vec.x;
        if (gindex == 1) return vec.y;
        if (gindex == 2) return vec.z;
        if (gindex == 3) return vec.w;
        throw py::index_error("v4int32 index out of range");
      }
      if (s.IsList() || s.IsArray()) {
        if (gindex >= static_cast<size_t>(s.Count()))
          throw py::index_error("Slaw index out of range");
        return s.Nth(gindex);
      }
      throw py::type_error("Unsupported Slaw type for indexing");
    });
*/

/// end ///
