from pathlib import Path
import numpy as np
from dolfinx import fem
from dolfinx.fem.petsc import LinearProblem
import ufl
from utils import load_gmsh_cantilever

def run_simulation():
    # 1. Load Geometry and Generate Mesh using Gmsh via shared utility
    geo_path = Path(__file__).parent.parent / "cantilever.geo"
    domain, cell_tags, facet_tags, physical_groups, params, dirichlet_bcs, neumann_loads = load_gmsh_cantilever(geo_path)

    # 2. Vector Function Space for Displacements
    V = fem.functionspace(domain, ("Lagrange", 1, (domain.geometry.dim,)))

    # 3. Dirichlet Boundary Condition
    bcs = []
    for name, values in dirichlet_bcs.items():
        if name in physical_groups:
            tag = physical_groups[name].tag
            facets = facet_tags.find(tag)
            dofs = fem.locate_dofs_topological(V, facet_tags.dim, facets)
            bc = fem.dirichletbc(np.array(values, dtype=np.float64), dofs, V)
            bcs.append(bc)

    # 4. Neumann Boundary Condition (Traction boundary)
    v = ufl.TestFunction(V)
    L_contributions = []
    for name, force in neumann_loads.items():
        if name in physical_groups:
            tag = physical_groups[name].tag
            ds = ufl.Measure("ds", domain=domain, subdomain_data=facet_tags, subdomain_id=tag)
            T = fem.Constant(domain, np.array(force, dtype=np.float64))
            L_contributions.append(ufl.inner(T, v) * ds)
    
    if L_contributions:
        L_form = sum(L_contributions)
    else:
        # Fallback to zero force if no loads are specified
        L_form = ufl.inner(fem.Constant(domain, np.array([0.0, 0.0], dtype=np.float64)), v) * ufl.dx

    # 5. Material Constitutive Law (Plane Strain)
    mu = params["mu"]
    lambda_ = params["lambda"]

    def epsilon(u_val):
        return ufl.sym(ufl.grad(u_val))

    def sigma(u_val):
        return lambda_ * ufl.div(u_val) * ufl.Identity(len(u_val)) + 2.0 * mu * epsilon(u_val)

    # 6. Variational Form
    u = ufl.TrialFunction(V)
    a = ufl.inner(sigma(u), epsilon(v)) * ufl.dx

    # 7. Solve the Linear System
    problem = LinearProblem(
        a, L_form, bcs=bcs,
        petsc_options_prefix="cantilever",
        petsc_options={"ksp_type": "preonly", "pc_type": "lu"}
    )
    uh = problem.solve()

    # 8. Output Verification
    u_values = uh.x.array.reshape(-1, domain.geometry.dim)
    max_disp_y = np.min(u_values[:, 1])  # Maximum downward deflection
    print(f"\nSimulation run complete.")
    print(f"Maximum tip deflection (u_y): {max_disp_y:.6f}")
    
    return uh

if __name__ == "__main__":
    run_simulation()
