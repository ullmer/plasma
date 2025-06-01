
#include <pybind11/pybind11.h>
#include "Slaw.h"
#include "Protein.h"

//Include the generated bindings
#include "plasma_bindings.cc.inc"

// Include your custom bindings
#include "custom_bindings.h"

namespace py = pybind11;
using namespace oblong::plasma;


void AddCustomEntities(pybind11::module_ &m, const pybind11_weaver::CustomBindingRegistry &registry) {
    using namespace pybind11_weaver;

    pybind11::object oblong_mod = m.attr("oblong");
    pybind11::object plasma_mod = oblong_mod.attr("plasma");

    EntityScope plasma_scope(static_cast<pybind11::detail::generic_type&>(plasma_mod));
    CreateEntity<Entity_oblong_plasma_Hose>(plasma_scope, registry)->Update();
    CreateEntity<Entity_oblong_plasma_Pool>(plasma_scope, registry)->Update();
}


PYBIND11_MODULE(plasma, m) {
    m.doc() = "Python bindings for libPlasma using pybind11_weaver";

    // Expose Slaw directly under the top-level module
    py::class_<Slaw>(m, "Slaw")
        .def(py::init<const char*>());

    // Expose Protein directly under the top-level module
    py::class_<Protein>(m, "Protein")
        .def(py::init<>())
        .def(py::init<Slaw>())
        .def(py::init<Slaw, Slaw>());

    // Set up the custom binding registry
    pybind11_weaver::CustomBindingRegistry registry;

    // Register custom bindings
    registry.SetCustomBinding<Entity_oblong_plasma_Slaw>();
    registry.SetCustomBinding<Entity_oblong_plasma_Protein>();
    registry.SetCustomBinding<Entity_oblong_plasma_Hose>();
    registry.SetCustomBinding<Entity_oblong_plasma_Pool>();

    // Call the weaver-generated binding function with the registry
    auto guard = DeclFn(m, registry);
    AddCustomEntities(m, registry);
    guard();  // Optional: immediately update all bindings
}
