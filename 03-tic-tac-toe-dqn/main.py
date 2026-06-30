from game import encode_board
import torch
from collections import deque
import random
import copy

class DQN(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(18, 36)
        self.linear2 = torch.nn.Linear(36, 72)
        self.linear3 = torch.nn.Linear(72, 9)

        self.dropout = torch.nn.Dropout(0.5)

    def forward(self, x):
        x = self.linear1(x)
        x = torch.nn.functional.relu(x)
        x = self.linear2(x)
        x = torch.nn.functional.relu(x)
        x = self.linear3(x)
        return x

class ReplayBuffer:
    def __init__(self):
        self.dq = deque(maxlen=10_000)
    
    def append(self, state, action, reward, next_state, done):
        self.dq.append((state, action, reward, next_state, done))

    def sample(self, batch_size):
        batch = random.sample(self.dq, batch_size)
        states, actions, rewards, next_states, dones = zip(*batch)
        
        return (
            torch.tensor(states, dtype=torch.float32),
            torch.tensor(actions, dtype=torch.long),
            torch.tensor(rewards, dtype=torch.float32),
            torch.tensor(next_states, dtype=torch.float32),
            torch.tensor(dones, dtype=torch.float32)
        )


class Agent:
    def __init__(self):
        self.policy_net = DQN()
        # Copy weights initially
        self.target_net = copy.deepcopy(self.policy_net)
        self.target_net.eval()
        
        self.optimizer = torch.optim.Adam(self.policy_net.parameters(), lr=0.001)
        self.loss_fn = torch.nn.SmoothL1Loss() # Huber loss (more stable than MSE)
        
    def select_action(self, state, epsilon, legal_moves):
        pass
        # Your turn to write this!
