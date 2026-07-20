# 2D Elasticity FNO Surrogate — Task Breakdown

## Tasks

### Task 1: PyTorch-native Q1 FEM Solver & Data Gen
- Implement the FEMSolver class in src/data_gen.py.
  - compute_k_ref: Compute standard bilinear element stiffness matrix using 2x2 Gauss Quadrature.
  - compute_element_dofs: Map local to global DOFs.
  - solve: Assemble global K (using coordinate indices for sparse creation), distribute forces F, apply Dirichlet boundary conditions (x=0 fixed), and solve using torch.linalg.solve.
  - Stress post-processing: Calculate strain and stress at element centers to get the von Mises stress field.
- Implement random smooth field generation for E(x, y) and body forces using a Gaussian kernel.
- Save generated datasets (inputs: E, f_x, f_y; outputs: u_x, u_y, sigma_vm) as .pt files.

### Task 2: FNO2d Architecture
- Implement SpectralConv2d in src/models.py.
  - Perform 2D FFT, filter modes, multiply by complex parameters, and project back via 2D IFFT.
- Implement FNO2d in src/models.py.
  - Coordinate injection (appending mesh grid coordinates).
  - Lifting layer, 4 Spectral blocks (with local Conv2d skip connections), and final Projection layers.

### Task 3: Training Pipeline
- Implement ElasticityDataset in src/training.py.
  - Load datasets and append grid coordinates to inputs.
- Implement RelativeL2Loss.
- Write training loop saving the best model and logging relative L2 loss per epoch.

### Task 4: Evaluation & Solver Speedup
- Write src/eval.py to:
  - Load trained FNO model.
  - Benchmark inference latency vs FEM solver time.
  - Compute average relative L2 errors.
  - Save visual comparisons (E, ground-truth sigma_vm, predicted sigma_vm) to disk.

### Task 5: Unit Tests
- Implement tests in tests/test_shapes.py to verify tensor shapes through training/evaluation.
