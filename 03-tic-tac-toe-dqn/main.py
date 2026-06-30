from game import encode_board, legal_moves, play_game, print_game, print_board, make_move
import torch
from collections import deque
import random
import copy
import numpy as np

epsilon = 0.5

class DQN(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(18, 128)
        self.linear2 = torch.nn.Linear(128, 128)
        self.linear3 = torch.nn.Linear(128, 9)

    def forward(self, x):
        x = self.linear1(x)
        x = torch.nn.functional.relu(x)
        x = self.linear2(x)
        x = torch.nn.functional.relu(x)
        x = self.linear3(x)
        return x

class ReplayBuffer:
    def __init__(self):
        self.dq = deque(maxlen=50_000)
    
    def append(self, state, action, reward, next_state, done):
        self.dq.append((state, action, reward, next_state, done))

    def sample(self, batch_size):
        batch = random.sample(self.dq, batch_size)
        states, actions, rewards, next_states, dones = zip(*batch)
        
        return (
            torch.tensor(np.array(states), dtype=torch.float32),
            torch.tensor(actions, dtype=torch.long),
            torch.tensor(rewards, dtype=torch.float32),
            torch.tensor(np.array(next_states), dtype=torch.float32),
            torch.tensor(dones, dtype=torch.float32)
        )


class Agent:
    def __init__(self):
        self.policy_net = DQN()
        self.target_net = copy.deepcopy(self.policy_net)
        self.target_net.eval()
        
        self.optimizer = torch.optim.Adam(self.policy_net.parameters(), lr=0.001)
        self.loss_fn = torch.nn.SmoothL1Loss()
        self.buffer = ReplayBuffer()
        
    def select_action(self, board, player):
        if random.random() < epsilon:
            return random.choice(legal_moves(board))
        
        state = torch.tensor(encode_board(board, player))
        with torch.no_grad():
            q_values = self.policy_net(state)
        # mask illegal moves
        for i in range(9):
            if i not in legal_moves(board):
                q_values[i] = -1e9
        return q_values.argmax().item()

    def train_step(self, batch_size, gamma):
        if len(self.buffer.dq) < batch_size:
            return None

        states, actions, rewards, next_states, dones = self.buffer.sample(batch_size)
        q = self.policy_net(states)
        predicted = q[torch.arange(batch_size), actions]

        nq = self.target_net(next_states)
        # mask illegal moves in target
        occupied = (next_states[:, :9] + next_states[:, 9:]) > 0
        nq[occupied] = -1e9
        max_next_q = nq.max(dim=1).values

        target = rewards + gamma * (1-dones) * max_next_q
        loss = self.loss_fn(predicted, target.detach())
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        return loss.item()


agent = Agent()

for i in range(50_000):
    epsilon = 0.5 if i < 40_000 else 0.1
    winner, history = play_game(agent.select_action, agent.select_action)

    # each player's moves as independent trajectory
    # next_state = board on this player's NEXT turn
    x_moves = [(b, p, a) for b, p, a in history if p == 1]
    o_moves = [(b, p, a) for b, p, a in history if p == -1]

    for moves in [x_moves, o_moves]:
        if not moves:
            continue
        for j, (board, p, action) in enumerate(moves):
            state = encode_board(board, p)
            if j + 1 < len(moves):
                next_state = encode_board(moves[j + 1][0], p)
                r, d = 0, 0
            else:
                next_state = np.zeros(18, dtype=np.float32)
                r, d = winner * p, 1
            agent.buffer.append(state, action, r, next_state, d)

    agent.train_step(batch_size=100, gamma=0.9)
    if i % 500 == 0:
        agent.target_net.load_state_dict(agent.policy_net.state_dict())


def random_step(board, _player):
    return random.choice(legal_moves(board))

# --- Evaluation ---
epsilon = 0
print("Evaluating (200k games vs random)...")
for i in range(100_000):
    winner, history = play_game(agent.select_action, random_step)
    if winner < 0:
        print(f"Failed at game {i}: agent lost as X")
        print_game(history, winner)
        break
    winner, history = play_game(random_step, agent.select_action)
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
        winner, history = play_game(human_step, agent.select_action)
        print_board(make_move(history[-1][0], history[-1][2], history[-1][1]))
        print(result_msg[winner])
except KeyboardInterrupt:
    print("\nThanks for playing!")
