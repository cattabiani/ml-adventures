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

Substituting this into $\delta W_{\text{ext}} = \delta W_{\text{int}}$ will yield:

$$\text{Coeff}_1 \delta c_1 + \text{Coeff}_2 \delta c_2 = 0$$

Since $\delta c_1$ and $\delta c_2$ are independent:

$$\text{Equation 1: } \text{Coeff}_1 = 0$$
$$\text{Equation 2: } \text{Coeff}_2 = 0$$

Which again provides 2 equations for the 2 unknown coefficients.
