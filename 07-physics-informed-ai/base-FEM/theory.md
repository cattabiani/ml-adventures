# 2D Cantilever Beam (Plane Strain) Theory

This document outlines the governing equations and boundary conditions for a 2D cantilever beam modeled under the plane strain assumption.

## Governing Equations

We consider a 2D elastic body in the x-y plane. Under the plane strain assumption, the out-of-plane strain components are zero:
* epsilon_zz = 0
* epsilon_xz = 0
* epsilon_yz = 0

The thickness in the z-direction is assumed to be very large (infinitely thick) and constrained.

### 1. Strain-Displacement Relationship
The in-plane strain tensor epsilon is defined in terms of the displacement vector u = (u_x, u_y) as:
* epsilon(u) = 0.5 * (grad(u) + grad(u)^T)

In component form:
* epsilon_xx = du_x / dx
* epsilon_yy = du_y / dy
* epsilon_xy = 0.5 * (du_x / dy + du_y / dx)

### 2. Constitutive Equations (Hooke's Law)
For an isotropic elastic material under plane strain, the stress tensor sigma is related to the strain tensor epsilon by:
* sigma(u) = lambda * div(u) * I + 2 * mu * epsilon(u)

where:
* I is the 2D identity tensor.
* div(u) = du_x / dx + du_y / dy is the divergence of displacement.
* lambda and mu are the Lame constants.

The Lame constants are computed from Young's Modulus (E) and Poisson's ratio (nu):
* mu = E / (2 * (1 + nu))
* lambda = E * nu / ((1 + nu) * (1 - 2 * nu))

Under these conditions, the out-of-plane normal stress is non-zero:
* sigma_zz = nu * (sigma_xx + sigma_yy)

### 3. Equilibrium Equation
In the absence of body forces, the equilibrium equation is:
* div(sigma(u)) = 0

---

## Boundary Conditions

We model a rectangular domain of length L and height H:
* Domain = [0, L] x [0, H]

### 1. Clamped Boundary (Left Edge)
At the left edge (x = 0), the displacement is completely constrained:
* u_x(0, y) = 0
* u_y(0, y) = 0

### 2. Traction Boundary (Right Edge)
At the right edge (x = L), a downward shear load/force is applied. The traction vector T is:
* T = (0, -F_y)
where F_y is the force per unit area.

This implies:
* sigma_xx * n_x + sigma_xy * n_y = 0
* sigma_yx * n_x + sigma_yy * n_y = -F_y
where n = (1, 0) is the outward normal vector on the right boundary.

### 3. Free Boundaries (Top and Bottom Edges)
At the top (y = H) and bottom (y = 0) edges, there are no external forces:
* T = (0, 0)
