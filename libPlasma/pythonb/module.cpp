#include <pybind11/pybind11.h>
namespace py = pybind11;

// Include the generated bindings
#include "binding_infra.h"

// Include your custom bindings
#include "custom_bindings.h"

PYBIND11_MODULE(plasma, m) {
  m.doc() = "Python bindings for libPlasma using pybind11_weaver";

  // Create the 'plasma' submodule 
  py::module plasma = m.def_submodule("plasma");

  // Create the 'hose' submodule 
  py::module hose   = m.def_submodule("hose");

  // Create the 'hose' submodule
  py::module protein = m.def_submodule("protein");

  // Create the 'hose' submodule 
  py::module slaw    = m.def_submodule("slaw");

  // Set up the custom binding registry
  pybind11_weaver::CustomBindingRegistry registry;

  // Register custom bindings
  registry.SetCustomBinding<Entity_oblong_plasma_Slaw>();
  registry.SetCustomBinding<Entity_oblong_plasma_Protein>();

  // Call the weaver-generated binding function with the registry
  auto guard = DeclFn(m, registry);
  guard();  // Optional: immediately update all bindings
}

/// end ///
