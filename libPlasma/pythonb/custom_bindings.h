
#ifndef CUSTOM_BINDINGS_H
#define CUSTOM_BINDINGS_H

#include "binding_infra.h"
#include "Slaw.h"
#include "Protein.h"
#include "Hose.h"
#include "Pool.h"

namespace pybind11_weaver {

template <typename Pybind11T = pybind11::module_>
struct Bind_oblong : public EntityBase {
    Pybind11T handle;
    explicit Bind_oblong(EntityScope scope)
        : handle(scope.AsScope().def_submodule("oblong")) {}
    void Update() override {}
    EntityScope AsScope() override { return EntityScope(handle); }
    static const char *Key() { return "oblong"; }
};

template <typename Pybind11T = pybind11::module_>
struct Bind_oblong_plasma : public EntityBase {
    Pybind11T handle;
    explicit Bind_oblong_plasma(EntityScope scope)
        : handle(scope.AsScope().def_submodule("plasma")) {}
    void Update() override {}
    EntityScope AsScope() override { return EntityScope(handle); }
    static const char *Key() { return "oblong_plasma"; }
};

template <typename Pybind11T = pybind11::module_>
struct Bind_oblong_plasma_OStreamReference : public EntityBase {
    Pybind11T handle;
    explicit Bind_oblong_plasma_OStreamReference(EntityScope scope)
        : handle(scope.AsScope().def_submodule("OStreamReference")) {}
    void Update() override {}
    EntityScope AsScope() override { return EntityScope(handle); }
    static const char *Key() { return "oblong_plasma_OStreamReference"; }
};

template <typename Pybind11T = pybind11::module_>
struct Bind_std : public EntityBase {
    Pybind11T handle;
    explicit Bind_std(EntityScope scope)
        : handle(scope.AsScope().def_submodule("std")) {}
    void Update() override {}
    EntityScope AsScope() override { return EntityScope(handle); }
    static const char *Key() { return "std"; }
};

template <typename Pybind11T = pybind11::class_<oblong::plasma::Slaw>>
struct Bind_oblong_plasma_Slaw {
    static const char *Key() { return "oblong_plasma_Slaw"; }
    Bind_oblong_plasma_Slaw(EntityScope scope) {
        auto handle = scope
            .attr("Slaw")
            .def(pybind11::init<>())
            .def("IsNull", &oblong::plasma::Slaw::IsNull)
            .def("IsCons", &oblong::plasma::Slaw::IsCons)
            .def("Car", &oblong::plasma::Slaw::Car)
            .def("Cdr", &oblong::plasma::Slaw::Cdr);
        TryAddDefaultCtor(handle);
    }
};

template <typename Pybind11T = pybind11::class_<oblong::plasma::Protein>>
struct Bind_oblong_plasma_Protein {
    static const char *Key() { return "oblong_plasma_Protein"; }
    Bind_oblong_plasma_Protein(EntityScope scope) {
        auto handle = scope
            .attr("Protein")
            .def(pybind11::init<>())
            .def("IsNull", &oblong::plasma::Protein::IsNull)
            .def("Descrips", &oblong::plasma::Protein::Descrips)
            .def("Ingests", &oblong::plasma::Protein::Ingests);
        TryAddDefaultCtor(handle);
    }
};

template <typename Pybind11T = pybind11::class_<oblong::plasma::Hose>>
struct Bind_oblong_plasma_Hose {
    static const char *Key() { return "oblong_plasma_Hose"; }
    Bind_oblong_plasma_Hose(EntityScope scope) {
        auto handle = scope
            .attr("Hose")
            .def(pybind11::init<>())
            .def("IsNull", &oblong::plasma::Hose::IsNull)
            .def("Name", &oblong::plasma::Hose::Name)
            .def("Open", &oblong::plasma::Hose::Open)
            .def("Close", &oblong::plasma::Hose::Close);
        TryAddDefaultCtor(handle);
    }
};

template <typename Pybind11T = pybind11::class_<oblong::plasma::Pool>>
struct Bind_oblong_plasma_Pool {
    static const char *Key() { return "oblong_plasma_Pool"; }
    Bind_oblong_plasma_Pool(EntityScope scope) {
        auto handle = scope
            .attr("Pool")
            .def(pybind11::init<>())
            .def("IsNull", &oblong::plasma::Pool::IsNull)
            .def("Name", &oblong::plasma::Pool::Name)
            .def("Open", &oblong::plasma::Pool::Open)
            .def("Close", &oblong::plasma::Pool::Close);
        TryAddDefaultCtor(handle);
    }
};

template <typename Pybind11T = pybind11::class_<std::hash<oblong::plasma::Protein>>>
struct Bind_std_hash6oblong_plasma_Protein9 {
    static const char *Key() { return "std_hash6oblong_plasma_Protein9"; }
    Bind_std_hash6oblong_plasma_Protein9(EntityScope scope) {
        auto handle = scope
            .attr("hash<oblong::plasma::Protein>")
            .def(pybind11::init<>());
        TryAddDefaultCtor(handle);
    }
};

template <typename Pybind11T = pybind11::class_<std::hash<oblong::plasma::Slaw>>>
struct Bind_std_hash6oblong_plasma_Slaw9 {
    static const char *Key() { return "std_hash6oblong_plasma_Slaw9"; }
    Bind_std_hash6oblong_plasma_Slaw9(EntityScope scope) {
        auto handle = scope
            .attr("hash<oblong::plasma::Slaw>")
            .def(pybind11::init<>());
        TryAddDefaultCtor(handle);
    }
};

using Entity_oblong = Bind_oblong<>;
using Entity_oblong_plasma = Bind_oblong_plasma<>;
using Entity_oblong_plasma_OStreamReference = Bind_oblong_plasma_OStreamReference<>;
using Entity_std = Bind_std<>;
using Entity_std_hash6oblong_plasma_Protein9 = Bind_std_hash6oblong_plasma_Protein9<>;
using Entity_std_hash6oblong_plasma_Slaw9 = Bind_std_hash6oblong_plasma_Slaw9<>;

[[nodiscard]] CallUpdateGuard DeclFn(pybind11::module &m, const CustomBindingRegistry &registry) {
    auto v0 = CreateEntity<Entity_oblong>(EntityScope(m), registry);
    auto v1 = CreateEntity<Entity_oblong_plasma>(v0->AsScope(), registry);
    auto v2 = CreateEntity<Entity_oblong_plasma_OStreamReference>(v1->AsScope(), registry);
    auto v3 = CreateEntity<Entity_std>(EntityScope(m), registry);
    auto v4 = CreateEntity<Entity_std_hash6oblong_plasma_Protein9>(v3->AsScope(), registry);
    auto v5 = CreateEntity<Entity_std_hash6oblong_plasma_Slaw9>(v3->AsScope(), registry);
    auto update_fn = [=]() {
        v0->Update();
        v1->Update();
        v2->Update();
        v3->Update();
        v4->Update();
        v5->Update();
    };
    return {update_fn};
}

} // namespace pybind11_weaver

#endif // CUSTOM_BINDINGS_H
