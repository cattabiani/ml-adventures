# 2D Linear Elasticity FNO Surrogate Model

This project implements a 2D Fourier Neural Operator (FNO) in PyTorch to act as a fast surrogate solver for structural plane stress linear elasticity.

The objective is to train a model that takes spatial distributions of material properties (Young's modulus) and body forces as inputs, and predicts the displacement fields and von Mises stress field.

## PDE Formulation (Plane Stress Linear Elasticity)

We solve the equilibrium equation over a 2D domain:
  div(sigma) + f = 0

where:
- sigma is the Cauchy stress tensor.
- f is the body force vector field.

Constitutive Relation (Hooke's Law):
  sigma = D * epsilon

where:
- epsilon is the infinitesimal strain tensor: epsilon_ij = 0.5 * (du_i/dx_j + du_j/dx_i)
- D is the plane stress stiffness tensor (isotropic material), parametrized by Young's modulus E(x, y) and Poisson's ratio nu.

Boundary Conditions:
- Dirichlet: u = 0 on the left boundary (x = 0).
- Neumann: Traction free / volume force loads.

Von Mises Stress (for 2D plane stress):
  sigma_vm = sqrt(sigma_xx^2 + sigma_yy^2 - sigma_xx * sigma_yy + 3 * sigma_xy^2)

## Directory Architecture

- configs/config.yaml: Hyperparameter and simulation configurations.
- src/data_gen.py: Synthetic dataset generator via a PyTorch-native Q1 bilinear elements FEM solver.
- src/models.py: FNO2d neural network architecture.
- src/training.py: Training script using Relative L2 Loss.
- src/eval.py: Performance evaluation and comparison against the classical FEM solver.
- tests/test_shapes.py: Basic shape assertions for models and data generators.
