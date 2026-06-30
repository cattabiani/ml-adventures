# Tic-Tac-Toe DQN — Task Breakdown

## Tasks

### Task 1: State Representation ✅
- Player-relative encoding: 18-element vector (my pieces | opponent pieces)
- Allows single network to play both sides

### Task 2: Neural Network ✅
- MLP: 18 → 128 → 128 → 9 (Q-value per cell)
- ReLU activations

### Task 3: Replay Buffer ✅
- Deque-based, 50k capacity
- Stores (state, action, reward, next_state, done) transitions
- Random batch sampling

### Task 4: DQN Agent ✅
- Policy net + target net (deep copy, updated every 500 games)
- Epsilon-greedy action selection with illegal move masking
- Huber loss (SmoothL1Loss) + Adam optimizer (lr=0.001)
- Illegal moves masked in BOTH action selection and target computation

### Task 5: Training Loop ✅
- 50k self-play games (epsilon=0.5 for 40k, then 0.1 for 10k)
- Each player's moves treated as independent trajectory
- next_state = board on same player's next turn (standard +gamma Bellman)
- Terminal reward: winner * player

### Task 6: Evaluation ✅
- Never loses in 200k games against random (as X or O)
- Interactive play mode

## Key Insight

The -gamma zero-sum formulation (next_state = opponent's board, negate their value)
is theoretically correct but unstable with neural network training.
Using +gamma with next_state = same player's next turn is more stable because
positive values reinforce directly without cross-player sign confusion.

## Results
- Never loses against random in 200k games
- Trains in ~30 seconds on CPU
