import dolfinx
from mpi4py import MPI
from dolfinx import mesh, fem
from dolfinx.fem.petsc import LinearProblem
import ufl
import numpy as np

# 1. Mesh and Vector Function Space
# Rectangular domain L x H using quadrilateral elements
L = 2.0
H = 0.5
nx = 40
ny = 10

domain = mesh.create_rectangle(
    MPI.COMM_SELF,
    [[0.0, 0.0], [L, H]],
    [nx, ny],
    mesh.CellType.quadrilateral
)

V = fem.functionspace(domain, ("Lagrange", 1, (domain.geometry.dim,)))

# 2. Dirichlet Boundary Condition: Clamped at x = 0
def left_boundary(x):
    return np.isclose(x[0], 0.0)

left_facets = mesh.locate_entities_boundary(domain, domain.topology.dim - 1, left_boundary)
left_dofs = fem.locate_dofs_topological(V, domain.topology.dim - 1, left_facets)

# Clamp both displacements (u_x, u_y) to 0
bc_left = fem.dirichletbc(np.array([0.0, 0.0], dtype=np.float64), left_dofs, V)
bcs = [bc_left]

# 3. Neumann Boundary Condition: Traction T = (0, -1.0) at x = L
def right_boundary(x):
    return np.isclose(x[0], L)

right_facets = mesh.locate_entities_boundary(domain, domain.topology.dim - 1, right_boundary)
facet_indices = np.array(right_facets, dtype=np.int32)
facet_values = np.ones(len(right_facets), dtype=np.int32)
facet_tags = mesh.meshtags(domain, domain.topology.dim - 1, facet_indices, facet_values)

ds = ufl.Measure("ds", domain=domain, subdomain_data=facet_tags, subdomain_id=1)
T = fem.Constant(domain, np.array([0.0, -1.0], dtype=np.float64))

# 4. Material Constitutive Law (Plane Strain)
E = 1000.0
nu = 0.3

mu = E / (2.0 * (1.0 + nu))
lambda_ = E * nu / ((1.0 + nu) * (1.0 - 2.0 * nu))

def epsilon(u):
    return ufl.sym(ufl.grad(u))

def sigma(u):
    return lambda_ * ufl.div(u) * ufl.Identity(len(u)) + 2.0 * mu * epsilon(u)

# 5. Variational Form
u = ufl.TrialFunction(V)
v = ufl.TestFunction(V)

a = ufl.inner(sigma(u), epsilon(v)) * ufl.dx
L_form = ufl.inner(T, v) * ds

# 6. Solve the Linear System
problem = LinearProblem(a, L_form, bcs=bcs, petsc_options_prefix="cantilever", petsc_options={"ksp_type": "preonly", "pc_type": "lu"})
uh = problem.solve()

# 7. Print the results
# Retrieve displacement values
u_values = uh.x.array.reshape(-1, domain.geometry.dim)
max_disp_y = np.min(u_values[:, 1])  # Min value (maximum downward deflection)
print("DOLFINx 2D Cantilever Beam (Plane Strain) Solver")
print(f"Maximum tip deflection (u_y): {max_disp_y:.6f}")
