#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "plasma/Slaw.h"
#include "plasma/Protein.h"

template <class Pybind11T = pybind11::class_<oblong::plasma::Slaw>>
struct Bind_oblong_plasma_Slaw : public pybind11_weaver::EntityBase {
  using Pybind11Type = Pybind11T;
  Pybind11Type handle;

  explicit Bind_oblong_plasma_Slaw(pybind11_weaver::EntityScope parent_h)
      : handle(parent_h, "Slaw", pybind11::dynamic_attr()) {
    handle.def(pybind11::init<const std::string &>());  // Adjust constructor as needed
  }

  void Update() override {}
  pybind11_weaver::EntityScope AsScope() override { return pybind11_weaver::EntityScope(handle); }

  static const char *Key() { return "oblong_plasma_Slaw"; }
};

#ifndef PB11_WEAVER_DISABLE_Entity_oblong_plasma_Slaw
using Entity_oblong_plasma_Slaw = Bind_oblong_plasma_Slaw<>;
#endif

template <class Pybind11T = pybind11::class_<oblong::plasma::Protein>>
struct Bind_oblong_plasma_Protein : public pybind11_weaver::EntityBase {
  using Pybind11Type = Pybind11T;
  Pybind11Type handle;

  explicit Bind_oblong_plasma_Protein(pybind11_weaver::EntityScope parent_h)
      : handle(parent_h, "Protein", pybind11::dynamic_attr()) {
    handle.def(pybind11::init<>());  // Adjust constructor as needed
  }

  void Update() override {}
  pybind11_weaver::EntityScope AsScope() override { return pybind11_weaver::EntityScope(handle); }

  static const char *Key() { return "oblong_plasma_Protein"; }
};

#ifndef PB11_WEAVER_DISABLE_Entity_oblong_plasma_Protein
using Entity_oblong_plasma_Protein = Bind_oblong_plasma_Protein<>;
#endif
