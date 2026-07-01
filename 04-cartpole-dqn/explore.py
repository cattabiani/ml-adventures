"""
Explore the CartPole environment manually.
Run this to understand the state, actions, and dynamics.
"""

import gymnasium as gym

env = gym.make("CartPole-v1", render_mode="human")

state, info = env.reset()
print(f"State shape: {state.shape}")
print(f"State: [cart_pos, cart_vel, pole_angle, pole_angular_vel]")
print(f"Action space: {env.action_space}  (0=left, 1=right)")
print(f"State: {state}")
print()
print("Controls: type 0 (left) or 1 (right), enter to step. 'q' to quit.")
print()

total_reward = 0
done = False
while not done:
    try:
        action = input("Action (0/1): ").strip()
        if action == 'q':
            break
        action = int(action)
        if action not in [0, 1]:
            print("Must be 0 or 1")
            continue
    except (ValueError, EOFError):
        break

    state, reward, terminated, truncated, info = env.step(action)
    done = terminated or truncated
    total_reward += reward
    print(f"  State: pos={state[0]:.3f}, vel={state[1]:.3f}, angle={state[2]:.3f}, ang_vel={state[3]:.3f}")
    print(f"  Reward: {reward}, Total: {total_reward}, Done: {done}")

print(f"\nEpisode finished. Total reward: {total_reward}")
env.close()
