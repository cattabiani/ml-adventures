# Tic-Tac-Toe DQN — Task Breakdown

## Goal
Implement a Deep Q-Network (DQN) agent that learns to play perfect Tic-Tac-Toe through self-play.

---

## Tasks

### Task 1: State Representation & Environment
* [ ] Copy `game.py` from `02-tic-tac-toe-rl` to this folder.
* [ ] Write a helper function in a new file (e.g., `utils.py` or in `model.py`) to convert the board tuple `(0, 1, -1, ...)` into a player-relative PyTorch tensor:
  * Input: Board tuple and the current player (`1` or `-1`).
  * Output: A tensor of shape `(18,)` or `(2, 3, 3)` containing:
    * Channel 1: `1` where the current player has a piece, `0` otherwise.
    * Channel 2: `1` where the opponent has a piece, `0` otherwise.

### Task 2: Neural Network (`model.py`)
* [ ] Create a PyTorch network class inheriting from `nn.Module`.
* [ ] Implement a Multi-Layer Perceptron (MLP):
  * Input layer: 18 units.
  * Hidden layer 1: 128 units + Rectified Linear Unit (ReLU).
  * Hidden layer 2: 128 units + ReLU.
  * Output layer: 9 units (representing the raw Q-values for each of the 9 board positions).

### Task 3: Replay Buffer (`agent.py`)
* [ ] Implement a `ReplayBuffer` class:
  * Under the hood, use a `collections.deque` with a maximum capacity (e.g., 10,000 or 50,000 transitions).
  * Implement `push(state, action, reward, next_state, done)` to add transitions.
  * Implement `sample(batch_size)` to return a random batch of transitions, converted to PyTorch tensors.

### Task 4: DQN Agent (`agent.py`)
* [ ] Implement the `DQNAgent` class:
  * Initialize two instances of your network: the **policy network** (updated every step) and the **target network** (frozen).
  * Implement `select_action(state, epsilon)`:
    * Choose a random legal move with probability `epsilon`.
    * Otherwise, pass the state through the policy network, **mask out the illegal moves** (set their Q-values to a very large negative number like `-1e9`), and select the move with the highest Q-value.
  * Implement `train_step(batch_size, gamma)`:
    * Sample a batch from the replay buffer.
    * Compute the predicted Q-values for the actions taken using the policy network.
    * Compute the target Q-values using the target network:
      * `target = reward + gamma * max(Q_target(next_state)) * (1 - done)`
    * Compute the loss between predictions and targets (prefer `nn.SmoothL1Loss` / Huber Loss).
    * Perform a gradient descent step on the policy network.

### Task 5: Training Loop (`main.py`)
* [ ] Write the self-play training loop:
  * Play games where the agent plays against itself, selecting actions using epsilon-greedy.
  * At each step, store the transition in the replay buffer.
  * Run a `train_step` after every move (once the buffer has enough samples).
  * Periodically (e.g., every 500 or 1000 steps), copy the weights of the policy network to the target network using `target_net.load_state_dict(policy_net.state_dict())`.
  * Implement epsilon decay (e.g., starting at `0.9` and decaying to `0.05` over training).

### Task 6: Evaluation & Play
* [ ] Implement an evaluation function that plays the agent (with `epsilon = 0`) against a random player.
* [ ] Verify that the agent never loses against the random player.
* [ ] Implement the interactive play mode so you can play against your trained agent.
