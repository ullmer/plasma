
#include <pybind11/pybind11.h>
#include "custom_bindings.h"

namespace py = pybind11;

void AddCustomEntities(py::module_ &m, const pybind11_weaver::CustomBindingRegistry &registry) {
    pybind11_weaver::DeclFn(m, registry);
}

PYBIND11_MODULE(plasma, m) {
    pybind11_weaver::CustomBindingRegistry registry;
    AddCustomEntities(m, registry);
}
