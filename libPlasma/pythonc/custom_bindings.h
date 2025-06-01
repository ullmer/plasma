
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "Slaw.h"
#include "Protein.h"
#include "Hose.h"
#include "Pool.h"

namespace pybind11_weaver { // forward declaration
struct EntityScope;
struct EntityBase;
}

template <class Pybind11T = pybind11::class_<oblong::plasma::Slaw>>
struct Bind_oblong_plasma_Slaw : public pybind11_weaver::EntityBase {
    using Pybind11Type = Pybind11T;
    Pybind11Type handle;

    explicit Bind_oblong_plasma_Slaw(pybind11_weaver::EntityScope parent_h)
    : handle(parent_h, "Slaw", pybind11::dynamic_attr()) {
        handle.def(pybind11::init<const char*>());
        handle.def("IsList",  &oblong::plasma::Slaw::IsList);
        handle.def("IsMap",   &oblong::plasma::Slaw::IsMap);
        handle.def("Count",   &oblong::plasma::Slaw::Count);
        handle.def("Nth",     &oblong::plasma::Slaw::Nth);
        handle.def("MapKeys", &oblong::plasma::Slaw::MapKeys);
        handle.def("Keys",    &oblong::plasma::Slaw::MapKeys); //more pythonic

        //handle.def_static("List", pybind11::overload_cast<slaw>(&Slaw::List));
        //handle.def_static("Map",  pybind11::overload_cast<slaw, slaw>(&Slaw::Map));

        handle.def_static("List",  [](const oblong::plasma::Slaw &s){return oblong::plasma::Slaw::List(s); });
        handle.def_static("Map",   [](const oblong::plasma::Slaw &k, oblong::plasma::Slaw v){
                           return oblong::plasma::Slaw::Map(k, v); });
        handle.def_static("Cons",  [](const oblong::plasma::Slaw &car, const oblong::plasma::Slaw &cdr){
                           return oblong::plasma::Slaw::Cons(car, cdr); });

        handle.def("Find", static_cast<oblong::plasma::Slaw (oblong::plasma::Slaw::*)(const oblong::plasma::Slaw &) const>
			     (&oblong::plasma::Slaw::Find));

        handle.def("__getitem__", [](const oblong::plasma::Slaw &s, const oblong::plasma::Slaw &key) {
          return s.Find(key); });

        handle.def("ToString",    [](const oblong::plasma::Slaw &s) {
            return std::string(static_cast<const char *>(s.ToString())); });
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
        handle.def(pybind11::init<>());
        handle.def(pybind11::init<oblong::plasma::Slaw>());
        handle.def(pybind11::init<oblong::plasma::Slaw, oblong::plasma::Slaw>());
        handle.def("ToSlaw",   &oblong::plasma::Protein::ToSlaw);
        handle.def("IsNull",   &oblong::plasma::Protein::IsNull);
        handle.def("Descrips", &oblong::plasma::Protein::Descrips);
        handle.def("Ingests",  &oblong::plasma::Protein::Ingests);

    }

    void Update() override {}
    pybind11_weaver::EntityScope AsScope() override { return pybind11_weaver::EntityScope(handle); }

    static const char *Key() { return "oblong_plasma_Protein"; }
};

#ifndef PB11_WEAVER_DISABLE_Entity_oblong_plasma_Protein
using Entity_oblong_plasma_Protein = Bind_oblong_plasma_Protein<>;
#endif

template <class Pybind11T = pybind11::class_<oblong::plasma::Hose>>
struct Bind_oblong_plasma_Hose : public pybind11_weaver::EntityBase {
    using Pybind11Type = Pybind11T;
    Pybind11Type handle;

    explicit Bind_oblong_plasma_Hose(pybind11_weaver::EntityScope parent_h)
    : handle(parent_h, "Hose", pybind11::dynamic_attr()) {
        handle.def(pybind11::init<const oblong::loam::Str&>());
        //handle.def(pybind11::init<oblong::plasma::pool_hose>());
        // 	handle.def(pybind11::init<pool_hose>());

        handle.def("Next",     &oblong::plasma::Hose::Next);
        handle.def("Deposit",  &oblong::plasma::Hose::Deposit);
        handle.def("Withdraw", &oblong::plasma::Hose::Withdraw);
    }

    void Update() override {}
    pybind11_weaver::EntityScope AsScope() override { return pybind11_weaver::EntityScope(handle); }

    static const char *Key() { return "oblong_plasma_Hose"; }
};

#ifndef PB11_WEAVER_DISABLE_Entity_oblong_plasma_Hose
using Entity_oblong_plasma_Hose = Bind_oblong_plasma_Hose<>;
#endif

template <class Pybind11T = pybind11::class_<oblong::plasma::Pool, std::unique_ptr<oblong::plasma::Pool, pybind11::nodelete>>>
struct Bind_oblong_plasma_Pool : public pybind11_weaver::EntityBase {
    using Pybind11Type = Pybind11T;
    Pybind11Type handle;

    explicit Bind_oblong_plasma_Pool(pybind11_weaver::EntityScope parent_h)
    : handle(parent_h, "Pool", pybind11::dynamic_attr()) {
        handle.def_static("Participate", pybind11::overload_cast<const char*, oblong::loam::ObRetort*>(&oblong::plasma::Pool::Participate), pybind11::return_value_policy::reference);
        handle.def_static("Participate", [](const char* name) { return oblong::plasma::Pool::Participate(name, nullptr); }, pybind11::return_value_policy::reference);
        handle.def_static("Create", pybind11::overload_cast<const char*, oblong::plasma::PoolType, bool, oblong::plasma::Protein>(&oblong::plasma::Pool::Create));
        handle.def_static("Dispose", &oblong::plasma::Pool::Dispose);
    }

    void Update() override {}
    pybind11_weaver::EntityScope AsScope() override { return pybind11_weaver::EntityScope(handle); }

    static const char *Key() { return "oblong_plasma_Pool"; }
};

#ifndef PB11_WEAVER_DISABLE_Entity_oblong_plasma_Pool
using Entity_oblong_plasma_Pool = Bind_oblong_plasma_Pool<>;
#endif

template <class Pybind11T = pybind11::class_<oblong::loam::ObRetort>>
struct Bind_oblong_loam_ObRetort : public pybind11_weaver::EntityBase {
  using Pybind11Type = Pybind11T;
  Pybind11Type handle;

  explicit Bind_oblong_loam_ObRetort(pybind11_weaver::EntityScope parent_h)
      : handle(parent_h, "ObRetort", pybind11::dynamic_attr()) {
    handle.def("IsError", &oblong::loam::ObRetort::IsError);
    handle.def("Code", &oblong::loam::ObRetort::Code);
    handle.def("Description", &oblong::loam::ObRetort::Description);
  }

  void Update() override {}
  pybind11_weaver::EntityScope AsScope() override {
    return pybind11_weaver::EntityScope(handle);
  }
  static const char *Key() { return "oblong_loam_ObRetort"; }
};

#ifndef PB11_WEAVER_DISABLE_Entity_oblong_loam_ObRetort
using Entity_oblong_loam_ObRetort = Bind_oblong_loam_ObRetort<>;
#endif

