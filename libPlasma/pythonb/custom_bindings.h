
#ifndef CUSTOM_BINDINGS_CLEANED_H
#define CUSTOM_BINDINGS_CLEANED_H

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "binding_infra.h"
#include "Protein.h"
#include "Slaw.h"

namespace py = pybind11;

namespace pybind11_weaver {

struct Bind_oblong_plasma_Slaw : public EntityBase {
    using Pybind11Type = py::class_<oblong::plasma::Slaw>;
    Pybind11Type handle;

    static const char* Key() { return "oblong_plasma_Slaw"; }

    explicit Bind_oblong_plasma_Slaw(EntityScope scope)
        : handle(scope.Get(), "Slaw") {
        handle
            .def(py::init<>())
            .def("IsNull", &oblong::plasma::Slaw::IsNull)
            .def("IsCons", &oblong::plasma::Slaw::IsCons)
            .def("Car", &oblong::plasma::Slaw::Car)
            .def("Cdr", &oblong::plasma::Slaw::Cdr);
        TryAddDefaultCtor<oblong::plasma::Slaw>(handle);
    }

    void Update() override {}
    EntityScope AsScope() override { return EntityScope(handle); }
};

struct Bind_oblong_plasma_Protein : public EntityBase {
    using Pybind11Type = py::class_<oblong::plasma::Protein>;
    Pybind11Type handle;

    static const char* Key() { return "oblong_plasma_Protein"; }

    explicit Bind_oblong_plasma_Protein(EntityScope scope)
        : handle(scope.Get(), "Protein") {
        handle
            .def(py::init<>())
            .def("IsNull", &oblong::plasma::Protein::IsNull)
            .def("IsEmpty", &oblong::plasma::Protein::IsEmpty)
            .def("Descrips", &oblong::plasma::Protein::Descrips)
            .def("Ingests", &oblong::plasma::Protein::Ingests);
        TryAddDefaultCtor<oblong::plasma::Protein>(handle);
    }

    void Update() override {}
    EntityScope AsScope() override { return EntityScope(handle); }
};

struct Bind_std_hash6oblong_plasma_Protein9 : public EntityBase {
    using Pybind11Type = py::class_<std::hash<oblong::plasma::Protein>>;
    Pybind11Type handle;

    static const char* Key() { return "std_hash6oblong_plasma_Protein9"; }

    explicit Bind_std_hash6oblong_plasma_Protein9(EntityScope scope)
        : handle(scope.Get(), "hash<oblong::plasma::Protein>") {
        TryAddDefaultCtor<std::hash<oblong::plasma::Protein>>(handle);
    }

    void Update() override {}
    EntityScope AsScope() override { return EntityScope(handle); }
};

struct Bind_std_hash6oblong_plasma_Slaw9 : public EntityBase {
    using Pybind11Type = py::class_<std::hash<oblong::plasma::Slaw>>;
    Pybind11Type handle;

    static const char* Key() { return "std_hash6oblong_plasma_Slaw9"; }

    explicit Bind_std_hash6oblong_plasma_Slaw9(EntityScope scope)
        : handle(scope.Get(), "hash<oblong::plasma::Slaw>") {
        TryAddDefaultCtor<std::hash<oblong::plasma::Slaw>>(handle);
    }

    void Update() override {}
    EntityScope AsScope() override { return EntityScope(handle); }
};

[[nodiscard]] CallUpdateGuard DeclFn(py::module &m, const CustomBindingRegistry &registry) {
    _PointerWrapperBase::FastBind(m);

    auto v0 = CreateEntity<Bind_oblong_plasma_Slaw>(EntityScope(m), registry);
    auto v1 = CreateEntity<Bind_oblong_plasma_Protein>(v0->AsScope(), registry);
    auto v2 = CreateEntity<Bind_std_hash6oblong_plasma_Protein9>(v1->AsScope(), registry);
    auto v3 = CreateEntity<Bind_std_hash6oblong_plasma_Slaw9>(v1->AsScope(), registry);

    auto update_fn = [=]() {
        v0->Update();
        v1->Update();
        v2->Update();
        v3->Update();
    };
    return {update_fn};
}

} // namespace pybind11_weaver

#endif // CUSTOM_BINDINGS_CLEANED_H
