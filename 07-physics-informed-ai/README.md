# 07 — Physics-Informed AI

Building toward Physics-Informed Neural Networks (PINNs) by first getting
solid on the classical numerics they're compared against and blended with:
the Finite Element Method (FEM).

## Projects

### `cantilever-beam/`
2D cantilever beam under a tip shear load, linear elasticity, plane strain.
Solved with [dolfinx](https://github.com/FEniCS/dolfinx) (FEniCSx). The goal
here isn't the beam itself -- it's a vehicle for learning the dolfinx
workflow: mesh import from Gmsh, function spaces, boundary conditions
(Dirichlet + Neumann), variational forms, and solving.

- `cantilever.geo` -- Gmsh geometry/mesh script; also defines material
  parameters and BC/load values via ONELAB.
- `base-FEM-and-theory/theory.md` -- governing equations (strain-displacement,
  Hooke's law for plane strain, equilibrium) and boundary conditions.
- `base-FEM-and-theory/utils.py` -- shared helper to load the `.geo` file,
  mesh it via Gmsh, and import it into dolfinx (`load_gmsh_cantilever`).
- `base-FEM-and-theory/main.py` -- the dolfinx solve itself. Currently a
  skeleton with TODOs (see `TASKS.md`) -- this is where the actual learning
  happens.

## Status
- [x] Geometry + mesh pipeline (Gmsh -> dolfinx) via `utils.py`
- [ ] `main.py` dolfinx solve (in progress, see `TASKS.md`)
- [ ] Validate against Euler-Bernoulli beam theory
- [ ] PINN version of the same problem, compared against FEM
