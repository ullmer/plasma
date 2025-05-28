
// GENERATED AT 05/27/2025, 20:00:20

#include "Protein.h"
#include "Plasma.h"

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




template <class Pybind11T=pybind11::class_<oblong::plasma::Protein>> struct Bind_oblong_plasma_Protein : public EntityBase {
  using Pybind11Type = Pybind11T;
  

virtual const char * AddMethod_IsNull(){
    
const char * _pb11_weaver_comment_str = R"_pb11_weaver(/**
   * A Protein is null when its underlying C-protein (obtainable via
   * ProteinValue) is NULL. A null Protein is also empty.
   */)_pb11_weaver";

#ifndef PB11_WEAVER_DISABLE_oblong_plasma_Protein_IsNull
handle.def("IsNull",static_cast<pybind11_weaver::FnPtrT<oblong::plasma::Protein,bool>::const_type>(&oblong::plasma::Protein::IsNull),_pb11_weaver_comment_str);
#endif
return _pb11_weaver_comment_str;

}


virtual const char * AddMethod_IsEmpty(){
    
const char * _pb11_weaver_comment_str = R"_pb11_weaver(/**
   * A Protein is empty when both its descrips and ingests are null.
   */)_pb11_weaver";

#ifndef PB11_WEAVER_DISABLE_oblong_plasma_Protein_IsEmpty
handle.def("IsEmpty",static_cast<pybind11_weaver::FnPtrT<oblong::plasma::Protein,bool>::const_type>(&oblong::plasma::Protein::IsEmpty),_pb11_weaver_comment_str);
#endif
return _pb11_weaver_comment_str;

}


virtual const char * AddMethod_Null(){
    
const char * _pb11_weaver_comment_str = R"_pb11_weaver(/**
   * Constructor for a NULL Protein, distinct, mind you, from an
   * empty one (as constructed by Protein()).
   */)_pb11_weaver";

#ifndef PB11_WEAVER_DISABLE_oblong_plasma_Protein_Null
handle.def_static("Null",static_cast<pybind11_weaver::FnPtrT<void,oblong::plasma::Protein()>::type>(&oblong::plasma::Protein::Null),_pb11_weaver_comment_str);
#endif
return _pb11_weaver_comment_str;

}


virtual const char * AddMethod_Descrips(){
    
const char * _pb11_weaver_comment_str = R"_pb11_weaver(/**
   * @name Protein structure accessors.
   */
  //@{
  /**
   * The list of Slawx that constitutes this protein's descrips.
   */)_pb11_weaver";

#ifndef PB11_WEAVER_DISABLE_oblong_plasma_Protein_Descrips
handle.def("Descrips",static_cast<pybind11_weaver::FnPtrT<oblong::plasma::Protein,oblong::plasma::Slaw>::const_type>(&oblong::plasma::Protein::Descrips),_pb11_weaver_comment_str);
#endif
return _pb11_weaver_comment_str;

}


virtual const char * AddMethod_Ingests(){
    
const char * _pb11_weaver_comment_str = R"_pb11_weaver(/**
   * A protein's ingests are a set of keyed Slaw. In other words, a
   * Slaw map, which is returned by this function.
   */)_pb11_weaver";

#ifndef PB11_WEAVER_DISABLE_oblong_plasma_Protein_Ingests
handle.def("Ingests",static_cast<pybind11_weaver::FnPtrT<oblong::plasma::Protein,oblong::plasma::Slaw>::const_type>(&oblong::plasma::Protein::Ingests),_pb11_weaver_comment_str);
#endif
return _pb11_weaver_comment_str;

}


virtual const char * AddMethod_ProteinValue(){
    
const char * _pb11_weaver_comment_str = R"_pb11_weaver(/**
   * @name Transforming to other Slaw types.
   */
  //@{
  /**
   * View this Protein as a C-level object.
   */)_pb11_weaver";

#ifndef PB11_WEAVER_DISABLE_oblong_plasma_Protein_ProteinValue
handle.def("ProteinValue",[](oblong::plasma::Protein& self){
    auto && __ret__ = std::invoke(static_cast<pybind11_weaver::FnPtrT<oblong::plasma::Protein,const _slaw *>::const_type>(&oblong::plasma::Protein::ProteinValue),&self) ; return pybind11_weaver::WrapP<const _slaw *>(__ret__);
},_pb11_weaver_comment_str);
#endif
return _pb11_weaver_comment_str;

}


virtual const char * AddMethod_ToSlaw(){
    
const char * _pb11_weaver_comment_str = R"_pb11_weaver(/**
   * Explicit cast to a Slaw, possibly to make this protein part of
   * another Slaw.
   */)_pb11_weaver";

#ifndef PB11_WEAVER_DISABLE_oblong_plasma_Protein_ToSlaw
handle.def("ToSlaw",static_cast<pybind11_weaver::FnPtrT<oblong::plasma::Protein,oblong::plasma::Slaw>::const_type>(&oblong::plasma::Protein::ToSlaw),_pb11_weaver_comment_str);
#endif
return _pb11_weaver_comment_str;

}


virtual const char * AddMethod_Search(){
    
const char * _pb11_weaver_comment_str = R"_pb11_weaver(/**
   * @name Descrips matching. These functions implement searches on
   * Protein descrips compliant with plasma/c semantics. Thus, no
   * coercion or reinterpretation of the descrips or the matching
   * needle is performed.
   */
  //@{
  /**
   * Descrips search. This function looks for @a needle in this
   * protein's descrips, using the plasma semantics. That means that
   * the search will only succeed if the descrips are a list (without
   * any coercion), in which case this functions returns:
   *     - if @a needle is a list, @c this->Descrips().IndexOfList(needle,false)
   *     - if @a needle is not a list, @c this->Descrips().IndexOf(needle)
   * If this protein's descrips are not a list, this function returns a
   * negative value.
   * The optional @a how argument works the same as in the C function
   * protein_search_ex().
   */)_pb11_weaver";

#ifndef PB11_WEAVER_DISABLE_oblong_plasma_Protein_Search
handle.def("Search",static_cast<pybind11_weaver::FnPtrT<oblong::plasma::Protein,long,oblong::plasma::Slaw,Protein_Search_Type>::const_type>(&oblong::plasma::Protein::Search),_pb11_weaver_comment_str);
#endif
return _pb11_weaver_comment_str;

}


virtual const char * AddMethod_Search1(){
    
const char * _pb11_weaver_comment_str = R"_pb11_weaver(/**
   * Works as Search(Slaw), only taking the needle as a bslaw.
   */)_pb11_weaver";

#ifndef PB11_WEAVER_DISABLE_oblong_plasma_Protein_Search1
handle.def("Search",[](oblong::plasma::Protein& self,pybind11_weaver::WrappedPtrT<const _slaw *> needle,Protein_Search_Type how){
    return std::invoke(static_cast<pybind11_weaver::FnPtrT<oblong::plasma::Protein,long,const _slaw *,Protein_Search_Type>::const_type>(&oblong::plasma::Protein::Search),&self,(needle)->Cptr(),how);
},_pb11_weaver_comment_str);
#endif
return _pb11_weaver_comment_str;

}


virtual const char * AddMethod_Matches(){
    
const char * _pb11_weaver_comment_str = R"_pb11_weaver(/**
   * Convenience function checking if Search(needle) > -1
   */)_pb11_weaver";

#ifndef PB11_WEAVER_DISABLE_oblong_plasma_Protein_Matches
handle.def("Matches",static_cast<pybind11_weaver::FnPtrT<oblong::plasma::Protein,bool,oblong::plasma::Slaw,Protein_Search_Type>::const_type>(&oblong::plasma::Protein::Matches),_pb11_weaver_comment_str);
#endif
return _pb11_weaver_comment_str;

}


virtual const char * AddMethod_Matches1(){
    
const char * _pb11_weaver_comment_str = R"_pb11_weaver(/**
   * Convenience function checking if Search(needle) > -1
   */)_pb11_weaver";

#ifndef PB11_WEAVER_DISABLE_oblong_plasma_Protein_Matches1
handle.def("Matches",[](oblong::plasma::Protein& self,pybind11_weaver::WrappedPtrT<const _slaw *> needle,Protein_Search_Type how){
    return std::invoke(static_cast<pybind11_weaver::FnPtrT<oblong::plasma::Protein,bool,const _slaw *,Protein_Search_Type>::const_type>(&oblong::plasma::Protein::Matches),&self,(needle)->Cptr(),how);
},_pb11_weaver_comment_str);
#endif
return _pb11_weaver_comment_str;

}


virtual const char * AddMethod_Timestamp(){
    
const char * _pb11_weaver_comment_str = R"_pb11_weaver(/**
   * Accessor to the pool timestamp of this protein.
   * The timestamp is the time at which the protein
   * was deposited into the pool.
   */)_pb11_weaver";

#ifndef PB11_WEAVER_DISABLE_oblong_plasma_Protein_Timestamp
handle.def("Timestamp",static_cast<pybind11_weaver::FnPtrT<oblong::plasma::Protein,double>::const_type>(&oblong::plasma::Protein::Timestamp),_pb11_weaver_comment_str);
#endif
return _pb11_weaver_comment_str;

}


virtual const char * AddMethod_Index(){
    
const char * _pb11_weaver_comment_str = R"_pb11_weaver(/**
   * The pool index at which this protein was retrieved or set.
   */)_pb11_weaver";

#ifndef PB11_WEAVER_DISABLE_oblong_plasma_Protein_Index
handle.def("Index",static_cast<pybind11_weaver::FnPtrT<oblong::plasma::Protein,long>::const_type>(&oblong::plasma::Protein::Index),_pb11_weaver_comment_str);
#endif
return _pb11_weaver_comment_str;

}


virtual const char * AddMethod_Origin(){
    
const char * _pb11_weaver_comment_str = R"_pb11_weaver(/**
   * The Pool this protein comes from.
   */)_pb11_weaver";

#ifndef PB11_WEAVER_DISABLE_oblong_plasma_Protein_Origin
handle.def("Origin",static_cast<pybind11_weaver::FnPtrT<oblong::plasma::Protein,oblong::loam::Str>::const_type>(&oblong::plasma::Protein::Origin),_pb11_weaver_comment_str);
#endif
return _pb11_weaver_comment_str;

}


virtual const char * AddMethod_Spew(){
    
const char * _pb11_weaver_comment_str = R"_pb11_weaver(/**
   * Debugging and testing aid.
   */)_pb11_weaver";

#ifndef PB11_WEAVER_DISABLE_oblong_plasma_Protein_Spew
handle.def("Spew",static_cast<pybind11_weaver::FnPtrT<oblong::plasma::Protein,void,oblong::plasma::OStreamReference>::const_type>(&oblong::plasma::Protein::Spew),_pb11_weaver_comment_str);
#endif
return _pb11_weaver_comment_str;

}


virtual const char * AddMethod_Hash(){
    
const char * _pb11_weaver_comment_str = R"_pb11_weaver(/**
   * Return a 64-bit hash code for this Protein.
   */)_pb11_weaver";

#ifndef PB11_WEAVER_DISABLE_oblong_plasma_Protein_Hash
handle.def("Hash",static_cast<pybind11_weaver::FnPtrT<oblong::plasma::Protein,unsigned long>::const_type>(&oblong::plasma::Protein::Hash),_pb11_weaver_comment_str);
#endif
return _pb11_weaver_comment_str;

}


virtual const char * AddCtor0(){
    const char * _pb11_weaver_comment_str = R"_pb11_weaver(/**
 * Proteins as a Slaw descrips plus a Slaw ingests. Access to the
 * protein's structure is therefore granted via the Slaw interfaces,
 * which keeps this class definition short and sweet. This class adds
 * to Slaw's protein interface access to metadata related to the hoses
 * originating the given protein.
 *
 * As with other Slaw containers, Protein instances can be constructed
 * from either a C-style object (protein) or by explicitly providing
 * its components in the form of separate Slaw values. In the former
 * case, this class takes care of disposing C-level resources when no
 * longer needed, and of maximising sharing without copying unless
 * needed.
 *
 * Protein instances are immutable objects with value semantics.
 *
 * @ingroup PlasmaSlaw
 */)_pb11_weaver";
    
#ifndef PB11_WEAVER_DISABLE_oblong_plasma_Protein_Ctor0
    handle.def(pybind11::init<>(),_pb11_weaver_comment_str);
#endif
    return _pb11_weaver_comment_str;
}


virtual const char * AddCtor1(){
    const char * _pb11_weaver_comment_str = R"_pb11_weaver(/**
 * Proteins as a Slaw descrips plus a Slaw ingests. Access to the
 * protein's structure is therefore granted via the Slaw interfaces,
 * which keeps this class definition short and sweet. This class adds
 * to Slaw's protein interface access to metadata related to the hoses
 * originating the given protein.
 *
 * As with other Slaw containers, Protein instances can be constructed
 * from either a C-style object (protein) or by explicitly providing
 * its components in the form of separate Slaw values. In the former
 * case, this class takes care of disposing C-level resources when no
 * longer needed, and of maximising sharing without copying unless
 * needed.
 *
 * Protein instances are immutable objects with value semantics.
 *
 * @ingroup PlasmaSlaw
 */)_pb11_weaver";
    
#ifndef PB11_WEAVER_DISABLE_oblong_plasma_Protein_Ctor1
    handle.def(pybind11::init<_slaw *>(),_pb11_weaver_comment_str);
#endif
    return _pb11_weaver_comment_str;
}


virtual const char * AddCtor2(){
    const char * _pb11_weaver_comment_str = R"_pb11_weaver(/**
 * Proteins as a Slaw descrips plus a Slaw ingests. Access to the
 * protein's structure is therefore granted via the Slaw interfaces,
 * which keeps this class definition short and sweet. This class adds
 * to Slaw's protein interface access to metadata related to the hoses
 * originating the given protein.
 *
 * As with other Slaw containers, Protein instances can be constructed
 * from either a C-style object (protein) or by explicitly providing
 * its components in the form of separate Slaw values. In the former
 * case, this class takes care of disposing C-level resources when no
 * longer needed, and of maximising sharing without copying unless
 * needed.
 *
 * Protein instances are immutable objects with value semantics.
 *
 * @ingroup PlasmaSlaw
 */)_pb11_weaver";
    
#ifndef PB11_WEAVER_DISABLE_oblong_plasma_Protein_Ctor2
    handle.def(pybind11::init<oblong::plasma::Slaw>(),_pb11_weaver_comment_str);
#endif
    return _pb11_weaver_comment_str;
}


virtual const char * AddCtor3(){
    const char * _pb11_weaver_comment_str = R"_pb11_weaver(/**
 * Proteins as a Slaw descrips plus a Slaw ingests. Access to the
 * protein's structure is therefore granted via the Slaw interfaces,
 * which keeps this class definition short and sweet. This class adds
 * to Slaw's protein interface access to metadata related to the hoses
 * originating the given protein.
 *
 * As with other Slaw containers, Protein instances can be constructed
 * from either a C-style object (protein) or by explicitly providing
 * its components in the form of separate Slaw values. In the former
 * case, this class takes care of disposing C-level resources when no
 * longer needed, and of maximising sharing without copying unless
 * needed.
 *
 * Protein instances are immutable objects with value semantics.
 *
 * @ingroup PlasmaSlaw
 */)_pb11_weaver";
    
#ifndef PB11_WEAVER_DISABLE_oblong_plasma_Protein_Ctor3
    handle.def(pybind11::init<oblong::plasma::Slaw,oblong::plasma::Slaw>(),_pb11_weaver_comment_str);
#endif
    return _pb11_weaver_comment_str;
}
 
  
  explicit Bind_oblong_plasma_Protein(EntityScope parent_h): handle{ parent_h,"Protein", pybind11::dynamic_attr(),R"_pb11_weaver(/**
 * Proteins as a Slaw descrips plus a Slaw ingests. Access to the
 * protein's structure is therefore granted via the Slaw interfaces,
 * which keeps this class definition short and sweet. This class adds
 * to Slaw's protein interface access to metadata related to the hoses
 * originating the given protein.
 *
 * As with other Slaw containers, Protein instances can be constructed
 * from either a C-style object (protein) or by explicitly providing
 * its components in the form of separate Slaw values. In the former
 * case, this class takes care of disposing C-level resources when no
 * longer needed, and of maximising sharing without copying unless
 * needed.
 *
 * Protein instances are immutable objects with value semantics.
 *
 * @ingroup PlasmaSlaw
 */)_pb11_weaver" }
  {}
  
  template<class... HandleArgsT>
  explicit Bind_oblong_plasma_Protein(EntityScope parent_h, HandleArgsT&&... args):handle{std::forward(args)...}
  {}
  
  void Update() override {
   AddMethod_IsNull();
AddMethod_IsEmpty();
AddMethod_Null();
AddMethod_Descrips();
AddMethod_Ingests();
AddMethod_ProteinValue();
AddMethod_ToSlaw();
AddMethod_Search();
AddMethod_Search1();
AddMethod_Matches();
AddMethod_Matches1();
AddMethod_Timestamp();
AddMethod_Index();
AddMethod_Origin();
AddMethod_Spew();
AddMethod_Hash();
AddCtor0();
AddCtor1();
AddCtor2();
AddCtor3(); 
  }
  
  EntityScope AsScope() override {
    return EntityScope(handle);
  }
  
  static const char * Key(){ 
    return "oblong_plasma_Protein";
  }
   
  Pybind11Type handle; 
};
#ifndef PB11_WEAVER_DISABLE_Entity_oblong_plasma_Protein

using Entity_oblong_plasma_Protein = Bind_oblong_plasma_Protein<>;

#else

struct Entity_oblong_plasma_Protein : public pybind11_weaver::DisabledEntity {
  explicit Entity_oblong_plasma_Protein(EntityScope){}
  static const char * Key(){ 
    return "oblong_plasma_Protein";
  }
};

#endif // PB11_WEAVER_DISABLE_Entity_oblong_plasma_Protein




template <class Pybind11T=pybind11::class_<oblong::plasma::Protein_hash>> struct Bind_oblong_plasma_Protein_hash : public EntityBase {
  using Pybind11Type = Pybind11T;
   
  
  explicit Bind_oblong_plasma_Protein_hash(EntityScope parent_h): handle{ parent_h,"Protein_hash", pybind11::dynamic_attr(),R"_pb11_weaver(/**
 * A hash function wrapper that makes Protein easy to use in Boost or TR1
 * unordered maps.
 */)_pb11_weaver" }
  {}
  
  template<class... HandleArgsT>
  explicit Bind_oblong_plasma_Protein_hash(EntityScope parent_h, HandleArgsT&&... args):handle{std::forward(args)...}
  {}
  
  void Update() override {
   pybind11_weaver::TryAddDefaultCtor<oblong::plasma::Protein_hash>(handle); 
  }
  
  EntityScope AsScope() override {
    return EntityScope(handle);
  }
  
  static const char * Key(){ 
    return "oblong_plasma_Protein_hash";
  }
   
  Pybind11Type handle; 
};
#ifndef PB11_WEAVER_DISABLE_Entity_oblong_plasma_Protein_hash

using Entity_oblong_plasma_Protein_hash = Bind_oblong_plasma_Protein_hash<>;

#else

struct Entity_oblong_plasma_Protein_hash : public pybind11_weaver::DisabledEntity {
  explicit Entity_oblong_plasma_Protein_hash(EntityScope){}
  static const char * Key(){ 
    return "oblong_plasma_Protein_hash";
  }
};

#endif // PB11_WEAVER_DISABLE_Entity_oblong_plasma_Protein_hash




template <class Pybind11T=pybind11::module_ &> struct Bind_hash_value : public EntityBase {
  using Pybind11Type = Pybind11T;
  
virtual const char * AddFunction(){
    const char * _pb11_weaver_comment_str = R"_pb11_weaver(// http://www.boost.org/doc/libs/1_47_0/doc/html/hash/custom.html)_pb11_weaver";
    
#ifndef PB11_WEAVER_DISABLE_hash_value_AddFunction
    handle.def("hash_value",static_cast<pybind11_weaver::FnPtrT<void,unsigned long(const oblong::plasma::Protein &)>::type>(&oblong::plasma::hash_value),_pb11_weaver_comment_str);
#endif
    return _pb11_weaver_comment_str;
}
 
  
  explicit Bind_hash_value(EntityScope parent_h): handle{ static_cast<pybind11::module_&>(parent_h) }
  {}
  
  template<class... HandleArgsT>
  explicit Bind_hash_value(EntityScope parent_h, HandleArgsT&&... args):handle{std::forward(args)...}
  {}
  
  void Update() override {
   AddFunction(); 
  }
  
  EntityScope AsScope() override {
    return EntityScope(handle);
  }
  
  static const char * Key(){ 
    return "hash_value";
  }
   
  Pybind11Type handle; 
};
#ifndef PB11_WEAVER_DISABLE_Entity_hash_value

using Entity_hash_value = Bind_hash_value<>;

#else

struct Entity_hash_value : public pybind11_weaver::DisabledEntity {
  explicit Entity_hash_value(EntityScope){}
  static const char * Key(){ 
    return "hash_value";
  }
};

#endif // PB11_WEAVER_DISABLE_Entity_hash_value




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


/**
* Create all entities, return a callable guard that can be called to update all entities.
* If the returned guard is not called, the guard will call the update function on its destruction.
**/
[[nodiscard]] pybind11_weaver::CallUpdateGuard DeclFn(pybind11::module & m, const pybind11_weaver::CustomBindingRegistry & registry){
pybind11_weaver::_PointerWrapperBase::FastBind(m);
pybind11_weaver::PointerWrapper<const _slaw *>::FastBind(m,"const_slawp");

auto v0 = pybind11_weaver::CreateEntity<Entity_oblong>(EntityScope(m), registry);
auto v1 = pybind11_weaver::CreateEntity<Entity_oblong_plasma>(v0->AsScope(), registry);
auto v2 = pybind11_weaver::CreateEntity<Entity_oblong_plasma_Protein>(v1->AsScope(), registry);
auto v3 = pybind11_weaver::CreateEntity<Entity_oblong_plasma_Protein_hash>(v1->AsScope(), registry);
auto v4 = pybind11_weaver::CreateEntity<Entity_hash_value>(v1->AsScope(), registry);
auto v5 = pybind11_weaver::CreateEntity<Entity_std>(EntityScope(m), registry);
auto v6 = pybind11_weaver::CreateEntity<Entity_std_hash6oblong_plasma_Protein9>(v5->AsScope(), registry);

    auto update_fn = [=](){
v0->Update();
v1->Update();
v2->Update();
v3->Update();
v4->Update();
v5->Update();
v6->Update();    
    };
    return {update_fn};
}

} // anonymous namespace

