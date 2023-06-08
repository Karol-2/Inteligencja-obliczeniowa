import gym

env = gym.make('FrozenLake8x8-v1', render_mode="human",is_slippery=False)
observation, info = env.reset(seed=42)
actions = [2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]

for move in actions:
    action = move
    observation, reward, terminated, truncated, info = env.step(action)
    env.render()

env.close()
