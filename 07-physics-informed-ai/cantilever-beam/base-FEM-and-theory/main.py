"""
2D cantilever beam, linear elasticity, plane strain -- solved with dolfinx.

Geometry, material params, and BC/load values are all defined in
`cantilever.geo` and loaded through `utils.load_gmsh_cantilever`.
See `theory.md` for the governing equations this script is expected to solve.

This is a learning exercise (see TASKS.md at the project root) -- fill in the
TODOs yourself. `utils.load_gmsh_cantilever` already gives you everything you
need to get started (mesh, tags, physical groups, material params, BC/load
dicts).
"""
from pathlib import Path

import ufl
from dolfinx import fem
from dolfinx.fem.petsc import LinearProblem

from utils import load_gmsh_cantilever


def epsilon(u):
    return ufl.sym(ufl.grad(u))

def sigma(u, lambda_, mu):
    return lambda_ * ufl.div(u) * ufl.Identity(len(u)) + 2*mu*epsilon(u)



def run_simulation():
    # 1. Load geometry and mesh via the shared gmsh utility.
    geo_path = Path(__file__).parent.parent / "cantilever.geo"
    domain, cell_tags, facet_tags, physical_groups, params, dirichlet_bcs, neumann_loads = (
        load_gmsh_cantilever(geo_path)
    )
    dim = domain.geometry.dim

    V = fem.functionspace(domain, ("CG", 1, (dim,)))

    bcs = []
    for bc, vals in dirichlet_bcs.items():
        tag = physical_groups[bc].tag
        facets = facet_tags.find(tag)
        dofs = fem.locate_dofs_topological(V, dim-1, facets)
        bcs.append(fem.dirichletbc(vals, dofs, V))


    u, v = ufl.TrialFunction(V), ufl.TestFunction(V)
    L_form = 0
    for bc, vals in neumann_loads.items():
        tag = physical_groups[bc].tag
        ds = ufl.Measure(integral_type="ds", domain=domain, subdomain_data=facet_tags, subdomain_id=tag)
        L_form += ufl.inner(fem.Constant(domain, vals), v) * ds

    a = ufl.inner(sigma(u, lambda_ = params["lambda"], mu = params["mu"]), epsilon(v)) * ufl.dx

    lp = LinearProblem(a=a, L=L_form, bcs=bcs, petsc_options_prefix="cantilever", petsc_options={"ksp_type": "preonly", "pc_type": "lu"})

    uh = lp.solve()

    print(min(uh.x.array.reshape((-1, dim))[:, 1]))


    return uh


if __name__ == "__main__":
    uh = run_simulation()
