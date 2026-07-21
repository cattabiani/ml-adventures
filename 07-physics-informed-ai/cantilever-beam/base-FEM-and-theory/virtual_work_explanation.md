# Principle of Virtual Work for a Cantilever Beam

You have a cantilever beam modeled with two degrees of freedom (e.g., displacement `v` and rotation `θ`), and you are stuck with 2 unknowns but only 1 equation. 

The issue is a common conceptual mix-up: you are likely equating the **actual** work (or thinking of virtual work as a single scalar equation), whereas the Principle of Virtual Work (PVW) operates on **virtual variations** which are arbitrary and independent.

Here is the breakdown of why you actually have 2 equations.

---

## 1. Actual Work vs. Virtual Work

If you write the conservation of energy (Clapeyron's theorem) for actual displacements:
```
W_ext = W_int
```
This is indeed **1 equation** for **2 unknowns**, making it underdetermined. This equation only guarantees that the total energy is balanced, but it does not specify the equilibrium path.

However, the **Principle of Virtual Work** states that the virtual work done by external forces must equal the virtual work done by internal forces for **any arbitrary virtual displacement field** that is kinematically admissible:
```
δW_ext = δW_int
```
Where `δ` (delta) represents a virtual, infinitesimal variation.

---

## 2. Setting Up the Virtual Work Equation

Let's assume your two independent unknowns are:
- `v`: Deflection (displacement) at the tip
- `θ`: Rotation (angle) at the tip

The corresponding virtual variations are `δv` and `δθ`. These variations are **completely independent and arbitrary**.

The virtual work of the external forces (e.g., a point force `F` and a moment `M` at the tip) is:
```
δW_ext = F * δv + M * δθ
```

The virtual work of the internal forces/moments (due to structural stiffness or internal stresses) can be written generally as:
```
δW_int = R_v(v, θ) * δv + R_θ(v, θ) * δθ
```
where `R_v` and `R_θ` are the internal resistance forces/moments as functions of the actual displacement `v` and rotation `θ`.

Equating the two:
```
F * δv + M * δθ = R_v(v, θ) * δv + R_θ(v, θ) * δθ
```
Rearranging:
```
[ F - R_v(v, θ) ] * δv  +  [ M - R_θ(v, θ) ] * δθ = 0
```

---

## 3. Resolving the 2 Unknowns (The "Magic" of PVW)

Since the virtual variations `δv` and `δθ` are **arbitrary and independent**, the equation above must hold for **any** choice of `δv` and `δθ`. 

Specifically:
1. If we choose a virtual state where `δv` is non-zero but `δθ = 0`, we get:
   ```
   F - R_v(v, θ) = 0
   ```
2. If we choose a virtual state where `δv = 0` but `δθ` is non-zero, we get:
   ```
   M - R_θ(v, θ) = 0
   ```

This gives you exactly **2 independent equations** for your **2 unknowns** (`v` and `θ`):
```
Equation 1:  R_v(v, θ) = F
Equation 2:  R_θ(v, θ) = M
```

---

## 4. Example: Rayleigh-Ritz and Kinematic Coupling

If you are using Euler-Bernoulli beam theory, the rotation is not independent of displacement:
```
θ(x) = dv(x)/dx
```
If you approximate the displacement along the beam `w(x)` using two shape functions `phi_1(x)` and `phi_2(x)`:
```
w(x) = c1 * phi_1(x) + c2 * phi_2(x)
```
Then the rotation is:
```
θ(x) = c1 * phi'_1(x) + c2 * phi'_2(x)
```
Here, your two unknowns are not `w` and `θ` at a point, but the coefficients `c1` and `c2`. 

The virtual variations are:
```
δw(x) = δc1 * phi_1(x) + δc2 * phi_2(x)
```
Substituting this into `δW_ext = δW_int` will yield:
```
(Coeff_1) * δc1 + (Coeff_2) * δc2 = 0
```
Since `δc1` and `δc2` are independent:
```
Equation 1:  Coeff_1 = 0
Equation 2:  Coeff_2 = 0
```
Which again provides 2 equations for the 2 unknown coefficients.
