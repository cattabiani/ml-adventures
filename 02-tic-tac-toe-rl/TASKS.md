# Tic-Tac-Toe Q-Learning — Task Breakdown

## Theory Refresher

Q-learning assigns a value Q(s, a) to each (state, action) pair — "if I'm in state s and take action a, how much future reward can I expect?" The agent updates this table after every move using the Bellman equation:

```
Q(s, a) ← Q(s, a) + α * (reward - γ * max_a' Q(s', a') - Q(s, a))
```

In zero-sum two-player games, the standard `+ γ * max Q(s')` becomes `- γ * max Q(s')` because the opponent's best move (next state) is bad for us.

Where:
- **α (alpha)** — learning rate: how much to trust the new information vs the old estimate
- **γ (gamma)** — discount factor: how much to value future rewards vs immediate ones
- **reward** — signal from the environment (win=+1, lose=-1, draw=0, ongoing=0)
- **s'** — the next state after taking action a
- **max_a' Q(s', a')** — the opponent's best move from the next state (bad for us in zero-sum)

## Tasks

### Task 1: Game environment ✅
- Board represented as tuple of 9 ints (0=empty, 1=X, -1=O)
- Tuple is hashable — works directly as Q-table dictionary key
- Win detection via 8 possible lines (rows, cols, diagonals)
- `play_game` takes two player functions, returns winner + history

### Task 2: Q-table and state representation ✅
- Q-table: Python dictionary mapping (board_tuple, action) → float
- Q-values stored from mover's perspective (positive = good for whoever's turn it is)
- `best_action(board)` returns action with highest Q-value

### Task 3: Training loop (self-play) ✅
- Online updates: Q-value updated immediately after each move
- Epsilon-greedy exploration (ε=0.5 for 400k games, then ε=0.1 for 100k games)
- Self-play: same agent plays both X and O
- Hyperparameters: α=0.5, γ=0.9

### Task 4: Evaluation ✅
- Against random opponent: never loses in 200k games (playing as both X and O)
- Interactive play mode: human can play against trained agent

### Task 5: Understanding ✅
- Why -γ instead of +γ: opponent's best value is our worst (zero-sum)
- Why slow convergence: values propagate one step per game visit ("bubble sort" of RL)
- Why epsilon matters: without exploration, agent converges to narrow set of games
- Bellman is exact for this problem (finite, deterministic, fully observable, zero-sum)

## Results
- Q-table size: ~50k state-action pairs
- Never loses against random in 200k evaluation games
- Converges with 500k training games (400k at ε=0.5 + 100k at ε=0.1)

## Success Criteria ✅
- Agent never loses against a random opponent ✅
- Clean, well-commented code ✅
- Can explain every design choice ✅
