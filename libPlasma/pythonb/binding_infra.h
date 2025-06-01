
#ifndef BINDING_INFRA_H
#define BINDING_INFRA_H

#include <memory>
#include <string>
#include <unordered_map>
#include <pybind11/pybind11.h>

namespace pybind11_weaver {

struct EntityScope {
    pybind11::object scope;
    EntityScope(pybind11::object s) : scope(s) {}
    pybind11::object AsScope() const { return scope; }
};

struct EntityBase {
    virtual ~EntityBase() = default;
    virtual void Update() = 0;
};

template <typename PB11T>
void TryAddDefaultCtor(PB11T &handle) {
    // Implementation for TryAddDefaultCtor
}

class CustomBindingRegistry {
public:
    template <typename EntityT>
    void SetCustomBinding(std::shared_ptr<EntityBase> entity) {
        // Implementation for SetCustomBinding
    }
};

class CallUpdateGuard {
public:
    CallUpdateGuard(std::function<void()> update_fn) : update_fn_(update_fn) {}
    ~CallUpdateGuard() { update_fn_(); }
private:
    std::function<void()> update_fn_;
};

template <typename EntityT>
std::shared_ptr<EntityBase> CreateEntity(EntityScope &&parent_h, const CustomBindingRegistry &registry) {
    auto entity = std::make_shared<EntityT>(std::move(parent_h));
    registry.SetCustomBinding<EntityT>(entity);
    return entity;
}

} // namespace pybind11_weaver

#endif // BINDING_INFRA_H
