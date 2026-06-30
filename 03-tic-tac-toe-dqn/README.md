# 03 — Tic-Tac-Toe (Deep Q-Network)

A Reinforcement Learning (RL) agent that learns to play perfect tic-tac-toe through self-play using a Deep Q-Network (DQN).

## Goal

Upgrade the tabular Q-learning agent to a neural network. Understand why DQN needs experience replay and a target network for stability, and how to handle two-player self-play with a single network.

## Architecture

- **State Representation:** Player-relative encoding (18-element vector: my pieces | opponent's pieces)
- **Q-Network:** Multi-Layer Perceptron (MLP), 18 → 128 → 128 → 9
- **Experience Replay:** Buffer of 50k transitions, random mini-batch sampling
- **Target Network:** Frozen copy updated every 500 games
- **Loss:** Huber Loss (SmoothL1Loss)
- **Optimizer:** Adam (lr=0.001)

## Training Setup

- 50k self-play games (epsilon=0.5 for 40k, then 0.1 for 10k)
- Batch size: 100, gamma: 0.9
- Each player's moves treated as independent trajectory (next_state = my next turn)
- Terminal reward: winner * player (+1 win, -1 loss, 0 draw)
- Illegal moves masked in both action selection and target computation

## Results

- **Never loses** against a random opponent in 200k evaluation games
- Loss converges from ~0.08 to ~0.01 over training
- Trains in ~30 seconds on CPU

## Key Learnings

- In two-player DQN, treating each player's moves as a separate trajectory with `+gamma` is more stable than the `-gamma` zero-sum formulation (though both are theoretically correct)
- Illegal move masking is critical in both action selection AND target Q-value computation — without it, the network learns corrupted targets
- Experience replay breaks temporal correlation and allows efficient reuse of data
- Target network prevents the "chasing a moving target" instability where predictions and targets shift simultaneously
- Player-relative state encoding allows a single network to play both sides
