# Tasks — 07 Physics-Informed AI

## cantilever-beam / base-FEM-and-theory

Objective: get comfortable with the dolfinx API by implementing the linear
elasticity solve for the cantilever beam described in `theory.md`. The mesh
loading is done for you (`utils.load_gmsh_cantilever`) -- everything from
the function space onward is yours to write in `main.py`.

- [ ] **Function space**: create a vector-valued Lagrange space on `domain`
      for the displacement field. What degree makes sense for a first pass?
- [ ] **Dirichlet BCs**: convert the `dirichlet_bcs` dict into
      `fem.dirichletbc` objects using `physical_groups` + `facet_tags`.
      Think about what `locate_dofs_topological` needs.
- [ ] **Neumann BCs**: turn `neumann_loads` into traction terms in the linear
      form, integrated over the correct boundary measure.
- [ ] **Constitutive law**: implement `epsilon(u)` and `sigma(u)` for plane
      strain from `theory.md`. Double check the Lame parameters `mu` and
      `lambda` are being used, not `E`/`nu` directly.
- [ ] **Variational form + solve**: assemble `a(u, v)`, build `LinearProblem`,
      solve.
- [ ] **Sanity check**: compute the max tip deflection and compare it against
      the Euler-Bernoulli beam theory estimate for the same `L`, `H`, `E`,
      and tip load. How close is plane-strain FEM expected to be, and why
      might it differ?
- [ ] **(stretch)** Visualize the deformed mesh / displacement field (e.g.
      via PyVista) instead of just printing a scalar.
- [ ] **(stretch)** Try a second-order (`"Lagrange", 2, ...`) space and see
      how much the tip deflection estimate moves -- gives you a feel for
      mesh/order convergence.

## Later
- [ ] Set up a PINN for the same cantilever problem and compare against the
      FEM solution from this exercise.
