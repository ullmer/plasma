# Bridge/Beam demo
# By CoPilot and Brygg Ullmer, Clemson University
# Begun 2026-06-07

import FreeCAD as App
import Part
import ObjectsFem
import FemGui

doc = App.newDocument("BridgeDemo")

# --- Geometry: simple beam ---
beam = doc.addObject("Part::Box", "Beam")
beam.Length = 300
beam.Width = 30
beam.Height = 30

support1 = doc.addObject("Part::Box", "Support1")
support1.Length = 30
support1.Width = 30
support1.Height = 50
support1.Placement.Base = App.Vector(0, 0, -50)

support2 = doc.addObject("Part::Box", "Support2")
support2.Length = 30
support2.Width = 30
support2.Height = 50
support2.Placement.Base = App.Vector(270, 0, -50)

doc.recompute()
mesh.createMesh()

# --- FEM analysis container ---
analysis = ObjectsFem.makeAnalysis(doc, "Analysis")

# --- Material (generic steel) ---
material = ObjectsFem.makeMaterialSolid(doc, "Steel")
material.Material = {
  "Name": "Steel",
  "YoungsModulus": "210000 MPa",
  "PoissonRatio": "0.30",
}
analysis.addObject(material)

# --- Solver ---
solver = ObjectsFem.makeSolverCalculixCcxTools(doc, "Solver")
analysis.addObject(solver)

# --- Constraint: fix left face ---
fixed = ObjectsFem.makeConstraintFixed(doc, "Fixed")
fixed.References = [(beam, "Face1")]  # one end
analysis.addObject(fixed)

# --- Constraint: fix right face ---
fixed2 = ObjectsFem.makeConstraintFixed(doc, "Fixed2")
fixed2.References = [(beam, "Face2")]  # other end
analysis.addObject(fixed2)

# --- Force: downward load on top face ---
force = ObjectsFem.makeConstraintForce(doc, "Force")
force.References = [(beam, "Face5")]  # top face
force.Force = 1000.0
force.Direction = App.Vector(0, 0, -1)
analysis.addObject(force)

# --- Mesh ---
mesh = ObjectsFem.makeMeshGmsh(doc, "Mesh")
mesh.Part = beam
mesh.CharacteristicLengthMax = 20
analysis.addObject(mesh)

doc.recompute()

# --- Solve ---
FemGui.setActiveAnalysis(analysis)
FemGui.runCalculix()

# --- Show results ---
for obj in doc.Objects:
  if "ResultObject" in obj.Name:
    FemGui.openResultObject(obj)
    FemGui.setActiveAnalysis(analysis)
    break

### end ###
