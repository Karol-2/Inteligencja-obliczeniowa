import gym

env = gym.make('Taxi-v3', render_mode="human")

observation, info = env.reset(seed=42)
moves = [1, 1, 1, 4, 3, 3, 3, 0, 0, 3, 3, 0, 0, 5]

for move in moves:
    action = move
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        observation, info = env.reset()
env.close()
