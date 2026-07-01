# 04 — CartPole (Deep Q-Network)

A DQN agent that learns to balance a pole on a cart using only reward signal.

## Goal

Implement DQN for a single-agent continuous-state environment. No self-play, no illegal moves, dense reward. Clean practice of the core algorithm.

## Environment

- **CartPole-v1** (Gymnasium)
- State: 4 floats (cart position, cart velocity, pole angle, pole angular velocity)
- Actions: 2 (push left, push right)
- Reward: +1 per timestep the pole stays up
- Episode ends: pole > 12°, cart off-screen, or 500 steps survived
- Solved: average reward ≥ 475 over 100 consecutive episodes

## Architecture

- **Q-Network:** MLP 4 → 64 → 64 → 2
- **Experience Replay:** Deque buffer, 50k capacity
- **Target Network:** Soft update (tau=0.005) every training step
- **Loss:** Huber Loss (SmoothL1Loss)
- **Optimizer:** Adam (lr=0.001)

## Training Setup

- 60k self-play games
- Epsilon decay: 0.5 → 0.05 over first 10k games
- Batch size: 500, gamma: 0.99
- Best model checkpoint saved during training

## Results

- **500.0 / 500** avg steps over 100 evaluation games (perfect play)
- Best training checkpoint reached 498.3 avg steps (with epsilon=0.05 noise)
- Agent learns near-perfect policy around game 35-40k but oscillates — best checkpoint captures peak performance

## Key Learnings

- gamma=0.99 is critical for CartPole (need to value rewards 100+ steps in the future)
- DQN is inherently unstable — policy oscillates between good and bad even after "solving" the task
- Saving the best checkpoint is standard practice, not a hack
- Larger batch size (500) helps stabilize gradients
- Soft target updates are smoother than hard copies but don't fully prevent instability
- The reward doesn't need to be negative at death — the absence of future reward (via done flag) is sufficient signal
