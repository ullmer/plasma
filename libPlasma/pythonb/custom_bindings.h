
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "Slaw.h"
#include "Protein.h"
#include "Hose.h"
#include "Pool.h"
#include "binding_infra.h"

template <class Pybind11T = pybind11::class_<oblong::plasma::Slaw>>
struct Bind_oblong_plasma_Slaw : public pybind11_weaver::EntityBase {
    using Pybind11Type = Pybind11T;
    Pybind11Type handle;

    explicit Bind_oblong_plasma_Slaw(pybind11_weaver::EntityScope parent_h)
    : handle(parent_h, "Slaw", pybind11::dynamic_attr()) {
        handle.def(pybind11::init<const char*>());
        handle.def("ToString", [](const oblong::plasma::Slaw &s) {
            return std::string(static_cast<const char *>(s.ToString()));
        });
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
        handle.def("ToSlaw", &oblong::plasma::Protein::ToSlaw);
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
        handle.def("Next", &oblong::plasma::Hose::Next);
        handle.def("Deposit", &oblong::plasma::Hose::Deposit);
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
