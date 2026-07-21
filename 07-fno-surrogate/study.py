import dolfinx
from mpi4py import MPI
from dolfinx import mesh, fem
from dolfinx.fem.petsc import LinearProblem
import ufl
import numpy as np

# 1. Mesh and Function Space
# Interval domain from 0 to 1 with 20 elements
nx = 20
domain = mesh.create_interval(MPI.COMM_SELF, nx, [0.0, 1.0])
V = fem.functionspace(domain, ("Lagrange", 1))

# 2. Boundary Conditions: u(0) = 0, u(1) = 0
def left_boundary(x):
    return np.isclose(x[0], 0.0)

def right_boundary(x):
    return np.isclose(x[0], 1.0)

left_facets = mesh.locate_entities_boundary(domain, domain.topology.dim - 1, left_boundary)
right_facets = mesh.locate_entities_boundary(domain, domain.topology.dim - 1, right_boundary)

left_dofs = fem.locate_dofs_topological(V, domain.topology.dim - 1, left_facets)
right_dofs = fem.locate_dofs_topological(V, domain.topology.dim - 1, right_facets)

bc_left = fem.dirichletbc(0.0, left_dofs, V)
bc_right = fem.dirichletbc(0.0, right_dofs, V)
bcs = [bc_left, bc_right]

# 3. Variational Form: -u'' = 1
u = ufl.TrialFunction(V)
v = ufl.TestFunction(V)
f = fem.Constant(domain, 1.0)

a = ufl.inner(ufl.grad(u), ufl.grad(v)) * ufl.dx
L = f * v * ufl.dx

# 4. Solve the Linear System
problem = LinearProblem(a, L, bcs=bcs, petsc_options_prefix="poisson", petsc_options={"ksp_type": "preonly", "pc_type": "lu"})
uh = problem.solve()

# 5. Output Verification
x_coords = domain.geometry.x[:, 0]
u_solved = uh.x.array
analytical = 0.5 * x_coords * (1.0 - x_coords)
max_error = np.max(np.abs(u_solved - analytical))

print("DOLFINx 1D Poisson Solver")
print(f"Max error vs analytical: {max_error:.2e}")
