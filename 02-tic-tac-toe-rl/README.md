# 02 — Tic-Tac-Toe (Tabular Q-Learning)

A Reinforcement Learning (RL) agent that learns to play perfect tic-tac-toe through self-play using tabular Q-learning.

## Goal

Implement Q-learning from scratch — no RL libraries. Understand the Bellman equation, exploration vs exploitation, and how an agent learns purely from game outcomes.

## Architecture

- **State:** Board as a tuple of 9 ints (0=empty, 1=X, -1=O) — hashable, used directly as dict key
- **Q-table:** Dictionary mapping (board, action) → float value from mover's perspective
- **Update rule:** Online Bellman with negated discount (zero-sum: opponent's gain = my loss)
- **Exploration:** Epsilon-greedy with decay (0.5 → 0.1)

## Training

- 500k self-play games (400k at ε=0.5, 100k at ε=0.1)
- α=0.5, γ=0.9
- Online updates (Q-value updated after each move, no history replay)
- Runs in a few seconds on CPU

## Results

- **Never loses** against a random opponent in 200k evaluation games (as X or O)
- Q-table converges to ~50k state-action pairs
- Interactive play mode confirms agent plays optimally (always draws or wins)

## Key Learnings

- In zero-sum games, the Bellman update uses `-γ * max Q(s')` instead of `+γ * max Q(s')` because the next state value represents the opponent's best move
- Q-learning convergence is slow ("bubble sort" — values propagate one step per visit) but provably correct for finite state spaces
- High exploration (ε=0.5) during bulk training is critical to ensure all defensive positions are visited
- The Q-table stores values from the mover's perspective — sign conventions are the hardest part to get right in two-player games
