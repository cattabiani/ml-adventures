# Principle of Virtual Work for a Cantilever Beam

You have a cantilever beam modeled with two degrees of freedom (e.g., displacement $v$ and rotation $\theta$), and you are stuck with 2 unknowns but only 1 equation. 

The issue is a common conceptual mix-up: you are likely equating the **actual** work (or thinking of virtual work as a single scalar equation), whereas the Principle of Virtual Work (PVW) operates on **virtual variations** which are arbitrary and independent.

Here is the breakdown of why you actually have 2 equations.

---

## 1. Actual Work vs. Virtual Work

If you write the conservation of energy (Clapeyron's theorem) for actual displacements:

$$W_{\text{ext}} = W_{\text{int}}$$

This is indeed **1 equation** for **2 unknowns**, making it underdetermined. This equation only guarantees that the total energy is balanced, but it does not specify the equilibrium path.

However, the **Principle of Virtual Work** states that the virtual work done by external forces must equal the virtual work done by internal forces for **any arbitrary virtual displacement field** that is kinematically admissible:

$$\delta W_{\text{ext}} = \delta W_{\text{int}}$$

where $\delta$ represents a virtual, infinitesimal variation.

---

## 2. Setting Up the Virtual Work Equation

Let's assume your two independent unknowns are:
- $v$: Deflection (displacement) at the tip
- $\theta$: Rotation (angle) at the tip

The corresponding virtual variations are $\delta v$ and $\delta \theta$. These variations are **completely independent and arbitrary**.

The virtual work of the external forces (e.g., a point force $F$ and a moment $M$ at the tip) is:

$$\delta W_{\text{ext}} = F \delta v + M \delta \theta$$

The virtual work of the internal forces/moments (due to structural stiffness or internal stresses) can be written generally as:

$$\delta W_{\text{int}} = R_v(v, \theta) \delta v + R_{\theta}(v, \theta) \delta \theta$$

where $R_v(v, \theta)$ and $R_{\theta}(v, \theta)$ are the internal resistance forces/moments as functions of the actual displacement $v$ and rotation $\theta$.

Equating the two:

$$F \delta v + M \delta \theta = R_v(v, \theta) \delta v + R_{\theta}(v, \theta) \delta \theta$$

Rearranging:

$$[ F - R_v(v, \theta) ] \delta v + [ M - R_{\theta}(v, \theta) ] \delta \theta = 0$$

---

## 3. Resolving the 2 Unknowns (The "Magic" of PVW)

Since the virtual variations $\delta v$ and $\delta \theta$ are **arbitrary and independent**, the equation above must hold for **any** choice of $\delta v$ and $\delta \theta$. 

Specifically:
1. If we choose a virtual state where $\delta v$ is non-zero but $\delta \theta = 0$, we get:
   $$F - R_v(v, \theta) = 0$$
2. If we choose a virtual state where $\delta v = 0$ but $\delta \theta$ is non-zero, we get:
   $$M - R_{\theta}(v, \theta) = 0$$

This gives you exactly **2 independent equations** for your **2 unknowns** ($v$ and $\theta$):

$$\text{Equation 1: } R_v(v, \theta) = F$$
$$\text{Equation 2: } R_{\theta}(v, \theta) = M$$

---

## 4. Example: Rayleigh-Ritz and Kinematic Coupling

If you are using Euler-Bernoulli beam theory, the rotation is not independent of displacement:

$$\theta(x) = \frac{dv(x)}{dx}$$

If you approximate the displacement along the beam $w(x)$ using two shape functions $\phi_1(x)$ and $\phi_2(x)$:

$$w(x) = c_1 \phi_1(x) + c_2 \phi_2(x)$$

Then the rotation is:

$$\theta(x) = c_1 \phi'_1(x) + c_2 \phi'_2(x)$$

Here, your two unknowns are not $w$ and $\theta$ at a point, but the coefficients $c_1$ and $c_2$. 

The virtual variations are:

$$\delta w(x) = \delta c_1 \phi_1(x) + \delta c_2 \phi_2(x)$$

Which again provides 2 equations for the 2 unknown coefficients.

---

## 5. Specific 2D Case: Stress-Strain Formulation ($M = 0$)

You are correct that the internal virtual work is formulated using the stress ($\boldsymbol{\sigma}$) and virtual strain ($\delta \boldsymbol{\varepsilon}$) tensors. In 2D plane strain, this is written in vector/matrix format as:

$$\delta W_{\text{int}} = \int_{\Omega} \delta \boldsymbol{\varepsilon}^T \boldsymbol{\sigma} \, d\Omega$$

where the stress and strain vectors are:

$$\boldsymbol{\sigma} = \begin{bmatrix} \sigma_{xx} \\ \sigma_{yy} \\ \sigma_{xy} \end{bmatrix}, \quad \boldsymbol{\varepsilon} = \begin{bmatrix} \varepsilon_{xx} \\ \varepsilon_{yy} \\ 2\varepsilon_{xy} \end{bmatrix}$$

Using the plane strain constitutive matrix $\mathbf{C}$ (Hooke's law: $\boldsymbol{\sigma} = \mathbf{C} \boldsymbol{\varepsilon}$):

$$\mathbf{C} = \frac{E}{(1+\nu)(1-2\nu)} \begin{bmatrix} 1-\nu & \nu & 0 \\ \nu & 1-\nu & 0 \\ 0 & 0 & \frac{1-2\nu}{2} \end{bmatrix}$$

$$\delta W_{\text{int}} = \int_{\Omega} \delta \boldsymbol{\varepsilon}^T \mathbf{C} \boldsymbol{\varepsilon} \, d\Omega$$

### Connecting the Fields to the Unknowns ($v, \theta$)

Suppose you parameterize the displacement field $\mathbf{u} = [u_x, u_y]^T$ using your two unknowns $\mathbf{q} = [v, \theta]^T$:

$$\mathbf{u}(x, y) = \mathbf{H}_v(x, y) v + \mathbf{H}_{\theta}(x, y) \theta$$

By taking spatial derivatives, the strain vector is related to the unknowns via the strain-displacement matrices $\mathbf{B}_v$ and $\mathbf{B}_{\theta}$:

$$\boldsymbol{\varepsilon}(x, y) = \mathbf{B}_v(x, y) v + \mathbf{B}_{\theta}(x, y) \theta$$

The virtual strain is:

$$\delta \boldsymbol{\varepsilon} = \mathbf{B}_v \delta v + \mathbf{B}_{\theta} \delta \theta$$

### Formulating the Resistance Terms

Substitute the virtual strain and actual strain into the internal virtual work expression:

$$\delta W_{\text{int}} = \int_{\Omega} (\mathbf{B}_v \delta v + \mathbf{B}_{\theta} \delta \theta)^T \mathbf{C} (\mathbf{B}_v v + \mathbf{B}_{\theta} \theta) \, d\Omega$$

Expanding this yields:

$$\delta W_{\text{int}} = \delta v \left[ \left( \int_{\Omega} \mathbf{B}_v^T \mathbf{C} \mathbf{B}_v \, d\Omega \right) v + \left( \int_{\Omega} \mathbf{B}_v^T \mathbf{C} \mathbf{B}_{\theta} \, d\Omega \right) \theta \right] + \delta \theta \left[ \left( \int_{\Omega} \mathbf{B}_{\theta}^T \mathbf{C} \mathbf{B}_v \, d\Omega \right) v + \left( \int_{\Omega} \mathbf{B}_{\theta}^T \mathbf{C} \mathbf{B}_{\theta} \, d\Omega \right) \theta \right]$$

This gives the linear resistance functions:

$$R_v(v, \theta) = K_{vv} v + K_{v\theta} \theta$$
$$R_{\theta}(v, \theta) = K_{\theta v} v + K_{\theta\theta} \theta$$

where the stiffness coefficients $K_{ij}$ are the integrals:

$$K_{ij} = \int_{\Omega} \mathbf{B}_i^T \mathbf{C} \mathbf{B}_j \, d\Omega$$

### Solving the System with $M = 0$

With an external load force $F$ and moment $M = 0$ at the tip:

$$\delta W_{\text{ext}} = F \delta v + 0 \delta \theta$$

Equating $\delta W_{\text{ext}} = \delta W_{\text{int}}$ and setting the coefficients of the independent variations $\delta v$ and $\delta \theta$ to zero yields:

$$\begin{aligned}
K_{vv} v + K_{v\theta} \theta &= F \\
K_{\theta v} v + K_{\theta\theta} \theta &= 0
\end{aligned}$$

Since $K_{\theta v} = K_{v\theta}$ (by symmetry of $\mathbf{C}$), the second equation allows you to express the rotation in terms of displacement:

$$\theta = -\frac{K_{\theta v}}{K_{\theta\theta}} v$$

Substituting this back into the first equation allows you to solve for the displacement $v$ directly:

$$\left( K_{vv} - \frac{K_{v\theta} K_{\theta v}}{K_{\theta\theta}} \right) v = F$$

---

## 6. Concrete Example: Constructing $\mathbf{u}(x, y)$

To go from generalized coordinates $(v_L, \theta_L)$ at the tip to the continuous 2D displacement field $\mathbf{u}(x, y) = [u_x(x, y), u_y(x, y)]^T$, we need a concrete kinematic assumption.

Let's assume the neutral axis of the beam is at $y = 0$, meaning the domain is $x \in [0, L]$ and $y \in [-H/2, H/2]$.

### 1. Kinematic Ansatz
Using Timoshenko-like assumptions where deflection and rotation are independent, and assuming simple linear shapes along the length that satisfy the clamped boundary conditions $u_x(0,y) = u_y(0,y) = 0$:

$$u_y(x, y) = v(x) = \frac{x}{L} v_L$$
$$u_x(x, y) = -y \theta(x) = -y \frac{x}{L} \theta_L$$

Here, $v_L$ and $\theta_L$ are the tip deflection and rotation (our 2 unknowns).

### 2. Strain Vector $\boldsymbol{\varepsilon}(x, y)$
Taking derivatives according to the plane strain definition:

$$\varepsilon_{xx} = \frac{\partial u_x}{\partial x} = -y \frac{1}{L} \theta_L$$
$$\varepsilon_{yy} = \frac{\partial u_y}{\partial y} = 0$$
$$\gamma_{xy} = 2\varepsilon_{xy} = \frac{\partial u_x}{\partial y} + \frac{\partial u_y}{\partial x} = -\frac{x}{L} \theta_L + \frac{1}{L} v_L$$

In matrix form $\boldsymbol{\varepsilon} = \mathbf{B}_v v_L + \mathbf{B}_{\theta} \theta_L$:

$$\boldsymbol{\varepsilon}(x, y) = \begin{bmatrix} 0 \\ 0 \\ 1/L \end{bmatrix} v_L + \begin{bmatrix} -y/L \\ 0 \\ -x/L \end{bmatrix} \theta_L \quad \implies \quad \mathbf{B}_v = \begin{bmatrix} 0 \\ 0 \\ 1/L \end{bmatrix}, \quad \mathbf{B}_{\theta} = \begin{bmatrix} -y/L \\ 0 \\ -x/L \end{bmatrix}$$

### 3. Integrating to get Stiffness Coefficients $K_{ij}$
Using the plane strain constitutive tensor matrix components:

$$\mathbf{C} = \begin{bmatrix} C_{11} & C_{12} & 0 \\ C_{12} & C_{11} & 0 \\ 0 & 0 & G \end{bmatrix}$$

where $C_{11} = \frac{E(1-\nu)}{(1+\nu)(1-2\nu)}$ and $G = \frac{E}{2(1+\nu)}$ is the shear modulus.

Now, integrate $K_{ij} = \int_{0}^L \int_{-H/2}^{H/2} \mathbf{B}_i^T \mathbf{C} \mathbf{B}_j \, dy \, dx$:

* **For $K_{vv}$**:
  $$\mathbf{B}_v^T \mathbf{C} \mathbf{B}_v = \frac{G}{L^2}$$
  $$K_{vv} = \int_0^L \int_{-H/2}^{H/2} \frac{G}{L^2} \, dy \, dx = \frac{G H}{L}$$

* **For $K_{v\theta}$**:
  $$\mathbf{B}_v^T \mathbf{C} \mathbf{B}_{\theta} = -\frac{G x}{L^2}$$
  $$K_{v\theta} = \int_0^L \int_{-H/2}^{H/2} -\frac{G x}{L^2} \, dy \, dx = -\frac{G H}{L^2} \int_0^L x \, dx = -\frac{G H}{2}$$

* **For $K_{\theta\theta}$**:
  $$\mathbf{B}_{\theta}^T \mathbf{C} \mathbf{B}_{\theta} = C_{11} \frac{y^2}{L^2} + G \frac{x^2}{L^2}$$
  $$K_{\theta\theta} = \int_0^L \int_{-H/2}^{H/2} \left( C_{11} \frac{y^2}{L^2} + G \frac{x^2}{L^2} \right) \, dy \, dx = C_{11} \frac{H^3}{12 L} + \frac{G H L}{3}$$

### 4. Direct Solution for $v_L$ and $\theta_L$
With these coefficients, the rotation $\theta_L$ at the tip is:

$$\theta_L = -\frac{K_{\theta v}}{K_{\theta\theta}} v_L = \frac{G H / 2}{C_{11} \frac{H^3}{12 L} + \frac{G H L}{3}} v_L = \frac{6 G L}{C_{11} H^2 + 4 G L^2} v_L$$

Substitute this back into the force equation to get $v_L$:

$$\left( \frac{G H}{L} - \frac{3 G^2 H L}{C_{11} H^2 + 4 G L^2} \right) v_L = F$$

Once you solve for $v_L$ and $\theta_L$, you plug them directly back into the kinematic ansatz in step 1 to get the explicit continuous field $\mathbf{u}(x, y)$.

---

## 7. Connection to the Galerkin Method

Yes, this is exactly the **Bubnov-Galerkin** approach (often just called the Galerkin method). 

In the Galerkin method, the governing differential equations (strong form) are converted into a weak form (which is mathematically identical to the Principle of Virtual Work). You then project this weak form onto a finite-dimensional subspace using two key rules:
1. **Trial Space:** Approximate the solution $\mathbf{u}(x, y)$ using a linear combination of shape functions (the ansatz):
   $$\mathbf{u} = \sum_{j=1}^N \boldsymbol{\Phi}_j(x, y) q_j$$
2. **Test Space:** Choose the virtual/test functions $\delta \mathbf{u}$ from the *same* subspace:
   $$\delta \mathbf{u} = \sum_{i=1}^N \boldsymbol{\Phi}_i(x, y) \delta q_i$$

### Orthogonality and the Equations
The weak form requires the virtual work to vanish for all kinematically admissible test functions. When we substitute the approximations into the weak form, we get:

$$\sum_{i=1}^N \delta q_i \cdot \text{Residual}_i(q_1, q_2, \dots, q_N) = 0$$

Because the virtual variations $\delta q_i$ are arbitrary and independent, the only way this statement holds is if the residual projected onto each test function is individually zero:

$$\text{Residual}_i(q_1, q_2, \dots, q_N) = 0 \quad \text{for } i = 1, \dots, N$$

In your 2-degree-of-freedom case ($N = 2$):
- $\boldsymbol{\Phi}_1(x, y)$ is the shape function associated with the displacement $v$ ($\mathbf{H}_v$).
- $\boldsymbol{\Phi}_2(x, y)$ is the shape function associated with the rotation $\theta$ ($\mathbf{H}_{\theta}$).

By testing the virtual work with the first shape function (setting $\delta v \neq 0$, $\delta \theta = 0$), you get the first equation. By testing with the second shape function (setting $\delta v = 0$, $\delta \theta \neq 0$), you get the second. This is the exact projection/orthogonality principle used in Galerkin finite elements.

---

## 8. Transition from Global Galerkin to FEM

When transitioning from a global Ritz/Galerkin method to the Finite Element Method (FEM), the mathematical framework of virtual work remains exactly the same, but the **equations change structurally** in three major ways:

### 1. Shape Functions: Global to Local (Piecewise)
- **Global Galerkin:** The shape functions $\boldsymbol{\Phi}_j(x, y)$ are defined globally over the entire beam (e.g., polynomials like $x/L$).
- **FEM:** The domain is subdivided into elements $\Omega_e$. The shape functions $N_i(x, y)$ are local piecewise polynomials (typically Lagrange polynomials). The function $N_i(x, y)$ is only non-zero within the elements immediately connected to node $i$ (its local support).

### 2. Integration: Element-Level Assembly
Because the shape functions are local, the integrals for the stiffness matrix $K_{ij}$ are computed element-by-element and then summed up (assembled):

$$K_{ij} = \sum_{e} K_{ij}^e = \sum_{e} \int_{\Omega_e} \mathbf{B}_i^T \mathbf{C} \mathbf{B}_j \, d\Omega_e$$

If node $i$ and node $j$ do not share a common element, their shape functions do not overlap, meaning:

$$\mathbf{B}_i^T \mathbf{C} \mathbf{B}_j = 0 \implies K_{ij} = 0$$

As a result, the global stiffness matrix $\mathbf{K}$ changes from a dense $2 \times 2$ matrix to a **large, sparse, and banded matrix**.

### 3. Degrees of Freedom (DOFs)
Instead of 2 global parameters ($v_L, \theta_L$), the unknowns are now the values at each mesh node:
- In a 2D continuum formulation (like your plane strain model in Gmsh/DOLFINx), each node $a$ has displacement unknowns $\mathbf{u}^a = [u_x^a, u_y^a]^T$.
- In a discretized beam element formulation, each node $a$ has deflection and rotation unknowns $[w^a, \theta^a]^T$.

If you have $M$ nodes and $d$ degrees of freedom per node, the size of your system becomes $(M \times d) \times (M \times d)$:

$$\mathbf{K} \mathbf{U} = \mathbf{F}$$

where $\mathbf{U} = [U_1, U_2, \dots, U_{M \times d}]^T$ contains all nodal displacements.




