"""
Tic-Tac-Toe Q-Learning Agent

Learns to play perfect tic-tac-toe through self-play using tabular Q-learning.
Q-values are stored from the mover's perspective (positive = good for whoever's turn it is).
In zero-sum games, the Bellman update uses -γ*Q(s') because the opponent's gain is our loss.
"""

from game import play_game, legal_moves, check_winner, make_move, print_game, print_board
import random

# --- Hyperparameters ---
alpha = 0.5   # learning rate
gamma = 0.9   # discount factor
epsilon = 0.5  # exploration rate (will be decayed)

# --- Q-table ---
qtable = {}


def best_action(board):
    """Return (action, q_value) for the best move from the current player's perspective."""
    actions = legal_moves(board)
    pairs = [(a, qtable.get((board, a), 0)) for a in actions]
    action, q_value = max(pairs, key=lambda p: p[1])
    return action, q_value


def update(board, player, action):
    """Online Bellman update after a single move."""
    new_board = make_move(board, action, player)
    reward = check_winner(new_board)
    q_value = 0
    if reward == 0 and legal_moves(new_board):
        _, q_value = best_action(new_board)
    key = board, action
    curr_v = qtable.get(key, 0)
    # Note: -gamma*q_value because opponent's best is our worst (zero-sum)
    qtable[key] = curr_v + alpha * (reward * player - gamma * q_value - curr_v)


def step(board, player):
    """Epsilon-greedy action selection with online Q-update."""
    if random.random() < epsilon:
        action = random.choice(legal_moves(board))
    else:
        action, _ = best_action(board)
    update(board, player, action)
    return action


def random_step(board, _player):
    """Uniformly random action (for evaluation)."""
    return random.choice(legal_moves(board))


# --- Training ---
print("Training (400k games, epsilon=0.5)...")
for i in range(400_000):
    play_game(step, step)

epsilon = 0.1
print("Training (100k games, epsilon=0.1)...")
for i in range(100_000):
    play_game(step, step)

print(f"Q-table size: {len(qtable)} state-action pairs")

# --- Evaluation ---
epsilon = 0
print("Evaluating (100k games vs random)...")
for i in range(100_000):
    winner, history = play_game(step, random_step)
    if winner < 0:
        print(f"Failed at game {i}: agent lost as X")
        print_game(history, winner)
        break
    winner, history = play_game(random_step, step)
    if winner > 0:
        print(f"Failed at game {i}: agent lost as O")
        print_game(history, winner)
        break
else:
    print("Agent never lost in 200k games against random!")

# --- Interactive play ---


def human_step(board, player):
    print_board(board)
    print(f"You are {'X' if player == 1 else 'O'}. Board positions:")
    print("0 1 2")
    print("3 4 5")
    print("6 7 8")
    while True:
        try:
            move = int(input("Your move (0-8): "))
            if move in legal_moves(board):
                return move
            print("Illegal move, try again.")
        except (ValueError, EOFError):
            print("Enter a number 0-8.")


print("\n--- Play against the agent! (Ctrl+C to quit) ---")
result_msg = {1: "You win!", -1: "Agent wins!", 0: "Draw!"}
try:
    while True:
        print("\nYou play X (first), agent plays O.\n")
        winner, history = play_game(human_step, step)
        print_board(make_move(history[-1][0], history[-1][2], history[-1][1]))
        print(result_msg[winner])
except KeyboardInterrupt:
    print("\nThanks for playing!")
