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


