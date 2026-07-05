# ML Adventures

An AI-powered learning project. I'm a senior software engineer (C++/Python, High-Performance Computing (HPC), numerical simulation) building Machine Learning (ML) skills through hands-on projects — with an AI as teacher, not as substitute.

## How this works

- **I write the code.** The AI provides direction, asks questions, reviews my work, and pushes back when I'm wrong.
- **Framing, design, and task documents** are written by the AI under my supervision.
- **Projects are real and complete** — each one trains a model, shows results, and has a clear README.
- **Training runs** on Kaggle/Colab free-tier Graphics Processing Units (GPUs).
- **AI steering** lives in `.kiro/steering/` — it sets ground rules for how the AI interacts with me (teacher, not substitute).

## Roadmap

### Phase 1: Core ML & RL
Get fluent in PyTorch, modern training workflows, and Reinforcement Learning (RL) fundamentals.

- [x] Image classifier (Convolutional Neural Network (CNN) on CIFAR-10) — 85% test accuracy
- [x] Tabular Q-learning agent (Tic-Tac-Toe — Bellman equation, self-play)
- [x] Deep Q-Network (DQN) agent (Tic-Tac-Toe — replay buffer, target network)
- [x] DQN on CartPole (single-agent, dense reward, Gymnasium environment)

### Phase 2: Transformers & Embeddings
Understand attention, embeddings, and generative models.

- [x] Character-level GPT (build a transformer from scratch, train on GPU)
- [ ] Fine-tune a small language or vision model on a custom task
- [ ] Semantic search / retrieval system

### Phase 3: Specialization
One or two deeper projects — pick based on interest and job market at the time.

- [ ] Diffusion models (image or video generation)
- [ ] World models (action-conditioned environment prediction)
- [ ] ML infrastructure (distributed training, model serving, custom Compute Unified Device Architecture (CUDA) kernels)
- [ ] Scientific ML (physics-informed neural networks, surrogate models)
- [ ] RL at scale (Proximal Policy Optimization (PPO) / policy gradient on a visual environment)

## Background

I have 8+ years of production C++/Python, a PhD in Computational Mechanics, and HPC/distributed computing experience. Strong applied math foundations (linear algebra, optimization, Partial Differential Equations (PDEs)). I've done some small ML projects, but no professional ML experience yet. This repo is my path from numerical software engineer to ML engineer.

## Progress

| # | Project | Status | Key Result |
|---|---------|--------|------------|
| 01 | Image Classifier (CIFAR-10) | ✅ | 85% test accuracy |
| 02 | Tic-Tac-Toe (Tabular Q-Learning) | ✅ | Never loses vs random |
| 03 | Tic-Tac-Toe (DQN) | ✅ | Never loses vs random |
| 04 | CartPole (DQN) | ✅ | 500/500 perfect |
| 05 | Character-Level GPT | ✅ | 2.24 train / 2.27 val loss |
