from pathlib import Path
import numpy as np
from mpi4py import MPI
import dolfinx
from dolfinx import fem
from dolfinx.io import gmsh as dgmsh
from dolfinx.fem.petsc import LinearProblem
import ufl
import gmsh

# 1. Load Geometry and Generate Mesh using Gmsh
geo_path = Path(__file__).parent.parent / "cantilever.geo"

gmsh.initialize()
# Hide terminal logging from gmsh
gmsh.option.setNumber("General.Terminal", 0)
gmsh.open(str(geo_path))

# Query parameters from Gmsh ONELAB variables
E = gmsh.onelab.getNumber("Material/E")[0]
nu = gmsh.onelab.getNumber("Material/nu")[0]
mu = gmsh.onelab.getNumber("Material/mu")[0]
lambda_ = gmsh.onelab.getNumber("Material/lambda")[0]
traction_force = [
    gmsh.onelab.getNumber("Load/traction_force_x")[0],
    gmsh.onelab.getNumber("Load/traction_force_y")[0]
]

clamped_name = "clamped"
traction_name = "traction"

# Generate 2D mesh
gmsh.model.mesh.generate(2)

# Import Gmsh model to DOLFINx Mesh
mesh_data = dgmsh.model_to_mesh(gmsh.model, MPI.COMM_SELF, rank=0, gdim=2)
gmsh.finalize()

domain = mesh_data.mesh
facet_tags = mesh_data.facet_tags
physical_groups = mesh_data.physical_groups

# print info about the loaded mesh and parameters
print("Mesh loaded successfully!")
print(f"Topology dimension: {domain.topology.dim}")
print(f"Geometry dimension: {domain.geometry.dim}")
print(f"Physical groups available: {list(physical_groups.keys())}")
print(f"Material Constants: E = {E}, nu = {nu}")
print(f"Lame parameters: mu = {mu:.3f}, lambda = {lambda_:.3f}")
print(f"Traction force: {traction_force}")

# # 3. Vector Function Space for Displacements
# V = fem.functionspace(domain, ("Lagrange", 1, (domain.geometry.dim,)))
# 
# # 4. Dirichlet Boundary Condition (Clamped boundary)
# clamped_tag = physical_groups[clamped_name].tag
# clamped_facets = facet_tags.find(clamped_tag)
# left_dofs = fem.locate_dofs_topological(V, facet_tags.dim, clamped_facets)
# 
# # Clamp both displacements (u_x, u_y) to 0
# bc_left = fem.dirichletbc(np.array([0.0, 0.0], dtype=np.float64), left_dofs, V)
# bcs = [bc_left]
# 
# # 5. Neumann Boundary Condition (Traction boundary)
# traction_tag = physical_groups[traction_name].tag
# ds = ufl.Measure("ds", domain=domain, subdomain_data=facet_tags, subdomain_id=traction_tag)
# T = fem.Constant(domain, np.array(traction_force, dtype=np.float64))
# 
# # 6. Material Constitutive Law (Plane Strain)
# def epsilon(u):
#     return ufl.sym(ufl.grad(u))
# 
# def sigma(u):
#     return lambda_ * ufl.div(u) * ufl.Identity(len(u)) + 2.0 * mu * epsilon(u)
# 
# # 7. Variational Form
# u = ufl.TrialFunction(V)
# v = ufl.TestFunction(V)
# 
# a = ufl.inner(sigma(u), epsilon(v)) * ufl.dx
# L_form = ufl.inner(T, v) * ds
# 
# # 8. Solve the Linear System
# problem = LinearProblem(
#     a, L_form, bcs=bcs,
#     petsc_options_prefix="cantilever",
#     petsc_options={"ksp_type": "preonly", "pc_type": "lu"}
# )
# uh = problem.solve()
# 
# # 9. Output Verification
# u_values = uh.x.array.reshape(-1, domain.geometry.dim)
# max_disp_y = np.min(u_values[:, 1])  # Maximum downward deflection
# print("\nDOLFINx 2D Cantilever Beam (Gmsh-driven) Solver")
# print(f"Maximum tip deflection (u_y): {max_disp_y:.6f}")
