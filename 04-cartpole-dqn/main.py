import gymnasium as gym
import random
import torch
from collections import deque
import copy

env = gym.make("CartPole-v1")

ngames = 60_000


class DQN(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = torch.nn.ModuleList([torch.nn.Linear(4, 64), torch.nn.Linear(64, 64), torch.nn.Linear(64, 2)])
    
    def forward(self, x):
        for layer in self.layers[:-1]:
            x = layer(x)
            x = torch.nn.functional.relu(x)
        
        return self.layers[-1](x)

class ReplayBuffer:
    def __init__(self):
        self.dq = deque(maxlen=50_000)
    
    def extend(self, history):
        states, actions, dones = zip(*history)
        next_states = states[1:] + states[-1:]
        self.dq.extend(zip(states, actions, next_states, dones))

    def sample(self, batch_size):
        batch = random.sample(self.dq, batch_size)
        states, actions, next_states, dones = zip(*batch)
        
        return (
            torch.tensor(states, dtype=torch.float32),
            torch.tensor(actions, dtype=torch.long),
            torch.tensor(next_states, dtype=torch.float32),
            torch.tensor(dones, dtype=torch.float32)
        )



def random_step(_state):
    return random.randint(0, 1)

def run_game(gen_action_fn, max_steps=500):
    state, info = env.reset()
    history = []
    while True:
        action = gen_action_fn(state)
        
        new_state, reward, terminated, truncated, info = env.step(action)
        history.append((state, action, terminated))
        state = new_state
        
        if terminated or truncated or len(history) >= max_steps:
            break
    return history


class Agent:
    def __init__(self):
        self.policy_net = DQN()
        self.target_net = DQN()
        self.update_target_net()

        self.optimizer = torch.optim.Adam(self.policy_net.parameters(), lr=0.001)
        self.loss_fn = torch.nn.SmoothL1Loss()

        self.buffer = ReplayBuffer()
        self.epsilon = 0.5
        # self.scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(self.optimizer, T_max=ngames)

    def select_action(self, state):
        if random.random() < self.epsilon:
            return random_step(state)
        return self.policy_net(torch.as_tensor(state)).argmax().item()

    def train_step(self, batch_size, gamma):
        if len(self.buffer.dq) < batch_size:
            return -1
        
        states, actions, next_states, dones = self.buffer.sample(batch_size)
        # print(states.size(), actions.size(), next_states.size(), dones.size())

        cont = 1-dones

        q_predicted = self.policy_net(states)[torch.arange(batch_size), actions]
        q_next = self.target_net(next_states).max(dim=1).values

        target = cont * (1 + gamma * q_next)


        self.policy_net.zero_grad()
        loss = self.loss_fn(q_predicted, target.detach())
        loss.backward()
        self.optimizer.step()
        # self.scheduler.step()

        # In train_step, after optimizer.step():
        tau = 0.005
        for target_param, policy_param in zip(self.target_net.parameters(), self.policy_net.parameters()):
            target_param.data.copy_(tau * policy_param.data + (1 - tau) * target_param.data)

        return loss.item()


    def update_target_net(self):
        self.target_net.load_state_dict(self.policy_net.state_dict())




agent = Agent()

best_avg = 0
best_state = None
len_h = 0
for igame in range(ngames):
    agent.epsilon = max(0.05, 0.5 - igame * 0.5 / 10_000)

    with torch.no_grad():
        history = run_game(agent.select_action)
    agent.buffer.extend(history)
    loss = agent.train_step(batch_size=500, gamma=0.99)
    len_h += len(history)
    if igame % 1000 == 0:
        avg_steps = len_h / 1000
        if avg_steps > best_avg:
            best_avg = avg_steps
            best_state = copy.deepcopy(agent.policy_net.state_dict())
        print(f"Game {igame}, loss: {loss:.4f}, steps survived: {avg_steps:.1f}, best: {best_avg:.1f}, epsilon: {agent.epsilon:.3f}")
        len_h = 0

# Load the best model for evaluation
if best_state:
    agent.policy_net.load_state_dict(best_state)


agent.epsilon = 0
total_steps = 0
n_eval = 100
with torch.no_grad():
    for i in range(n_eval):
        history = run_game(agent.select_action)
        total_steps += len(history)

avg = total_steps / n_eval
print(f"Evaluation: avg steps survived = {avg:.1f} / 500 (over {n_eval} games)")
if avg >= 475:
    print("Solved!")
else:
    print("Not solved yet.")


    