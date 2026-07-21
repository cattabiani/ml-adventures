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

where:
- $\mathbf{U} = [U_1, U_2, \dots, U_{M \times d}]^T$ contains all nodal displacements.
- $\mathbf{K}$ is the assembled stiffness matrix representing the discretized **bilinear form** $a(u, v)$ (internal virtual work).
- $\mathbf{F}$ is the assembled load vector representing the discretized **linear form** $L(v)$ (external virtual work).


---

## 9. PINNs and Discrete Residual Loss: $\mathbf{K}\mathbf{U} - \mathbf{F}$

Using the residual of the discretized algebraic system as a loss function:

$$\mathcal{L}_{\text{discrete}}(\theta) = \|\mathbf{K} \mathbf{U}(\theta) - \mathbf{F}\|^2$$

is technically possible (often called **discrete residual minimization**), but it is not a standard PINN and has severe practical drawbacks.

Here is the comparison between how PINNs, the Deep Ritz Method, and the discrete loss approach work.

### 1. The Discrete Residual Loss: $\|\mathbf{K}\mathbf{U}(\theta) - \mathbf{F}\|^2$
In this approach, you parameterize the nodal displacements using a neural network $\mathbf{U}(\theta)$. 
- **Pros:** Enforces the physical constraints directly on the discretized mesh.
- **Cons:** You must construct the mesh, compute element stiffnesses, and assemble the global $\mathbf{K}$ and $\mathbf{F}$ matrices first. If you have already done this, using a standard linear solver (like conjugate gradient or sparse LU) will solve $\mathbf{K}\mathbf{U} = \mathbf{F}$ to machine precision in milliseconds. Training a neural network to minimize the residual is mathematically redundant, orders of magnitude slower, and less accurate.

### 2. Physics-Informed Neural Networks (PINNs) — Strong Form
A standard PINN is **completely mesh-free**. The neural network directly models the continuous displacement field:

$$\mathbf{u}_{\theta}(x, y) = \begin{bmatrix} u_x(x, y; \theta) \\ u_y(x, y; \theta) \end{bmatrix}$$

The loss function is evaluated at random collocation points inside the domain $\Omega$ and on the boundaries $\partial\Omega$:

$$\mathcal{L}(\theta) = \mathcal{L}_{\text{PDE}}(\theta) + \mathcal{L}_{\text{BC}}(\theta)$$

- **PDE Loss:** Minimizes the strong form equilibrium equations using automatic differentiation to compute the derivatives:
  $$\mathcal{L}_{\text{PDE}} = \int_{\Omega} \|\text{div}(\boldsymbol{\sigma}(\mathbf{u}_{\theta}))\|^2 \, d\Omega \approx \frac{1}{N_c} \sum_{i=1}^{N_c} \|\text{div}(\boldsymbol{\sigma}(\mathbf{u}_{\theta}(x_i, y_i)))\|^2$$
- **Boundary Condition Loss:** Enforces the clamped and traction boundary conditions:
  $$\mathcal{L}_{\text{BC}} = \frac{1}{N_b} \sum_{j=1}^{N_b} \|\mathbf{u}_{\theta}(0, y_j)\|^2 + \frac{1}{N_t} \sum_{k=1}^{N_t} \|\boldsymbol{\sigma}(\mathbf{u}_{\theta}(L, y_k)) \mathbf{n} - \mathbf{T}\|^2$$

### 3. The Deep Ritz / Deep Energy Method (DEM) — Weak Form
If you want to use the **Principle of Virtual Work / Energy** with neural networks, you use the **Deep Ritz Method** (or Deep Energy Method). Instead of solving the strong-form differential equations, you minimize the total potential energy functional directly:

$$\mathcal{L}_{\text{energy}}(\theta) = \Pi(\mathbf{u}_{\theta}) = \int_{\Omega} \left( \frac{1}{2} \boldsymbol{\varepsilon}(\mathbf{u}_{\theta})^T \mathbf{C} \boldsymbol{\varepsilon}(\mathbf{u}_{\theta}) \right) d\Omega - \int_{\Gamma_t} \mathbf{u}_{\theta}^T \mathbf{T} \, d\Gamma$$

- The neural network $\mathbf{u}_{\theta}(x, y)$ is the trial function.
- The derivatives for strain $\boldsymbol{\varepsilon}(\mathbf{u}_{\theta})$ are computed using automatic differentiation.
- The integrals are evaluated using Monte Carlo integration or quadrature points.
- By minimizing $\mathcal{L}_{\text{energy}}(\theta)$, the network naturally converges to the equilibrium solution (where the first variation/virtual work is zero).

---

## 10. Why use Deep Ritz (DEM) over a Standard FEM Solver?

For a standard, linear elastic forward problem (like a 2D linear elastic cantilever beam), **FEM is vastly superior**. It is orders of magnitude faster, mathematically guaranteed to converge, and resolves stress concentrations with precise local refinement. 

However, the Deep Ritz Method / Deep Energy Method (DEM) and PINNs become highly advantageous in more complex engineering scenarios:

### 1. Parametric Solutions (Real-Time Surrogates)
In FEM, if you change a design parameter (e.g., beam length $L$, height $H$, Young's modulus $E$, or the load magnitude $F$), you must rebuild the mesh, reassemble the equations, and resolve the system from scratch.

With Deep Ritz, you can pass these parameters as **extra inputs to the neural network**:

$$\mathbf{u}_{\theta}(x, y, L, H, E, F)$$

You train the network by sampling points in both space $(x,y)$ and parameter space $(L, H, E, F)$. Once trained, the network acts as a **real-time surrogate**. You can evaluate the deformation for *any* combination of geometry and load in microseconds without running new simulations.

### 2. Mesh-Free and Multi-Scale Problems
For complex 3D geometries, generating a high-quality conformal mesh can consume up to 80% of the engineering workflow time. 
- DEM is **mesh-free**: it only requires sampling points in the domain.
- It also handles sharp gradients and multi-scale structures better than FEM, as neural networks are universal function approximators and do not suffer from the same polynomial element locking issues (e.g., shear locking in thin structures) when set up correctly.

### 3. Solving Inverse Problems (Parameter Identification)
If you have experimental displacement data (e.g., from Digital Image Correlation) and want to find the unknown spatial distribution of material properties $E(x,y)$:
- **In FEM:** You must solve a nested, expensive optimization loop (updating $E(x,y)$, solving the full FEM system, calculating gradients via adjoints, and repeating).
- **In DEM/PINNs:** You simply add a data loss term $\|\mathbf{u}_{\theta} - \mathbf{u}_{\text{data}}\|^2$ to the loss function and treat $E(x,y)$ (which can also be parameterized by a network) as learnable weights. The physics equations and the material property identification are solved simultaneously in a single optimization loop.

### 4. High-Dimensional Problems
In traditional FEM, the computational cost grows exponentially with the number of dimensions (curse of dimensionality). For stochastic/probabilistic mechanics or high-dimensional parameter spaces, the mesh-free, sample-based optimization of Deep Ritz scales much better.

---

## 11. How does the "Mesh-Free" aspect actually work?

To understand why PINNs and the Deep Ritz Method are mesh-free, consider how FEM uses a mesh versus how a neural network represents a field.

### 1. How Derivatives are Computed
- **In FEM (Mesh-dependent):** 
  The displacement field $\mathbf{u}(x,y)$ is not a continuous analytical function. It is only defined at the nodes. To find the strain $\boldsymbol{\varepsilon} = \frac{\partial u}{\partial x}$ at an arbitrary point inside an element, FEM must interpolate between the nodal values using the local element shape functions:
  $$\mathbf{u}(x,y) \approx \sum_i N_i(x,y) \mathbf{U}_i$$
  Without the elements (the mesh connectivity and shape functions), you cannot compute derivatives.
- **In PINNs (Mesh-free):**
  The displacement is represented by a neural network $\mathbf{u}_{\theta}(x,y)$, which is a single, globally defined, continuously differentiable function. 
  Because the network consists of analytical functions (e.g., linear layers and differentiable activations like $\tanh$), you can compute the exact derivatives (gradients) at **any coordinate** $(x,y)$ using **Automatic Differentiation (AD)** (the backpropagation chain rule through the network's layers, with respect to the input coordinates $x, y$):
  $$\frac{\partial u_x}{\partial x} = \text{autograd}(\mathbf{u}_{\theta}, x)$$
  This requires no mesh, shape functions, or nodal connectivity. You just feed any coordinate $(x,y)$ into the autograd engine.

### 2. How Domain Integrals or Residuals are Evaluated
- **In FEM (Mesh-dependent):**
  To solve the equations, you must integrate the bilinear and linear forms over the domain $\Omega$. Because the shape functions are local piecewise functions, you must integrate element-by-element using Gauss quadrature (sampling points at specific mathematical locations inside each element).
- **In PINNs / Deep Ritz (Mesh-free):**
  - **For PINNs (Strong Form):** There are no integrals. You evaluate the strong-form PDE residual at a set of randomly sampled "collocation points" $\{ (x_i, y_i) \}_{i=1}^N$ distributed inside the domain (using simple random sampling or Latin Hypercube sampling). You just minimize the sum of square residuals at these discrete points.
- **For Deep Ritz (Weak Form / Energy):** You do have to compute the integral of the energy density $\int_{\Omega} \mathcal{U}(\mathbf{u}_{\theta}) \, d\Omega$. However, instead of integrating over elements, you use **Monte Carlo Integration** (or quasi-Monte Carlo). You sample random points $\{ (x_i, y_i) \}_{i=1}^N$ in the domain and approximate the integral as:
    $$\int_{\Omega} g(x,y) \, d\Omega \approx \frac{\text{Volume}(\Omega)}{N} \sum_{i=1}^N g(x_i, y_i)$$
    The accuracy of this integration scales with the number of random samples $N$, completely bypassing the need for structured element integration.

---

## 12. Connecting the "Vector of Floats" NN Model to Continuous Fields

If you are used to normal neural networks (like classifiers or predictors), you think of inputs as a tensor of features (like pixels) and outputs as a tensor of class probabilities, with the network being a series of matrix multiplications. That mental model is 100% correct here too. 

To see how that "vector of floats" represents a continuous function, let's look at the forward pass of a PINN.

### 1. The Inputs and Outputs are Coordinates and Displacements
In a PINN, you feed a single coordinate $(x,y)$ into the network. 
- **Input:** A vector of 2 floats: $\mathbf{x}_{\text{in}} = [x, y]^T$ (e.g., `[0.5, 0.2]`).
- **Output:** A vector of 2 floats: $\mathbf{u}_{\text{out}} = [u_x, u_y]^T$ (e.g., `[-0.01, -0.05]`).

### 2. A 1-Layer Network Example
To see why this is a continuous function, let's write out a simple 1-layer Multi-Layer Perceptron (MLP) with a Tanh activation function:

$$\mathbf{u}(x, y) = \mathbf{W}_2 \tanh\left( \mathbf{W}_1 \begin{bmatrix} x \\ y \end{bmatrix} + \mathbf{b}_1 \right) + \mathbf{b}_2$$

If we write out the equation for the output $u_x$ using the individual float weights and biases:

$$u_x(x, y) = w'_{11} \tanh(w_{11} x + w_{12} y + b_{11}) + w'_{12} \tanh(w_{21} x + w_{22} y + b_{12}) + b'_{11}$$

This equation is a classic, continuous mathematical function of two variables ($x$ and $y$). 
- For *any* float value of $x$ and $y$ you feed in, you get a float value of $u_x$ out.
- There are no gaps or jumps because $\tanh$ is smooth.

### 3. Computing derivatives using PyTorch `autograd`
Because the equation for $u_x(x,y)$ is analytically defined by the weights and activations, we can compute the derivative $\frac{\partial u_x}{\partial x}$ at any point $(x,y)$ using the standard calculus chain rule.

In PyTorch, you do this by setting `requires_grad=True` on your input coordinate vector and calling `torch.autograd.grad`:

```python
import torch

# 1. Input coordinate (2 floats)
coord = torch.tensor([[0.5, 0.2]], requires_grad=True) # shape (1, 2)

# 2. Forward pass: outputs displacement (2 floats)
u = model(coord) # u = [u_x, u_y]

# 3. Compute du_x / dx analytically using Autograd
du_dx = torch.autograd.grad(
    outputs=u[:, 0], # u_x
    inputs=coord, 
    grad_outputs=torch.ones_like(u[:, 0]),
    create_graph=True
)[0][:, 0] # first component is wrt x
```

No mesh is needed because PyTorch is not doing finite differences (like $(u(x+\Delta x) - u(x))/\Delta x$). It is evaluating the exact analytical derivative of the network's layers at that specific coordinate.

---

## 13. The Deep Ritz Training Loop Step-by-Step

Yes, exactly: the neural network **is** the unknown field $\mathbf{u}(x, y)$. 

To find the correct weights $\theta$ (the float parameters of the network), we sample a bunch of coordinate points inside the beam and on the boundary, evaluate the energy at those points, and minimize the energy using gradient descent. 

Here is the exact step-by-step loop of what we do:

### Step 1: Initialize the Network
You start with a neural network `model` with random weights $\theta$. If you feed in a coordinate like `[0.5, 0.2]`, it will output random garbage like `[-142.3, 89.1]`.

### Step 2: Sample Points (No Mesh)
Generate two batches of random coordinate floats (often using Latin Hypercube Sampling to distribute them evenly):
1. `X_domain`: $N_d$ points inside the beam (e.g., $x \in [0, L], y \in [-H/2, H/2]$).
2. `X_boundary`: $N_b$ points on the right edge where the force $F$ is applied ($x = L, y \in [-H/2, H/2]$).

### Step 3: Compute the Strain Energy (Internal Work)
Pass the domain coordinates `X_domain` through the network:
1. Get the displacements: $\mathbf{u} = \text{model}(\mathbf{x}_i)$.
2. Use PyTorch Autograd to compute the strain components at each point:
   $$\varepsilon_{xx} = \frac{\partial u_x}{\partial x}, \quad \varepsilon_{yy} = \frac{\partial u_y}{\partial y}, \quad \gamma_{xy} = \frac{\partial u_x}{\partial y} + \frac{\partial u_y}{\partial x}$$
3. Compute the strain energy density at each sampled point:
   $$U_i = \frac{1}{2} \boldsymbol{\varepsilon}_i^T \mathbf{C} \boldsymbol{\varepsilon}_i$$
4. Compute the total strain energy of the beam by taking the average over all points and multiplying by the total volume (area in 2D) $\Omega$:
   $$E_{\text{strain}} \approx \text{Volume}(\Omega) \cdot \frac{1}{N_d} \sum_{i=1}^{N_d} U_i$$

### Step 4: Compute the External Work
Pass the boundary coordinates `X_boundary` through the network:
1. Get the boundary displacements: $\mathbf{u}_j = \text{model}(\mathbf{x}_j)$.
2. Compute the work done by the traction force $\mathbf{T} = [0, -F_y]^T$ at each boundary point:
   $$W_j = u_y(L, y_j) \cdot (-F_y)$$
3. Compute the total external work by averaging and multiplying by the boundary area (height in 2D) $\Gamma_t$:
   $$E_{\text{external}} \approx \text{Height}(H) \cdot \frac{1}{N_b} \sum_{j=1}^{N_b} W_j$$

### Step 5: Compute the Total Energy (The Loss)
The loss function is the total potential energy of the system:

$$\text{Loss}(\theta) = E_{\text{strain}} - E_{\text{external}}$$

*(If you have essential boundary conditions like the clamped end at $x=0$, you also add a penalty term like $\beta \sum \| \mathbf{u}(0, y) \|^2$ to the loss to force the network to output zero displacement at the wall).*

### Step 6: Backpropagate and Update
1. Call `loss.backward()` to compute the gradients of the energy with respect to the network weights: $\nabla_{\theta} \text{Loss}$.
2. Run an optimizer step (e.g., Adam):
   $$\theta \leftarrow \theta - \eta \nabla_{\theta} \text{Loss}$$

### Step 7: Iterate
Repeat steps 2–6 for thousands of epochs. At each epoch, you can optionally sample **new** random points. 

According to the **Principle of Minimum Potential Energy**, the displacement field that minimizes this energy loss function is the exact, true physical equilibrium solution. As the optimizer minimizes the loss, the neural network converges to the correct physical displacement field $\mathbf{u}(x, y)$.

---

## 14. Why the Method is "Crude" (And the Reality of PINNs)

It is indeed extremely crude compared to the mathematical elegance and precision of FEM. If you are coming from numerical analysis, the "brute force" nature of PINNs/Deep Ritz is often jarring. 

Here are the main reasons why this approach is considered crude, along with the actual engineering realities:

### 1. Integration Noise vs. Gauss Quadrature
- **FEM:** Uses **Gauss Quadrature** inside elements. For a linear or quadratic polynomial shape function, Gauss Quadrature evaluates the integrals *exactly* using only 2 or 3 points.
- **Deep Ritz:** Uses **Monte Carlo Integration** over random points. The error in Monte Carlo integration decreases very slowly with the number of points $N$ (specifically, $O(1/\sqrt{N})$). This introduces high high-frequency noise into the loss landscape, making the optimization path erratic.

### 2. "Soft" Boundary Conditions (The Penalty Method Pain)
- **FEM:** Dirichlet boundary conditions are **hard-coded** directly into the system of equations. For example, if node 1 is clamped ($u_1 = 0$), the first row and column of $\mathbf{K}$ are modified, guaranteeing the displacement is exactly zero.
- **Deep Ritz / PINNs:** Boundary conditions are usually enforced as a **soft penalty** in the loss:
  $$\text{Loss} = E_{\text{strain}} - E_{\text{external}} + \beta \sum \|\mathbf{u}_{\text{wall}}\|^2$$
  Balancing the penalty weight $\beta$ is a notorious issue. If $\beta$ is too small, the beam will detach from the wall. If $\beta$ is too large, the optimizer will focus entirely on the boundary and completely ignore the stress/strain physics in the domain.

*(Note: Advanced formulations try to bypass this by designing a **hard-constrained ansatz**, e.g., $\mathbf{u}(x,y) = x \cdot \text{MLP}(x,y)$ which mathematically guarantees $\mathbf{u}=0$ at $x=0$, but this is hard to construct for complex shapes).*

### 3. Non-Convex Optimization vs. Linear Solving
- **FEM:** For linear elasticity, the optimization problem is quadratic and convex. Solving $\mathbf{K}\mathbf{U}=\mathbf{F}$ is a single step (LU decomposition or Conjugate Gradient). It always finds the global minimum immediately.
- **Deep Ritz / PINNs:** You are training a non-convex, highly nonlinear network using gradient descent (Adam/L-BFGS). It requires thousands of iterations, can easily get stuck in local minima, and has no mathematical guarantee of converging to the true solution.

### Summary
PINNs and Deep Ritz are not meant to compete with FEM for standard forward simulations. They are essentially a brute-force optimization approach to solving differential equations. Their main value is in **unifying data and physics** (solving inverse problems where FEM fails) and building **real-time parametric surrogates** where the upfront training cost is offset by instant evaluation later.

---

## 15. PINN (Strong Form) vs. Deep Ritz (Weak Form)

To see the difference in how they work, compare what each method asks the neural network to compute.

### 1. Standard PINN (Strong Form)
A standard PINN solves the strong-form PDEs directly. 
- **The Equation:** For 2D elasticity, it must satisfy:
  $$\frac{\partial \sigma_{xx}}{\partial x} + \frac{\partial \sigma_{xy}}{\partial y} = 0, \quad \frac{\partial \sigma_{xy}}{\partial x} + \frac{\partial \sigma_{yy}}{\partial y} = 0$$
- **Derivative Requirement:** Since stress $\boldsymbol{\sigma}$ is already a first derivative of displacement $\mathbf{u}$ (strain), computing the divergence of stress requires **second-order spatial derivatives** of the displacement field:
  $$\frac{\partial^2 u_x}{\partial x^2}, \quad \frac{\partial^2 u_y}{\partial y^2}, \quad \frac{\partial^2 u_x}{\partial y^2}, \text{ etc.}$$
- **Traction BCs:** You must manually enforce traction boundary conditions (like the force at the tip) by adding another penalty term to the loss:
  $$\mathcal{L}_{\text{traction}} = \beta_{\text{trac}} \sum \|\boldsymbol{\sigma}\mathbf{n} - \mathbf{T}\|^2$$

### 2. Deep Ritz / Deep Energy Method (Weak Form)
Instead of enforcing the differential equations point-by-point, Deep Ritz minimizes the total potential energy of the system.
- **The Equation:** It minimizes:
  $$\Pi(\mathbf{u}) = \int_{\Omega} \left( \frac{1}{2} \boldsymbol{\varepsilon}(\mathbf{u})^T \mathbf{C} \boldsymbol{\varepsilon}(\mathbf{u}) \right) d\Omega - \int_{\Gamma_t} \mathbf{u}^T \mathbf{T} \, d\Gamma$$
- **Derivative Requirement:** Because the energy depends only on strain $\boldsymbol{\varepsilon}$, you only need **first-order spatial derivatives** of the displacement field:
  $$\frac{\partial u_x}{\partial x}, \quad \frac{\partial u_y}{\partial y}, \quad \frac{\partial u_x}{\partial y}, \quad \frac{\partial u_y}{\partial x}$$
- **Traction BCs:** You do not need to add a penalty term for traction boundary conditions. The work done by the force $- \int_{\Gamma_t} \mathbf{u}^T \mathbf{T} \, d\Gamma$ is **naturally built into the energy functional**. The optimizer satisfies this boundary condition automatically as it minimizes the total energy.

### Comparison Table

| Feature | PINN (Strong Form) | Deep Ritz (Weak Form) |
| :--- | :--- | :--- |
| **Physical Principle** | Equilibrium of forces (PDE) | Minimum Potential Energy (PVW) |
| **Max Derivative Order**| 2nd order ($\frac{\partial^2 u}{\partial x^2}$) | 1st order ($\frac{\partial u}{\partial x}$) |
| **Computational Cost** | High (double autograd graph) | Lower (single autograd graph) |
| **Traction Boundary (Force)** | Soft penalty in loss | Integrated naturally in the energy |
| **Dirichlet Boundary (Wall)** | Soft penalty in loss | Soft penalty in loss |
| **Loss Landscape** | Stiffer, harder to optimize | Smoother, faster convergence |

---

## 16. How Deep Ritz Integrates the Bilinear Form

Yes, it is still a numerical approximation. To evaluate the domain integral of the strain energy density (the bilinear form):

$$\int_{\Omega} \left( \frac{1}{2} \boldsymbol{\varepsilon}(\mathbf{u}_{\theta})^T \mathbf{C} \boldsymbol{\varepsilon}(\mathbf{u}_{\theta}) \right) d\Omega$$

Deep Ritz does not integrate analytically. Instead, it uses one of two numerical integration methods:

### Method A: Monte Carlo (or quasi-Monte Carlo) Integration
This is the standard mesh-free approach:
1. **Sample points:** You generate a set of $N$ randomly distributed coordinates $\{\mathbf{x}_i\}_{i=1}^N$ in the domain $\Omega$ (using uniform random distribution, Latin Hypercube Sampling, or low-discrepancy Sobol sequences to cover the space evenly).
2. **Evaluate and Sum:** You compute the strain energy density at each coordinate and multiply the average by the total area/volume of the domain:
   $$\int_{\Omega} \mathcal{U}(\mathbf{u}_{\theta}) \, d\Omega \approx \text{Area}(\Omega) \cdot \frac{1}{N} \sum_{i=1}^N \mathcal{U}(\mathbf{u}_{\theta}(\mathbf{x}_i))$$
3. **Resampling:** In practice, we generate **new random points at every epoch**. This means the network sees a slightly different sample of coordinates each iteration. The optimizer minimizes the expected potential energy over the entire probability space of the domain, which acts as a powerful regularizer preventing overfitting.

### Method B: Fixed Background Quadrature Grid
If you want to eliminate the noise of Monte Carlo integration, you can use a fixed grid of integration points:
1. **Define Grid:** Predefine a static grid of coordinates $\{\mathbf{x}_i\}_{i=1}^N$ inside the domain $\Omega$ along with their respective integration weights $w_i$. Note that this grid has **no mesh connectivity**—it is just a list of independent point coordinates and floats.
2. **Evaluate:**
   $$\int_{\Omega} \mathcal{U}(\mathbf{u}_{\theta}) \, d\Omega \approx \sum_{i=1}^N w_i \, \mathcal{U}(\mathbf{u}_{\theta}(\mathbf{x}_i))$$
3. **Keep Static:** Since the coordinates are fixed, the integration weights $w_i$ do not change during training, making the loss landscape completely deterministic and easier for optimizers like L-BFGS to converge.

---

## 17. The Exact Computational Difference: PINN Loss vs. Deep Ritz Loss

To see why they are not the same computation, look at what you compute at each point $(x_i, y_i)$ to get the final scalar loss.

### 1. PINN Loss (Strong Form PDE Residuals)
A standard PINN does **not** compute energy, virtual work, or integrals. It checks if Newton's second law (force balance) holds at each point.

For each point $i$, you compute:
1. Displacement: $\mathbf{u}_i = [u_x, u_y]^T$
2. Strains (1st derivatives): $\boldsymbol{\varepsilon}_i = [\frac{\partial u_x}{\partial x}, \frac{\partial u_y}{\partial y}, \frac{\partial u_x}{\partial y} + \frac{\partial u_y}{\partial x}]^T$
3. Stresses: $\boldsymbol{\sigma}_i = \mathbf{C} \boldsymbol{\varepsilon}_i$
4. **PDE Residuals (2nd derivatives):**
   $$R_{x, i} = \frac{\partial \sigma_{xx}}{\partial x} + \frac{\partial \sigma_{xy}}{\partial y} + f_x$$
   $$R_{y, i} = \frac{\partial \sigma_{xy}}{\partial x} + \frac{\partial \sigma_{yy}}{\partial y} + f_y$$
5. **The Domain Loss is the mean of squared residuals:**
   $$\mathcal{L}_{\text{PINN\_domain}} = \frac{1}{N} \sum_{i=1}^N \left( R_{x, i}^2 + R_{y, i}^2 \right)$$

*Note:* You are squaring the local force imbalances at each point and averaging them. There is no multiplication by volume/area, and no summation of energy.

---

### 2. Deep Ritz / DEM Loss (Potential Energy)
Deep Ritz does **not** compute force balance or stress divergence. It computes the total potential energy of the system.

For each point $i$, you compute:
1. Displacement: $\mathbf{u}_i = [u_x, u_y]^T$
2. Strains (1st derivatives): $\boldsymbol{\varepsilon}_i = [\frac{\partial u_x}{\partial x}, \frac{\partial u_y}{\partial y}, \frac{\partial u_x}{\partial y} + \frac{\partial u_y}{\partial x}]^T$
3. **Strain Energy Density (No 2nd derivatives):**
   $$\mathcal{U}_i = \frac{1}{2} \boldsymbol{\varepsilon}_i^T \mathbf{C} \boldsymbol{\varepsilon}_i$$
4. **The Domain Loss is the approximated integral of energy:**
   $$\mathcal{L}_{\text{Ritz\_domain}} = \text{Volume}(\Omega) \cdot \frac{1}{N} \sum_{i=1}^N \mathcal{U}_i$$

---

### Key Takeaways
- **The mathematical quantities are different:** PINN minimizes force imbalance (units: $\text{N}^2/\text{m}^6$ squared force density), while Deep Ritz minimizes potential energy (units: $\text{J}$ energy).
- **The derivative orders are different:** PINN requires second-order derivatives of displacements to get the divergence of stress ($\frac{\partial^2 u}{\partial x^2}$). Deep Ritz only requires first-order derivatives ($\frac{\partial u}{\partial x}$) to calculate strain energy density.
- **Traction BCs:** PINN requires an explicit boundary term $\sum \|\boldsymbol{\sigma}\mathbf{n} - \mathbf{T}\|^2$. Deep Ritz naturally satisfies traction boundaries through the external work term $- \int \mathbf{u}^T \mathbf{T} \, d\Gamma$.

---

## 18. What are $f_x$ and $f_y$?

In the Navier-Cauchy equations:

$$\frac{\partial \sigma_{xx}}{\partial x} + \frac{\partial \sigma_{xy}}{\partial y} + f_x = 0$$
$$\frac{\partial \sigma_{xy}}{\partial x} + \frac{\partial \sigma_{yy}}{\partial y} + f_y = 0$$

$f_x$ and $f_y$ are **not** unknowns. They are the **known external body forces** per unit volume acting on the material. 

### Common Examples:
1. **Gravity:** If the beam has density $\rho$ and gravity $g$ acts downward along the $y$-axis:
   $$f_x = 0, \quad f_y = -\rho g$$
2. **No Body Force:** If you are ignoring gravity and the beam is only loaded by forces at its boundary/tip (which is typical for a simple cantilever model):
   $$f_x = 0, \quad f_y = 0$$
   In this case, the equations simplify to pure divergence of stress:
   $$\frac{\partial \sigma_{xx}}{\partial x} + \frac{\partial \sigma_{xy}}{\partial y} = 0$$
   $$\frac{\partial \sigma_{xy}}{\partial x} + \frac{\partial \sigma_{yy}}{\partial y} = 0$$

Because $f_x$ and $f_y$ are known constants (or known functions of coordinate inputs $x, y$), you do not need to calculate them from the network output. You just define them as constants in your python script (e.g., `fx = 0.0`, `fy = 0.0`) and add them directly to the residual expression inside your loss function.

---

## 19. A Physical Intuition of PINNs: Infinitesimal Block Equilibrium

Your physical intuition is 100% correct:

### 1. The Infinitesimal Block Analogy
The Navier-Cauchy equations:

$$\frac{\partial \sigma_{xx}}{\partial x} + \frac{\partial \sigma_{xy}}{\partial y} = 0$$

are derived in mechanics by drawing a tiny, infinitesimal control block of dimensions $dx \times dy$ inside the material, calculating the normal and shear forces acting on each face, and summing them to zero. 

A PINN does exactly this: at every single collocation point $(x_i, y_i)$, it looks at that infinitesimal block and penalizes the network if the forces on that block do not balance. 

### 2. The Training Step
The training process mirrors standard deep learning batch optimization:
1. **Forward Pass (Vectorized):** You feed a batch of e.g. 5,000 coordinate points into the network. PyTorch calculates the displacement, stresses, and the force imbalance for all 5,000 infinitesimal blocks in parallel.
2. **Loss Evaluation:** You compute the average squared force imbalance across the batch (plus boundary term penalties).
3. **Backpropagation:** You backpropagate the gradients of this mean loss to update the weights $\theta$, forcing all infinitesimal blocks across the entire domain to reach static equilibrium.

---

## 20. Where did the Virtual/Test Fields go in Deep Ritz?

This is a profound question. In the Principle of Virtual Work (or Galerkin), you need virtual test displacements $\delta \mathbf{u}$ to check equilibrium:

$$\delta W_{\text{int}}(\mathbf{u}, \delta \mathbf{u}) - \delta W_{\text{ext}}(\delta \mathbf{u}) = 0 \quad \forall \delta \mathbf{u}$$

But in Deep Ritz, you only have one neural network representing $\mathbf{u}_{\theta}(x, y)$. You do not define any virtual test functions or test basis functions. 

So how does the equilibrium balance get satisfied without testing? 

### 1. Ritz vs. Galerkin Equivalence
Deep Ritz relies on a core theorem of variational calculus:
> For a self-adjoint system, finding the field $\mathbf{u}$ that satisfies the virtual work equation for all arbitrary $\delta \mathbf{u}$ is mathematically equivalent to finding the field $\mathbf{u}$ that **minimizes** the total potential energy functional:
> $$\mathbf{u} = \arg\min_{\mathbf{v}} \Pi(\mathbf{v})$$

By minimizing the energy $\Pi(\mathbf{u}_{\theta})$ directly, we guarantee that at the minimum, the first variation (virtual work) is zero.

### 2. The Network's Weights *Are* the Test Space
To see how this works computationally, consider what happens when you train the network. You minimize the energy functional $\Pi(\mathbf{u}_{\theta})$ with respect to the network weights $\theta$:

$$\frac{\partial \Pi(\mathbf{u}_{\theta})}{\partial \theta_k} = 0 \quad \text{for all weights } \theta_k$$

Using the chain rule, this derivative is:

$$\frac{\partial \Pi(\mathbf{u}_{\theta})}{\partial \theta_k} = \int_{\Omega} \left( \text{stresses} \right) \cdot \frac{\partial \boldsymbol{\varepsilon}(\mathbf{u}_{\theta})}{\partial \theta_k} \, d\Omega - \int_{\Gamma_t} \mathbf{T} \cdot \frac{\partial \mathbf{u}_{\theta}}{\partial \theta_k} \, d\Gamma = 0$$

Look at this equation. It is exactly the Principle of Virtual Work where the virtual variation $\delta \mathbf{u}$ has been replaced by the **sensitivity of the neural network with respect to its weights**:

$$\delta \mathbf{u}_k(x, y) = \frac{\partial \mathbf{u}_{\theta}(x, y)}{\partial \theta_k}$$

### Summary
In Deep Ritz, you do not need to construct a test space or a set of orthonormal test functions. The network's weights $\theta_k$ automatically define millions of independent, continuous virtual displacement fields $\delta \mathbf{u}_k = \frac{\partial \mathbf{u}_{\theta}}{\partial \theta_k}$. 

By running backpropagation and driving the gradient of the energy loss with respect to all weights to zero ($\nabla_{\theta} \text{Loss} = 0$), you are forcing the virtual work to vanish for all virtual fields spanned by the network's parameters.

---

## 21. The Potential Energy Loss: A Global Scalar (And Why You Do NOT Square It)

Your understanding of the global nature of the loss is completely correct, but there is one critical warning: **you must never square the energy loss!**

Here is why:

### 1. Yes, the Loss is a Single Global Scalar
In a standard PINN, the loss is the average of many small punctual errors:

$$\mathcal{L}_{\text{PINN}} = \frac{1}{N} \sum_{i=1}^N (\text{Residual}_i)^2$$

In Deep Ritz, the loss is the **total potential energy of the entire physical system**, computed by integrating over the whole domain:

$$\text{Loss}(\theta) = E_{\text{strain}} - E_{\text{external}}$$

You are correct: you are not checking balance at each point individually. Instead, you are looking at the global discrepancy between the internal strain energy and the external work done by the loads. The neural network adjusts its weights to find the state of minimum global energy.

---

### 2. CRITICAL: Why You Do NOT Square the Loss
In traditional deep learning, we always square the residuals (like Mean Squared Error) because the target value of the loss is $0$.

If you square the potential energy:

$$\text{Loss}_{\text{incorrect}}(\theta) = \left( E_{\text{strain}} - E_{\text{external}} \right)^2$$

the optimizer will try to drive this loss to $0$, meaning it will look for a state where:

$$E_{\text{strain}} = E_{\text{external}}$$

However, in linear elasticity, **Clapeyron's Theorem** states that at physical equilibrium:

$$E_{\text{strain}} = \frac{1}{2} E_{\text{external}}$$

This is because as the load is applied, some work is stored as strain energy ($50\%$), and the other $50\%$ is lost to the system's potential. 

Therefore, the true minimum of the potential energy is **negative**:

$$\Pi(\mathbf{u}_{\text{equilibrium}}) = \frac{1}{2} E_{\text{external}} - E_{\text{external}} = -\frac{1}{2} E_{\text{external}} < 0$$

If you square the energy functional, you are forcing the system to satisfy $E_{\text{strain}} = E_{\text{external}}$, which results in a completely wrong, non-physical displacement field. You must minimize the potential energy directly as a raw, signed value:

$$\text{Loss}(\theta) = E_{\text{strain}} - E_{\text{external}}$$

The optimizer will drive the energy to its lowest possible negative value, which corresponds exactly to the physical equilibrium state.

---

## 22. The Mathematical Link: PVW vs. Clapeyron's Theorem

Here is how the Principle of Virtual Work and Clapeyron's Theorem meet mathematically.

### 1. The Virtual Work Statement (Galerkin/Weak Form)
The Principle of Virtual Work states that for any arbitrary virtual displacement $\delta \mathbf{u}$:

$$\int_{\Omega} \delta \boldsymbol{\varepsilon}^T \mathbf{C} \boldsymbol{\varepsilon}(\mathbf{u}) \, d\Omega = \int_{\Gamma_t} \delta \mathbf{u}^T \mathbf{T} \, d\Gamma$$

This is a statement about **variations** (derivatives) at the equilibrium state.

### 2. Testing with the Actual Displacement
Since the virtual variation $\delta \mathbf{u}$ can be *any* kinematically admissible displacement, let's choose to evaluate the virtual work equation specifically using the **actual displacement field $\mathbf{u}$ itself** as the virtual displacement (i.e., setting $\delta \mathbf{u} = \mathbf{u}$):

$$\int_{\Omega} \boldsymbol{\varepsilon}(\mathbf{u})^T \mathbf{C} \boldsymbol{\varepsilon}(\mathbf{u}) \, d\Omega = \int_{\Gamma_t} \mathbf{u}^T \mathbf{T} \, d\Gamma$$

Now, identify the physical terms:
- The right-hand side is the **total external work** done by the constant load:
  $$E_{\text{external}} = \int_{\Gamma_t} \mathbf{u}^T \mathbf{T} \, d\Gamma$$
- The left-hand side is **twice** the strain energy. Recall that for a linear elastic material under load, the stress-strain relation is linear, so the integrated strain energy is:
  $$E_{\text{strain}} = \frac{1}{2} \int_{\Omega} \boldsymbol{\varepsilon}(\mathbf{u})^T \mathbf{C} \boldsymbol{\varepsilon}(\mathbf{u}) \, d\Omega$$
  This means the left-hand side is exactly $2 E_{\text{strain}}$.

### 3. The Meeting Point
Substituting these terms back into the evaluated virtual work equation yields:

$$2 E_{\text{strain}} = E_{\text{external}} \implies E_{\text{strain}} = \frac{1}{2} E_{\text{external}}$$

This is Clapeyron's Theorem. It is not a different physical law; it is simply the Principle of Virtual Work evaluated on the equilibrium solution itself. 

This explains why at the minimum of the potential energy functional $\Pi = E_{\text{strain}} - E_{\text{external}}$, the total potential energy is:

$$\Pi = \frac{1}{2} E_{\text{external}} - E_{\text{external}} = -\frac{1}{2} E_{\text{external}}$$

which is negative.

---

## 23. Why Can't We Use $\left( E_{\text{strain}} - \frac{1}{2} E_{\text{external}} \right)^2$ as the Loss?

It is highly tempting to say: *"Since $E_{\text{strain}} = \frac{1}{2} E_{\text{external}}$ at equilibrium, why don't we just square the difference and drive it to zero as our loss?"*

$$\mathcal{L}_{\text{incorrect}}(\theta) = \left( E_{\text{strain}} - \frac{1}{2} E_{\text{external}} \right)^2$$

This does not work. Minimizing this squared quantity results in a **non-physical solution** due to the existence of infinite false minima.

### 1. The Local vs. Global Information Loss
- **The True Potential Energy $\Pi = E_{\text{strain}} - E_{\text{external}}$:**
  When you minimize $\Pi(\mathbf{u})$, you are finding a stationary point where the first variation is zero for **every possible virtual displacement variation $\delta \mathbf{u}$**:
  $$\delta \Pi = \delta E_{\text{strain}} - \delta E_{\text{external}} = 0 \quad \forall \delta \mathbf{u}$$
  This derivative requirement forces the local differential equations of force equilibrium to be satisfied at *every single coordinate* in the domain.
- **The Squared Energy Balance $\mathcal{L}_{\text{incorrect}} = \left( E_{\text{strain}} - \frac{1}{2} E_{\text{external}} \right)^2$:**
  Let's take the variation (derivative) of this loss function:
  $$\delta \mathcal{L}_{\text{incorrect}} = 2 \left( E_{\text{strain}} - \frac{1}{2} E_{\text{external}} \right) \cdot \left( \delta E_{\text{strain}} - \frac{1}{2} \delta E_{\text{external}} \right)$$
  Notice that $\delta \mathcal{L} = 0$ is satisfied **any time** $E_{\text{strain}} = \frac{1}{2} E_{\text{external}}$, regardless of what the variation $\left( \delta E_{\text{strain}} - \frac{1}{2} \delta E_{\text{external}} \right)$ is. 

### 2. Infinite False Global Minima
There are infinitely many completely wrong, non-physical displacement fields that happen to satisfy the single scalar ratio $E_{\text{strain}} = \frac{1}{2} E_{\text{external}}$.

For example, take a completely random, garbage displacement field $\mathbf{u}_{\text{garbage}}(x, y)$ that violates all force balance equations. If you scale this garbage field by a constant factor $\alpha$:
$$\mathbf{u} = \alpha \mathbf{u}_{\text{garbage}}$$
Since strain energy is quadratic in displacement ($E_{\text{strain}} \propto \alpha^2$) and external work is linear ($E_{\text{external}} \propto \alpha$), you can always solve for a scaling factor $\alpha$:
$$\alpha^2 E_{\text{strain\_garbage}} = \frac{1}{2} \alpha E_{\text{external\_garbage}} \implies \alpha = \frac{E_{\text{external\_garbage}}}{2 E_{\text{strain\_garbage}}}$$
This scaled garbage field will yield a loss of **exactly zero**. 

If you train a neural network with this squared loss, the optimizer will quickly find one of these infinite scaled garbage fields that satisfies the scalar ratio, instead of solving the actual physical boundary value problem.



















