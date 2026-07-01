# CartPole DQN — Task Breakdown

## Tasks

### Task 1: Explore the environment ✅
- Installed Gymnasium + pygame
- Played CartPole manually to understand dynamics
- State: 4 continuous values, actions: 2 discrete, reward: +1 per step

### Task 2: DQN Agent ✅
- MLP: 4 → 64 → 64 → 2 (ModuleList + functional ReLU)
- Replay buffer with deque, stores (state, action, next_state, done)
- Epsilon-greedy action selection
- Soft target network update (tau=0.005)

### Task 3: Training loop ✅
- Gymnasium loop: reset → step → store → train
- Epsilon decay (0.5 → 0.05 over 10k games)
- Best model checkpoint saved based on running average steps

### Task 4: Evaluation ✅
- 100 episodes with epsilon=0 using best checkpoint
- Average 500.0 / 500 steps — perfectly solved

## Key differences from Tic-Tac-Toe DQN
- Single agent (no self-play, no sign conventions)
- Continuous state (not discrete board positions)
- Dense reward (every step, not just terminal)
- Both actions always legal (no masking)
- DQN instability is the main challenge (not reward shaping)
- gamma=0.99 needed (vs 0.9 for tic-tac-toe) due to long episodes
