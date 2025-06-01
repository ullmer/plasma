
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

  template <class BindT, class PB11T>
  void TryAddDefaultCtor(PB11T &handle) {
    if constexpr (std::is_default_constructible<BindT>::value) {
      handle.def(pybind11::init<>());
    }
  } // namespace pybind11_weaver
}

#endif // BINDING_INFRA_H
