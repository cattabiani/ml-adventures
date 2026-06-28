# 01 — Image Classifier

A Convolutional Neural Network (CNN) trained on CIFAR-10 to classify images into 10 categories.

## Goal

Build an image classifier from scratch in PyTorch. No copy-pasting from tutorials — write every line yourself.

## Status

Complete — target of 80% test accuracy reached and exceeded.

## Architecture

- 3-layer CNN with channel progression: 32 → 64 → 128
- Batch Normalization after each conv layer (conv → BN → ReLU → MaxPool)
- Dropout (0.5) before final linear layer
- LazyLinear output layer (10 classes)

## Training Setup

- Optimizer: Stochastic Gradient Descent (SGD), lr=0.01, momentum=0.9
- Scheduler: Cosine Annealing LR (T_max=80)
- Data augmentation: random crop (padding=4), random horizontal flip
- Batch size: 64
- Epochs: 80
- Hardware: Apple MPS

## Results

| Run | Changes | Train Acc | Test Acc |
|-----|---------|-----------|----------|
| 1 | Baseline (16→32→64, no BN, flat LR) | 74.18% | 74.41% |
| 2 | + BatchNorm | 79.38% | 78.62% |
| 3 | + Bigger channels (32→64→128) + Cosine LR | 87.89% | 85.32% |

## Key Learnings

- Batch Normalization stabilizes training by bounding activations, smoothing the loss landscape, and allowing higher effective learning rates
- Cosine annealing LR provides high LR early (exploration) and low LR late (fine-tuning)
- With no overfitting, increasing model capacity (channels) translates directly to better accuracy
- The train-test gap only appeared after increasing capacity (2.5%), indicating mild overfitting
