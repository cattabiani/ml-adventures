# 2D Cantilever Beam (Plane Strain) Theory

This document outlines the governing equations and boundary conditions for a 2D cantilever beam modeled under the plane strain assumption.

---

## Governing Equations

We consider a 2D elastic body in the x-y plane. Under the **plane strain** assumption, the out-of-plane strain components are zero:

* $\varepsilon_{zz} = 0$
* $\varepsilon_{xz} = 0$
* $\varepsilon_{yz} = 0$

The thickness in the z-direction is assumed to be very large (infinitely thick) and constrained.

### 1. Strain-Displacement Relationship
The in-plane strain tensor $\varepsilon$ is defined in terms of the displacement vector $\mathbf{u} = (u_x, u_y)$ as:

$$\varepsilon(\mathbf{u}) = \frac{1}{2}(\nabla\mathbf{u} + (\nabla\mathbf{u})^T)$$

In component form:

$$\varepsilon_{xx} = \frac{\partial u_x}{\partial x}$$

$$\varepsilon_{yy} = \frac{\partial u_y}{\partial y}$$

$$\varepsilon_{xy} = \frac{1}{2}\left(\frac{\partial u_x}{\partial y} + \frac{\partial u_y}{\partial x}\right)$$

### 2. Constitutive Equations (Hooke's Law)
For an isotropic elastic material under plane strain, the stress tensor $\sigma$ is related to the strain tensor $\varepsilon$ by:

$$\sigma(\mathbf{u}) = \lambda \text{div}(\mathbf{u})\mathbf{I} + 2\mu\varepsilon(\mathbf{u})$$

where:
* $\mathbf{I}$ is the 2D identity tensor.
* $\text{div}(\mathbf{u}) = \frac{\partial u_x}{\partial x} + \frac{\partial u_y}{\partial y}$ is the divergence of displacement.
* $\lambda$ and $\mu$ are the Lame constants.

The Lame constants are computed from Young's Modulus ($E$) and Poisson's ratio ($\nu$):

$$\mu = \frac{E}{2(1 + \nu)}$$

$$\lambda = \frac{E\nu}{(1 + \nu)(1 - 2\nu)}$$

Under these conditions, the out-of-plane normal stress is non-zero:

$$\sigma_{zz} = \nu(\sigma_{xx} + \sigma_{yy})$$

### 3. Equilibrium Equation
In the absence of body forces, the equilibrium equation is:

$$\text{div}(\sigma(\mathbf{u})) = \mathbf{0}$$

which in component form is:

$$\frac{\partial \sigma_{xx}}{\partial x} + \frac{\partial \sigma_{xy}}{\partial y} = 0$$

$$\frac{\partial \sigma_{yx}}{\partial x} + \frac{\partial \sigma_{yy}}{\partial y} = 0$$

---

## Boundary Conditions

We model a rectangular domain of length $L$ and height $H$:
* Domain $\Omega = [0, L] \times [0, H]$

Under the assumption of **small deformations** (infinitesimal strain theory), boundary conditions are formulated and integrated in the reference (undeformed) configuration. Therefore, the boundary normals and shapes are assumed to remain constant during deformation.

### 1. Clamped Boundary (Left Edge at $x = 0$)
The displacement is completely constrained:
* $u_x(0, y) = 0$
* $u_y(0, y) = 0$

### 2. Traction Boundary (Right Edge at $x = L$)
A downward vertical shear load is applied to the tip. The traction vector $\mathbf{T}$ is:
* $\mathbf{T} = (0, -F_y)$
where $F_y$ is the force per unit length.

This boundary condition is:
* $\sigma \mathbf{n} = \mathbf{T}$  at $x = L$
where $\mathbf{n} = (1, 0)$ is the outward normal vector.

### 3. Free Boundaries (Top at $y = H$ and Bottom at $y = 0$)
No external forces are applied to the top or bottom surfaces:
* $\sigma \mathbf{n} = \mathbf{0}$
