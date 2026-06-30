# 03 — Tic-Tac-Toe (Deep Q-Learning)

A Reinforcement Learning (RL) agent that learns to play perfect Tic-Tac-Toe through self-play using a Deep Q-Network (DQN).

## Goal

Upgrade the tabular Q-learning agent to a Deep Q-Network (DQN). Understand the stability challenges of combining neural networks with reinforcement learning, and implement the two key solutions: Experience Replay and Target Networks.

## Architecture

* **State Representation**: Player-relative encoding. A 18-element vector representing the board from the active player's perspective:
  * Inputs 0-8: `1` where the current player has a piece, `0` otherwise.
  * Inputs 9-17: `1` where the opponent has a piece, `0` otherwise.
* **Q-Network**: A Multi-Layer Perceptron (MLP) mapping the 18-element input to 9 output Q-values (one for each cell).
* **Experience Replay**: A buffer of size 20,000 storing past transitions. Training is performed on random mini-batches sampled from this buffer to break temporal correlation.
* **Target Network**: A copy of the Q-network with frozen weights, updated periodically, used to compute stable Bellman targets.
* **Loss Function**: Huber Loss (Smooth L1 Loss) to minimize Bellman error.

## Training Setup

* **Optimizer**: Adam or RMSprop
* **Exploration**: Epsilon-greedy with exponential or linear decay
* **Symmetry**: Single network playing both sides via player-relative state representation

## Results

*To be filled by the student after training.*
