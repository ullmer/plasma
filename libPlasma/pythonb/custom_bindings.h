
#ifndef CUSTOM_BINDINGS_H
#define CUSTOM_BINDINGS_H

#include "binding_infra.h"
#include "Slaw.h"
#include "Protein.h"
#include "Hose.h"
#include "Pool.h"

namespace py = pybind11;

namespace pybind11_weaver {

template <typename Pybind11T = pybind11::class_<oblong::plasma::Slaw>>
struct Bind_oblong_plasma_Slaw : public EntityBase {
    Pybind11T handle;
    explicit Bind_oblong_plasma_Slaw(EntityScope scope)
        : handle(pybind11::class_<oblong::plasma::Slaw>(scope.AsScope(), "Slaw")
            .def(pybind11::init<>())
            .def("IsNull", &oblong::plasma::Slaw::IsNull)
            .def("IsCons", &oblong::plasma::Slaw::IsCons)
            .def("Car", &oblong::plasma::Slaw::Car)
            .def("Cdr", &oblong::plasma::Slaw::Cdr)) {}
    void Update() override {}
    EntityScope AsScope() override { return EntityScope(handle); }
    static const char *Key() { return "oblong_plasma_Slaw"; }
};

template <typename Pybind11T = pybind11::class_<oblong::plasma::Protein>>
struct Bind_oblong_plasma_Protein : public EntityBase {
    Pybind11T handle;
    explicit Bind_oblong_plasma_Protein(EntityScope scope)
        : handle(pybind11::class_<oblong::plasma::Protein>(scope.AsScope(), "Protein")
            .def(pybind11::init<>())
            .def("IsNull", &oblong::plasma::Protein::IsNull)
            .def("Descrips", &oblong::plasma::Protein::Descrips)
            .def("Ingests", &oblong::plasma::Protein::Ingests)) {}
    void Update() override {}
    EntityScope AsScope() override { return EntityScope(handle); }
    static const char *Key() { return "oblong_plasma_Protein"; }
};

template <typename Pybind11T = pybind11::class_<oblong::plasma::Hose>>
struct Bind_oblong_plasma_Hose : public EntityBase {
    Pybind11T handle;
    explicit Bind_oblong_plasma_Hose(EntityScope scope)
        : handle(pybind11::class_<oblong::plasma::Hose>(scope.AsScope(), "Hose")
            .def(pybind11::init<>())
            .def("IsConfigured", &oblong::plasma::Hose::IsConfigured)
            .def("Name", &oblong::plasma::Hose::Name)
            .def("Deposit", &oblong::plasma::Hose::Deposit)
            .def("Next", &oblong::plasma::Hose::Next)) {}
    void Update() override {}
    EntityScope AsScope() override { return EntityScope(handle); }
    static const char *Key() { return "oblong_plasma_Hose"; }
};

template <typename Pybind11T = pybind11::class_<oblong::plasma::Pool>>
struct Bind_oblong_plasma_Pool : public EntityBase {
    Pybind11T handle;
    explicit Bind_oblong_plasma_Pool(EntityScope scope)
        : handle(pybind11::class_<oblong::plasma::Pool>(scope.AsScope(), "Pool")
            .def(pybind11::init<>())
            .def_static("Participate", py::overload_cast<const char *>(&oblong::plasma::Pool::Participate))
            .def_static("Create", py::overload_cast<const char *, oblong::plasma::Pool::Configuration, bool>(&oblong::plasma::Pool::Create))) {}
    void Update() override {}
    EntityScope AsScope() override { return EntityScope(handle); }
    static const char *Key() { return "oblong_plasma_Pool"; }
};

template <typename Pybind11T = pybind11::class_<std::hash<oblong::plasma::Protein>>>
struct Bind_std_hash6oblong_plasma_Protein9 : public EntityBase {
    Pybind11T handle;
    explicit Bind_std_hash6oblong_plasma_Protein9(EntityScope scope)
        : handle(pybind11::class_<std::hash<oblong::plasma::Protein>>(scope.AsScope(), "hash<oblong::plasma::Protein>")
            .def(pybind11::init<>())) {}
    void Update() override {}
    EntityScope AsScope() override { return EntityScope(handle); }
    static const char *Key() { return "std_hash6oblong_plasma_Protein9"; }
};

template <typename Pybind11T = pybind11::class_<std::hash<oblong::plasma::Slaw>>>
struct Bind_std_hash6oblong_plasma_Slaw9 : public EntityBase {
    Pybind11T handle;
    explicit Bind_std_hash6oblong_plasma_Slaw9(EntityScope scope)
        : handle(pybind11::class_<std::hash<oblong::plasma::Slaw>>(scope.AsScope(), "hash<oblong::plasma::Slaw>")
            .def(pybind11::init<>())) {}
    void Update() override {}
    EntityScope AsScope() override { return EntityScope(handle); }
    static const char *Key() { return "std_hash6oblong_plasma_Slaw9"; }
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
