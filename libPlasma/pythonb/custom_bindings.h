
#ifndef CUSTOM_BINDINGS_H
#define CUSTOM_BINDINGS_H

#include "binding_infra.h"
#include "Slaw.h"
#include "Protein.h"
#include "Hose.h"
#include "Pool.h"

namespace pybind11_weaver {

template <typename Pybind11T = pybind11::class_<oblong::plasma::Slaw>>
struct Bind_oblong_plasma_Slaw {
  static const char *Key() { return "oblong_plasma_Slaw"; }
  Bind_oblong_plasma_Slaw(EntityScope scope) {
    auto handle = scope
      .attr("Slaw")
      .def(pybind11::init<>())
      .def("IsNull", &oblong::plasma::Slaw::IsNull)
      .def("IsCons", &oblong::plasma::Slaw::IsCons)
      .def("Car", &oblong::plasma::Slaw::Car)
      .def("Cdr", &oblong::plasma::Slaw::Cdr);
    TryAddDefaultCtor(handle);
  }
};

template <typename Pybind11T = pybind11::class_<oblong::plasma::Protein>>
struct Bind_oblong_plasma_Protein {
  static const char *Key() { return "oblong_plasma_Protein"; }
  Bind_oblong_plasma_Protein(EntityScope scope) {
    auto handle = scope
      .attr("Protein")
      .def(pybind11::init<>())
      .def("IsNull", &oblong::plasma::Protein::IsNull)
      .def("Descrips", &oblong::plasma::Protein::Descrips)
      .def("Ingests", &oblong::plasma::Protein::Ingests);
    TryAddDefaultCtor(handle);
  }
};

template <typename Pybind11T = pybind11::class_<oblong::plasma::Hose>>
struct Bind_oblong_plasma_Hose {
  static const char *Key() { return "oblong_plasma_Hose"; }
  Bind_oblong_plasma_Hose(EntityScope scope) {
    auto handle = scope
      .attr("Hose")
      .def(pybind11::init<>())
      .def("IsNull", &oblong::plasma::Hose::IsNull)
      .def("Name", &oblong::plasma::Hose::Name)
      .def("Open", &oblong::plasma::Hose::Open)
      .def("Close", &oblong::plasma::Hose::Close);
    TryAddDefaultCtor(handle);
  }
};

template <typename Pybind11T = pybind11::class_<oblong::plasma::Pool>>
struct Bind_oblong_plasma_Pool {
  static const char *Key() { return "oblong_plasma_Pool"; }
  Bind_oblong_plasma_Pool(EntityScope scope) {
    auto handle = scope
      .attr("Pool")
      .def(pybind11::init<>())
      .def("IsNull", &oblong::plasma::Pool::IsNull)
      .def("Name", &oblong::plasma::Pool::Name)
      .def("Open", &oblong::plasma::Pool::Open)
      .def("Close", &oblong::plasma::Pool::Close);
    TryAddDefaultCtor(handle);
  }
};

template <typename Pybind11T = pybind11::class_<std::hash<oblong::plasma::Protein>>>
struct Bind_std_hash6oblong_plasma_Protein9 {
  static const char *Key() { return "std_hash6oblong_plasma_Protein9"; }
  Bind_std_hash6oblong_plasma_Protein9(EntityScope scope) {
    auto handle = scope
      .attr("hash<oblong::plasma::Protein>")
      .def(pybind11::init<>());
    TryAddDefaultCtor(handle);
  }
};

template <typename Pybind11T = pybind11::class_<std::hash<oblong::plasma::Slaw>>>
struct Bind_std_hash6oblong_plasma_Slaw9 {
  static const char *Key() { return "std_hash6oblong_plasma_Slaw9"; }
  Bind_std_hash6oblong_plasma_Slaw9(EntityScope scope) {
    auto handle = scope
      .attr("hash<oblong::plasma::Slaw>")
      .def(pybind11::init<>());
    TryAddDefaultCtor(handle);
  }
};

using Entity_oblong = Bind_oblong<>;
using Entity_oblong_plasma = Bind_oblong_plasma<>;
using Entity_oblong_plasma_OStreamReference = Bind_oblong_plasma_OStreamReference<>;
using Entity_std = Bind_std<>;
using Entity_std_hash6oblong_plasma_Protein9 = Bind_std_hash6oblong_plasma_Protein9<>;
using Entity_std_hash6oblong_plasma_Slaw9 = Bind_std_hash6oblong_plasma_Slaw9<>;

[[nodiscard]] CallUpdateGuard DeclFn(pybind11::module &m, const CustomBindingRegistry &registry) {
    auto v0 = CreateEntity<Entity_oblong>(EntityScope(m), registry);
    auto v1 = CreateEntity<Entity_oblong_plasma>(v0->AsScope(), registry);
    auto v2 = CreateEntity<Entity_oblong_plasma_OStreamReference>(v1->AsScope(), registry);
    auto v3 = CreateEntity<Entity_std>(EntityScope(m), registry);
    auto v4 = CreateEntity<Entity_std_hash6oblong_plasma_Protein9>(v3->AsScope(), registry);
    auto v5 = CreateEntity<Entity_std_hash6oblong_plasma_Slaw9>(v3->AsScope(), registry);
    return {update_fn};
}

} // namespace pybind11_weaver

#endif // CUSTOM_BINDINGS_H
template <class Pybind11T=pybind11::module_> struct Bind_oblong : public EntityBase {
  using Pybind11Type = Pybind11T;
   
  
  explicit Bind_oblong(EntityScope parent_h): handle{ parent_h.Get().def_submodule("oblong") }
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
template <class Pybind11T=pybind11::module_> struct Bind_oblong_plasma : public EntityBase {
  using Pybind11Type = Pybind11T;
   
  
  explicit Bind_oblong_plasma(EntityScope parent_h): handle{ parent_h.Get().def_submodule("plasma") }
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
template <class Pybind11T=pybind11::module_> struct Bind_std : public EntityBase {
  using Pybind11Type = Pybind11T;
   
  
  explicit Bind_std(EntityScope parent_h): handle{ parent_h.Get().def_submodule("std") }
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