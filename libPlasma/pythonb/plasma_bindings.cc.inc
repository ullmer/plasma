
// GENERATED AT 05/30/2025, 10:32:16

#include "Protein.h"
#include "Plasma.h"
#include "PlasmaStreams.h"
#include "Pool.h"
#include "Hose.h"
#include "Slaw.h"
#include "CompositeSlaw.h"
#include "HoseGang.h"
#include "PlasmaForward.h"
#include "SlawIterator.h"
#include "SlawRef.h"

#ifndef GITHUB_COM_PYBIND11_WEAVER
#define GITHUB_COM_PYBIND11_WEAVER
#include <atomic>
#include <functional>
#include <map>
#include <mutex>
#include <thread>
#include <utility>

#include <pybind11/functional.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace pybind11_weaver {

template <class BindT, class PB11T> void TryAddDefaultCtor(PB11T &handle) {
  if constexpr (std::is_default_constructible<BindT>::value) {
    handle.def(pybind11::init<>());
  }
}

template <class ClassT, class MethodRetT, class... MethodArgs> struct FnPtrT {
  using type = MethodRetT (ClassT::*)(MethodArgs...);
  using const_type = MethodRetT (ClassT::*)(MethodArgs...) const;
  using const_rref_type = MethodRetT (ClassT::*)(MethodArgs...) const &&;
  using const_lref_type = MethodRetT (ClassT::*)(MethodArgs...) const &;
  using rref_type = MethodRetT (ClassT::*)(MethodArgs...) &&;
  using lref_type = MethodRetT (ClassT::*)(MethodArgs...) &;
};
template <class FnTtype> struct FnPtrT<void, FnTtype> {
  using type = FnTtype *;
};

struct _PointerWrapperBase {
  _PointerWrapperBase(void *ptr_) : ptr(ptr_) {}
  _PointerWrapperBase(intptr_t ptr_v) : ptr(reinterpret_cast<void *>(ptr_v)) {}
  intptr_t get_ptr() { return reinterpret_cast<intptr_t>(ptr); }
  void set_ptr(intptr_t ptr_v) { ptr = reinterpret_cast<void *>(ptr_v); }
  static void FastBind(pybind11::module &m) {
    pybind11::class_<_PointerWrapperBase, std::shared_ptr<_PointerWrapperBase>>(
        m, "_PointerWrapperBase", pybind11::dynamic_attr())
        .def(pybind11::init<void *>())
        .def(pybind11::init<intptr_t>())
        .def("get_ptr", &_PointerWrapperBase::get_ptr)
        .def("set_ptr", &_PointerWrapperBase::set_ptr);
  }
  void *ptr;
};

template <class T> struct PointerWrapper : public _PointerWrapperBase {
  static_assert(std::is_pointer<T>::value, "T must be a pointer type");
  using _PointerWrapperBase::_PointerWrapperBase;

  static void FastBind(pybind11::module &m, const std::string &name) {
    pybind11::class_<PointerWrapper, std::shared_ptr<PointerWrapper>,
                     _PointerWrapperBase>(m, name.c_str(),
                                          pybind11::dynamic_attr())
        .def(pybind11::init<intptr_t>())
        .def_static("from_capsule", [](pybind11::capsule o) {
          return std::make_shared<PointerWrapper<T>>(
              reinterpret_cast<void *>(o.get_pointer()));
        });
  }
  T Cptr() { return reinterpret_cast<T>(ptr); }
};
template <class T> using WrappedPtrT = std::shared_ptr<PointerWrapper<T>>;

template <class T> WrappedPtrT<T> WrapP(T ptr) {
  if (!ptr) {
    return nullptr;
  }
  return WrappedPtrT<T>{new PointerWrapper<T>((void *)ptr)};
}

struct Guardian {
  std::vector<std::function<void()>> dtor_callbacks;
  ~Guardian() {
    for (auto &fn : dtor_callbacks) {
      fn();
    }
  }
};

template <typename R, typename... Args> struct FnPointerWrapper {
  using CppFnT = R(Args...);

  template <class CR, typename... CArgs> struct GetCptr {
    using CFnPtrT = CR (*)(CArgs...);
    static CFnPtrT Run(std::function<CppFnT> to_call, Guardian &&guard,
                       CFnPtrT c_wrapper, const char *uuid0, int64_t uuid1) {
      // lock
      guard.dtor_callbacks.push_back(
          [uuid0, uuid1]() { ReleaseFnProxy(uuid0, uuid1); });
      SetFnProxy(uuid0, uuid1, to_call);
      return c_wrapper;
    }
  };

  using FnMapT =
      std::map<const char *, std::map<int64_t, std::function<CppFnT>>>;
  static void SetFnProxy(const char *uuid0, int64_t uuid1,
                         std::function<CppFnT> &fn) {
    FnMapMutex().lock();
    while (FnMap()[uuid0].count(uuid1) != 0) {
      // The chance is so low, spin lock should be fine
      FnMapMutex().unlock();
      std::this_thread::sleep_for(std::chrono::milliseconds(1));
      FnMapMutex().lock();
    }
    FnMap()[uuid0][uuid1] = fn;
    FnMapMutex().unlock();
  }

  static std::function<CppFnT> GetFnProxy(const char *uuid0, int64_t uuid1) {
    std::lock_guard<std::mutex> _(FnMapMutex());
    auto ret = FnMap()[uuid0][uuid1];
    return ret;
  }

  static void ReleaseFnProxy(const char *uuid0, int64_t uuid1) {
    std::lock_guard<std::mutex> _(FnMapMutex());
    FnMap()[uuid0].erase(uuid1);
  }
  static FnMapT &FnMap() {
    static FnMapT fns;
    return fns;
  }

  static std::mutex &FnMapMutex() {
    static std::mutex m;
    return m;
  }
};

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

struct EntityScope {
  explicit EntityScope(int64_t, int64_t) {} // a tag for disabled scope
  explicit EntityScope(pybind11::module_ &parent_h) : module_{&parent_h} {}
  explicit EntityScope(pybind11::detail::generic_type &parent_h)
      : type_{&parent_h} {}
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
    registry_.emplace(
        key, [](EntityScope &&) { return std::make_shared<DisabledEntity>(); });
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

} // namespace pybind11_weaver
#endif // GITHUB_COM_PYBIND11_WEAVER


namespace {

using pybind11_weaver::EntityScope;
using pybind11_weaver::EntityBase;





template <class Pybind11T=pybind11::module_> struct Bind_oblong : public EntityBase {
  using Pybind11Type = Pybind11T;
   
  
  explicit Bind_oblong(EntityScope parent_h): handle{ static_cast<pybind11::module_&>(parent_h).def_submodule("oblong") }
  {}
  
  template<class... HandleArgsT>
  explicit Bind_oblong(EntityScope parent_h, HandleArgsT&&... args):handle{std::forward(args)...}
  {}
  
  void Update() override {
    
  }
  
  EntityScope AsScope() override {
    return EntityScope(handle);
  }
  
  static const char * Key(){ 
    return "oblong";
  }
   
  Pybind11Type handle; 
};
#ifndef PB11_WEAVER_DISABLE_Entity_oblong

using Entity_oblong = Bind_oblong<>;

#else

struct Entity_oblong : public pybind11_weaver::DisabledEntity {
  explicit Entity_oblong(EntityScope){}
  static const char * Key(){ 
    return "oblong";
  }
};

#endif // PB11_WEAVER_DISABLE_Entity_oblong




template <class Pybind11T=pybind11::module_> struct Bind_oblong_plasma : public EntityBase {
  using Pybind11Type = Pybind11T;
   
  
  explicit Bind_oblong_plasma(EntityScope parent_h): handle{ static_cast<pybind11::module_&>(parent_h).def_submodule("plasma") }
  {}
  
  template<class... HandleArgsT>
  explicit Bind_oblong_plasma(EntityScope parent_h, HandleArgsT&&... args):handle{std::forward(args)...}
  {}
  
  void Update() override {
    
  }
  
  EntityScope AsScope() override {
    return EntityScope(handle);
  }
  
  static const char * Key(){ 
    return "oblong_plasma";
  }
   
  Pybind11Type handle; 
};
#ifndef PB11_WEAVER_DISABLE_Entity_oblong_plasma

using Entity_oblong_plasma = Bind_oblong_plasma<>;

#else

struct Entity_oblong_plasma : public pybind11_weaver::DisabledEntity {
  explicit Entity_oblong_plasma(EntityScope){}
  static const char * Key(){ 
    return "oblong_plasma";
  }
};

#endif // PB11_WEAVER_DISABLE_Entity_oblong_plasma




template <class Pybind11T=pybind11::class_<oblong::plasma::OStreamReference>> struct Bind_oblong_plasma_OStreamReference : public EntityBase {
  using Pybind11Type = Pybind11T;
  

virtual const char * AddCtor0(){
    const char * _pb11_weaver_comment_str = R"_pb11_weaver(/**
 * It is forbidden (with echo sound effect like in Superman) to
 * include any C++ I/O headers, even harmless little \<iosfwd\>,
 * in "normal" Oblong headers like Slaw.h.  So, we take a
 * Plessy v. Ferguson approach and segregate all mention of
 * std::ostream into this header, PlasmaStreams.h.
 *
 * However, the problem is that Jao long ago gave Slaw this method:
 *
 * \code
 *   void Spew (\::std::ostream &os)  const;
 * \endcode
 *
 * So, in order to remain backwards-compatible with that method,
 * while retroactively purging \<iosfwd\> from Slaw.h, we have to
 * resort to a little trick.  We change the method to instead be:
 *
 * \code
 *   void Spew (OStreamReference os)  const;
 * \endcode
 *
 * Where OStreamReference is forward-declared in PlasmaForward.h.
 * Then, if you actually want to call that method, you include
 * PlasmaStream.h, which defines OStreamReference to be a simple
 * wrapper around a reference to \::std::ostream, and most importantly,
 * with a constructor that will automatically wrap the ostream for you.
 * Therefore, due to the wonders of C++, you can continue to call
 * the method just like you used to, even though the signature has
 * changed.  This double-indirection-of-forward-declarations seems
 * silly, but then the lengths to which Oblong goes to avoid the
 * standard C++ library are often silly.
 */)_pb11_weaver";
    
#ifndef PB11_WEAVER_DISABLE_oblong_plasma_OStreamReference_Ctor0
    handle.def(pybind11::init<std::basic_ostream<char> &>(),_pb11_weaver_comment_str);
#endif
    return _pb11_weaver_comment_str;
}
 
  
  explicit Bind_oblong_plasma_OStreamReference(EntityScope parent_h): handle{ parent_h,"OStreamReference", pybind11::dynamic_attr(),R"_pb11_weaver(/**
 * It is forbidden (with echo sound effect like in Superman) to
 * include any C++ I/O headers, even harmless little \<iosfwd\>,
 * in "normal" Oblong headers like Slaw.h.  So, we take a
 * Plessy v. Ferguson approach and segregate all mention of
 * std::ostream into this header, PlasmaStreams.h.
 *
 * However, the problem is that Jao long ago gave Slaw this method:
 *
 * \code
 *   void Spew (\::std::ostream &os)  const;
 * \endcode
 *
 * So, in order to remain backwards-compatible with that method,
 * while retroactively purging \<iosfwd\> from Slaw.h, we have to
 * resort to a little trick.  We change the method to instead be:
 *
 * \code
 *   void Spew (OStreamReference os)  const;
 * \endcode
 *
 * Where OStreamReference is forward-declared in PlasmaForward.h.
 * Then, if you actually want to call that method, you include
 * PlasmaStream.h, which defines OStreamReference to be a simple
 * wrapper around a reference to \::std::ostream, and most importantly,
 * with a constructor that will automatically wrap the ostream for you.
 * Therefore, due to the wonders of C++, you can continue to call
 * the method just like you used to, even though the signature has
 * changed.  This double-indirection-of-forward-declarations seems
 * silly, but then the lengths to which Oblong goes to avoid the
 * standard C++ library are often silly.
 */)_pb11_weaver" }
  {}
  
  template<class... HandleArgsT>
  explicit Bind_oblong_plasma_OStreamReference(EntityScope parent_h, HandleArgsT&&... args):handle{std::forward(args)...}
  {}
  
  void Update() override {
   AddCtor0(); 
  }
  
  EntityScope AsScope() override {
    return EntityScope(handle);
  }
  
  static const char * Key(){ 
    return "oblong_plasma_OStreamReference";
  }
   
  Pybind11Type handle; 
};
#ifndef PB11_WEAVER_DISABLE_Entity_oblong_plasma_OStreamReference

using Entity_oblong_plasma_OStreamReference = Bind_oblong_plasma_OStreamReference<>;

#else

struct Entity_oblong_plasma_OStreamReference : public pybind11_weaver::DisabledEntity {
  explicit Entity_oblong_plasma_OStreamReference(EntityScope){}
  static const char * Key(){ 
    return "oblong_plasma_OStreamReference";
  }
};

#endif // PB11_WEAVER_DISABLE_Entity_oblong_plasma_OStreamReference




template <class Pybind11T=pybind11::module_> struct Bind_std : public EntityBase {
  using Pybind11Type = Pybind11T;
   
  
  explicit Bind_std(EntityScope parent_h): handle{ static_cast<pybind11::module_&>(parent_h).def_submodule("std") }
  {}
  
  template<class... HandleArgsT>
  explicit Bind_std(EntityScope parent_h, HandleArgsT&&... args):handle{std::forward(args)...}
  {}
  
  void Update() override {
    
  }
  
  EntityScope AsScope() override {
    return EntityScope(handle);
  }
  
  static const char * Key(){ 
    return "std";
  }
   
  Pybind11Type handle; 
};
#ifndef PB11_WEAVER_DISABLE_Entity_std

using Entity_std = Bind_std<>;

#else

struct Entity_std : public pybind11_weaver::DisabledEntity {
  explicit Entity_std(EntityScope){}
  static const char * Key(){ 
    return "std";
  }
};

#endif // PB11_WEAVER_DISABLE_Entity_std




template <class Pybind11T=pybind11::class_<std::hash<oblong::plasma::Protein>>> struct Bind_std_hash6oblong_plasma_Protein9 : public EntityBase {
  using Pybind11Type = Pybind11T;
  using _Tp = oblong::plasma::Protein; 
  
  explicit Bind_std_hash6oblong_plasma_Protein9(EntityScope parent_h): handle{ parent_h,"hash6oblong_plasma_Protein9", pybind11::dynamic_attr() }
  {}
  
  template<class... HandleArgsT>
  explicit Bind_std_hash6oblong_plasma_Protein9(EntityScope parent_h, HandleArgsT&&... args):handle{std::forward(args)...}
  {}
  
  void Update() override {
   pybind11_weaver::TryAddDefaultCtor<std::hash<oblong::plasma::Protein>>(handle); 
  }
  
  EntityScope AsScope() override {
    return EntityScope(handle);
  }
  
  static const char * Key(){ 
    return "std_hash6oblong_plasma_Protein9";
  }
   
  Pybind11Type handle; 
};
#ifndef PB11_WEAVER_DISABLE_Entity_std_hash6oblong_plasma_Protein9

using Entity_std_hash6oblong_plasma_Protein9 = Bind_std_hash6oblong_plasma_Protein9<>;

#else

struct Entity_std_hash6oblong_plasma_Protein9 : public pybind11_weaver::DisabledEntity {
  explicit Entity_std_hash6oblong_plasma_Protein9(EntityScope){}
  static const char * Key(){ 
    return "std_hash6oblong_plasma_Protein9";
  }
};

#endif // PB11_WEAVER_DISABLE_Entity_std_hash6oblong_plasma_Protein9




template <class Pybind11T=pybind11::class_<std::hash<oblong::plasma::Slaw>>> struct Bind_std_hash6oblong_plasma_Slaw9 : public EntityBase {
  using Pybind11Type = Pybind11T;
  using _Tp = oblong::plasma::Slaw; 
  
  explicit Bind_std_hash6oblong_plasma_Slaw9(EntityScope parent_h): handle{ parent_h,"hash6oblong_plasma_Slaw9", pybind11::dynamic_attr() }
  {}
  
  template<class... HandleArgsT>
  explicit Bind_std_hash6oblong_plasma_Slaw9(EntityScope parent_h, HandleArgsT&&... args):handle{std::forward(args)...}
  {}
  
  void Update() override {
   pybind11_weaver::TryAddDefaultCtor<std::hash<oblong::plasma::Slaw>>(handle); 
  }
  
  EntityScope AsScope() override {
    return EntityScope(handle);
  }
  
  static const char * Key(){ 
    return "std_hash6oblong_plasma_Slaw9";
  }
   
  Pybind11Type handle; 
};
#ifndef PB11_WEAVER_DISABLE_Entity_std_hash6oblong_plasma_Slaw9

using Entity_std_hash6oblong_plasma_Slaw9 = Bind_std_hash6oblong_plasma_Slaw9<>;

#else

struct Entity_std_hash6oblong_plasma_Slaw9 : public pybind11_weaver::DisabledEntity {
  explicit Entity_std_hash6oblong_plasma_Slaw9(EntityScope){}
  static const char * Key(){ 
    return "std_hash6oblong_plasma_Slaw9";
  }
};

#endif // PB11_WEAVER_DISABLE_Entity_std_hash6oblong_plasma_Slaw9


/**
* Create all entities, return a callable guard that can be called to update all entities.
* If the returned guard is not called, the guard will call the update function on its destruction.
**/
[[nodiscard]] pybind11_weaver::CallUpdateGuard DeclFn(pybind11::module & m, const pybind11_weaver::CustomBindingRegistry & registry){
pybind11_weaver::_PointerWrapperBase::FastBind(m);


auto v0 = pybind11_weaver::CreateEntity<Entity_oblong>(EntityScope(m), registry);
auto v1 = pybind11_weaver::CreateEntity<Entity_oblong_plasma>(v0->AsScope(), registry);
auto v2 = pybind11_weaver::CreateEntity<Entity_oblong_plasma_OStreamReference>(v1->AsScope(), registry);
auto v3 = pybind11_weaver::CreateEntity<Entity_std>(EntityScope(m), registry);
auto v4 = pybind11_weaver::CreateEntity<Entity_std_hash6oblong_plasma_Protein9>(v3->AsScope(), registry);
auto v5 = pybind11_weaver::CreateEntity<Entity_std_hash6oblong_plasma_Slaw9>(v3->AsScope(), registry);

    auto update_fn = [=](){
v0->Update();
v1->Update();
v2->Update();
v3->Update();
v4->Update();
v5->Update();    
    };
    return {update_fn};
}

} // anonymous namespace

