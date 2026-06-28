# Image Classifier — Task Breakdown

## Theory Refresher

A CNN applies small learnable filters (kernels) that slide across an image. Each filter detects a local pattern (edge, texture, color blob). Stacking multiple convolutional layers lets the network learn hierarchical features: edges → shapes → objects.

Key components you'll implement:
- **Convolutional layers** — filters that slide over the input (you know this as a stencil operation)
- **Activation functions** — non-linearity after each layer (ReLU is standard)
- **Pooling** — downsampling to reduce spatial dimensions (max pooling)
- **Fully-connected layers** — at the end, flatten the feature maps and classify
- **Cross-entropy loss** — standard loss for multi-class classification
- **Backpropagation** — PyTorch handles this via autograd, but you should understand what it's doing

## Tasks

### Task 1: Setup and data loading ✅
- Install PyTorch and torchvision
- Load CIFAR-10 using `torchvision.datasets`
- Create DataLoaders for train and test sets
- Visualize a few sample images to confirm it works
- Understand the shape of the data: (batch, channels, height, width)

### Task 2: Build the model ✅
- Define a CNN class inheriting from `nn.Module`
- Architecture:
  - 3 convolutional layers (32 → 64 → 128 channels) with ReLU and max pooling
  - Batch Normalization after each conv (conv → BN → ReLU → pool)
  - Padding=1 to preserve spatial dimensions
  - Flatten + fully-connected layer to 10 classes
  - Dropout (0.5) before linear layer

### Task 3: Training loop ✅
- Write the training loop from scratch (no high-level wrappers)
- Components: forward pass, loss computation, backward pass, optimizer step
- Using Cross-Entropy Loss and Stochastic Gradient Descent (lr=0.01, momentum=0.9)
- Cosine Annealing learning rate scheduler (T_max=80)
- Track average training loss per epoch
- MPS (Metal Performance Shaders) GPU acceleration on M4 Mac

### Task 4: Evaluation ✅
- Run the trained model on the test set
- Compute accuracy (train and test) to diagnose overfitting/underfitting

### Task 5: Experimentation ✅
- [x] Added padding=1 (preserves spatial dims, cleaner architecture)
- [x] Added dropout — reduced overfitting
- [x] Added data augmentation (RandomCrop + RandomHorizontalFlip) — eliminated overfitting
- [x] Added Batch Normalization — 74% → 79% test accuracy
- [x] Increased channels (32 → 64 → 128) — more capacity without overfitting
- [x] Added Cosine Annealing learning rate scheduler — 79% → 85% test accuracy

### Task 6: GPU awareness ✅
- Code detects MPS (Apple Silicon GPU) and falls back to CPU
- Model and data move to device automatically

## Results

| Run | Changes | Train Acc | Test Acc |
|-----|---------|-----------|----------|
| 1 | Baseline (16→32→64, no BN, flat LR) | 74.18% | 74.41% |
| 2 | + Batch Normalization | 79.38% | 78.62% |
| 3 | + Bigger channels (32→64→128) + Cosine LR | 87.89% | 85.32% |

## Target
- ~~Reach >70% accuracy on CIFAR-10 test set~~ ✅ (70.49%)
- ~~Stretch goal: >80%~~ ✅ (85.32%)

## What "done" looks like
- Clean, well-commented Python script(s) in this folder ✅
- README updated with results ✅
- You can explain every line of code if asked ✅
