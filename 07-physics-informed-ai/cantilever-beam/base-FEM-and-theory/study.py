from pathlib import Path
from utils import load_gmsh_cantilever

# 1. Load Geometry and Generate Mesh using Gmsh via shared utility
geo_path = Path(__file__).parent.parent / "cantilever.geo"
domain, cell_tags, facet_tags, physical_groups, params, dirichlet_bcs, neumann_loads = load_gmsh_cantilever(geo_path)

# # 3. Vector Function Space for Displacements
# from dolfinx import fem
# import ufl
# import numpy as np
# from dolfinx.fem.petsc import LinearProblem
# 
# V = fem.functionspace(domain, ("Lagrange", 1, (domain.geometry.dim,)))
# 
# # 4. Dirichlet Boundary Condition
# bcs = []
# for name, values in dirichlet_bcs.items():
#     if name in physical_groups:
#         tag = physical_groups[name].tag
#         facets = facet_tags.find(tag)
#         dofs = fem.locate_dofs_topological(V, facet_tags.dim, facets)
#         bc = fem.dirichletbc(np.array(values, dtype=np.float64), dofs, V)
#         bcs.append(bc)
# 
# # 5. Neumann Boundary Condition (Traction boundary)
# for name, force in neumann_loads.items():
#     if name in physical_groups:
#         tag = physical_groups[name].tag
#         ds = ufl.Measure("ds", domain=domain, subdomain_data=facet_tags, subdomain_id=tag)
#         T = fem.Constant(domain, np.array(force, dtype=np.float64))
# 
# # 6. Material Constitutive Law (Plane Strain)
# mu = params["mu"]
# lambda_ = params["lambda"]
# 
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
# print(f"Maximum tip deflection (u_y): {max_disp_y:.6f}")
