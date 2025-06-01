
#include <pybind11/pybind11.h>
#include "Slaw.h"
#include "Protein.h"

//Include the generated bindings
#include "custom_bindings.h"

// Include your custom bindings
#include "binding_infra.h"

namespace py = pybind11;
using namespace oblong::plasma;

void AddCustomEntities(pybind11::module_ &m, const pybind11_weaver::CustomBindingRegistry &registry) {
    using namespace pybind11_weaver;

    EntityScope top_scope(m);
    CreateEntity<Entity_oblong_plasma_Hose>(std::move(top_scope), registry)->Update();

    // Recreate top_scope since it's been moved
    EntityScope top_scope2(m);
    CreateEntity<Entity_oblong_plasma_Pool>(std::move(top_scope2), registry)->Update();

    EntityScope top_scope3(m);
    CreateEntity<Entity_oblong_plasma_Protein>(std::move(top_scope3), registry)->Update();

    EntityScope top_scope4(m);
    CreateEntity<Entity_oblong_plasma_Slaw>(std::move(top_scope4), registry)->Update();
}

PYBIND11_MODULE(plasma, m) {
    m.doc() = "Python bindings for libPlasma using pybind11_weaver";

    // Expose Slaw directly under the top-level module
    py::class_<Slaw>(m, "Slaw")
        .def(py::init<const char*>());

    // Set up the custom binding registry
    pybind11_weaver::CustomBindingRegistry registry;

    // Register custom bindings
    registry.SetCustomBinding<Entity_oblong_plasma_Slaw>();
    registry.SetCustomBinding<Entity_oblong_plasma_Protein>();
    registry.SetCustomBinding<Entity_oblong_plasma_Hose>();
    registry.SetCustomBinding<Entity_oblong_plasma_Pool>();

    // Call the weaver-generated binding function with the registry
    auto guard = DeclFn(m, registry);
    guard();  // Optional: immediately update all bindings

    // Add custom entities to the top-level module
    AddCustomEntities(m, registry);
}
