# 2D Cantilever Beam (Plane Strain) Theory

This document outlines the governing equations and boundary conditions for a 2D cantilever beam modeled under the plane strain assumption.

---

## Governing Equations

We consider a 2D elastic body in the x-y plane. Under the **plane strain** assumption, the out-of-plane strain components are zero because the thickness in the z-direction is assumed to be very large and constrained:

* ε<sub>zz</sub> = 0
* ε<sub>xz</sub> = 0
* ε<sub>yz</sub> = 0

### 1. Strain-Displacement Relationship
The in-plane strain tensor **ε** is defined in terms of the displacement vector **u** = (u<sub>x</sub>, u<sub>y</sub>) as:

* **ε**(**u**) = 0.5 * (∇**u** + ∇**u**<sup>T</sup>)

In component form:

```
               ∂u_x
  ε_xx   =  --------
               ∂x

               ∂u_y
  ε_yy   =  --------
               ∂y

             1   /  ∂u_x      ∂u_y  \
  ε_xy   =  --- | ------  +  ------ |
             2   \  ∂y        ∂x    /
```

### 2. Constitutive Equations (Hooke's Law)
For an isotropic elastic material under plane strain, the stress tensor **σ** is related to the strain tensor **ε** by:

* **σ**(**u**) = λ * div(**u**) * **I** + 2 * μ * **ε**(**u**)

where:
* **I** is the 2D identity tensor.
* div(**u**) = ε<sub>xx</sub> + ε<sub>yy</sub> is the divergence of displacement (volume change).
* λ (lambda) and μ (mu) are the Lame constants.

The Lame constants are computed from Young's Modulus (E) and Poisson's ratio (ν):

```
                 E
  μ     =  -------------
             2 * (1 + ν)

                 E * ν
  λ     =  -----------------------
             (1 + ν) * (1 - 2 * ν)
```

Under these conditions, the out-of-plane normal stress is non-zero:
* σ<sub>zz</sub> = ν * (σ<sub>xx</sub> + σ<sub>yy</sub>)

### 3. Equilibrium Equation
In the absence of body forces, the momentum balance/equilibrium equation is:

* div(**σ**(**u**)) = **0**

which in components translates to:

```
   ∂σ_xx      ∂σ_xy
  -------  + -------  =  0
    ∂x         ∂y

   ∂σ_yx      ∂σ_yy
  -------  + -------  =  0
    ∂x         ∂y
```

---

## Boundary Conditions

The domain is a rectangular beam of length L and height H:
* Domain Ω = [0, L] x [0, H]

### 1. Clamped Boundary (Left Edge at x = 0)
The displacement is completely fixed:
* u<sub>x</sub>(0, y) = 0
* u<sub>y</sub>(0, y) = 0

### 2. Traction Boundary (Right Edge at x = L)
A downward vertical shear load is applied to the tip. The traction vector **T** is:
* **T** = (0, -F<sub>y</sub>)
where F<sub>y</sub> is the force per unit area.

This boundary condition is:
* **σ** * **n** = **T**  at x = L
where **n** = (1, 0) is the outward normal vector.

### 3. Free Boundaries (Top at y = H and Bottom at y = 0)
No external forces are applied to the top or bottom surfaces:
* **σ** * **n** = **0**
