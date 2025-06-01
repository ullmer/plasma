
#ifndef BINDING_INFRA_H
#define BINDING_INFRA_H

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <memory>
#include <string>
#include <map>
#include <functional>
#include <vector>

namespace pybind11_weaver {

using Entity_std = Bind_std<>;

struct EntityScope {
    explicit EntityScope(int64_t, int64_t) {} // a tag for disabled scope
    explicit EntityScope(pybind11::module_ &parent_h) : module_{&parent_h} {}
    explicit EntityScope(pybind11::detail::generic_type &parent_h) : type_{&parent_h} {}
    explicit operator pybind11::module_ &() { return *module_; }
    explicit operator pybind11::detail::generic_type &() { return *type_; }
    operator pybind11::handle &() {
        if (module_) {
            return *module_;
        } else {
            return *type_;
        }
    }
    bool IsDisabled() const { return module_ == nullptr && type_ == nullptr; }

private:
    pybind11::detail::generic_type *type_ = nullptr;
    pybind11::module_ *module_ = nullptr;
};

struct EntityBase {
    virtual ~EntityBase() = default;
    virtual void Update() = 0;
    virtual EntityScope AsScope() = 0;
};

struct DisabledEntity : public EntityBase {
    void Update() override {}
    EntityScope AsScope() override { return EntityScope{0, 0}; }
};

struct CustomBindingRegistry {
    using CTorT = std::function<std::shared_ptr<EntityBase>(EntityScope &&)>;
    using RegistryT = std::map<std::string, CTorT>;

    bool contains(const std::string &key) const {
        return registry_.count(key) > 0;
    }
    CTorT at(const std::string &key) const { return registry_.at(key); }

    template <class BindingT> void DisableBinding() {
        auto key = std::string(BindingT::Key());
        registry_.emplace(key, [](EntityScope &&) { return std::make_shared<DisabledEntity>(); });
    }

    void RegCustomBinding(const std::string &key, CTorT &&ctor) {
        registry_.emplace(key, std::move(ctor));
    }

    template <class BindingT> void SetCustomBinding() {
        auto key = std::string(BindingT::Key());
        registry_.emplace(key, [](EntityScope &&parent_h) {
            return std::make_shared<BindingT>(std::move(parent_h));
        });
    }

private:
    RegistryT registry_;
};

template <class EntityT>
std::shared_ptr<EntityBase>
CreateEntity(EntityScope &&parent_h, const CustomBindingRegistry &registry) {
    if (parent_h.IsDisabled()) {
        return std::make_shared<DisabledEntity>();
    }
    auto key = std::string(EntityT::Key());
    if (!registry.contains(key)) {
        return std::make_shared<EntityT>(std::move(parent_h));
    } else {
        auto fn = registry.at(key);
        return fn(std::move(parent_h));
    }
}

class CallUpdateGuard {
public:
    using Fn = std::function<void(void)>;
    CallUpdateGuard(Fn fn) : fn_(fn) {}

    CallUpdateGuard(CallUpdateGuard &&rhs) {
        this->fn_ = rhs.fn_;
        rhs.fn_ = nullptr;
    }

    void operator()() {
        if (fn_) {
            fn_();
            fn_ = nullptr;
        }
    }

    ~CallUpdateGuard() { this->operator()(); }

private:
    Fn fn_;
};

[[nodiscard]] CallUpdateGuard ;
    return {update_fn};
}

  template <class BindT, class PB11T>
  void TryAddDefaultCtor(PB11T &handle) {
    if constexpr (std::is_default_constructible<BindT>::value) {
      handle.def(pybind11::init<>());
    }
  } // namespace pybind11_weaver

template <class Pybind11T = pybind11::module_>
struct Bind_std : public pybind11_weaver::EntityBase {
  using Pybind11Type = Pybind11T;
  Pybind11Type handle;

  explicit Bind_std(pybind11_weaver::EntityScope parent_h)
      : handle(static_cast<pybind11::module_ &>(parent_h).def_submodule("std")) {}
  void Update() override {}
  pybind11_weaver::EntityScope AsScope() override { return pybind11_weaver::EntityScope(handle); }
  static const char *Key() { return "std"; }
};
}


#endif // BINDING_INFRA_H
