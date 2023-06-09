import gym
import numpy as np
# NIE DZIAŁA, W SENSIE WPADA DO DZIURY

def value_iteration(env, gamma=0.9, theta=1e-8, max_iterations=1000):
    env.reset(seed=42)
    V = np.zeros(env.observation_space.n)

    for i in range(max_iterations):
        delta = 0

        for s in range(env.observation_space.n):
            v = V[s]

            Q = np.zeros(env.action_space.n)
            for a in range(env.action_space.n):
                for prob, next_state, reward, done in env.P[s][a]:
                    Q[a] += prob * (reward + gamma * V[next_state])

            best_action = np.argmax(Q)
            V[s] = Q[best_action]

            delta = max(delta, abs(v - V[s]))

        if delta < theta:
            break

    policy = np.zeros(env.observation_space.n, dtype=int)
    for s in range(env.observation_space.n):
        Q = np.zeros(env.action_space.n)
        for a in range(env.action_space.n):
            for prob, next_state, reward, done in env.P[s][a]:
                Q[a] += prob * (reward + gamma * V[next_state])
        policy[s] = np.argmax(Q)

    return policy


# Tworzymy środowisko FrozenLake
env = gym.make('FrozenLake8x8-v1', is_slippery=False)
env.reset(seed=42)

# Wywołujemy Value Iteration Algorithm
optimal_policy = value_iteration(env)

# Wyświetlamy optymalną politykę
print("Optymalna polityka:")
print(optimal_policy)

env = gym.make('FrozenLake8x8-v1', is_slippery=False, render_mode="human")
env.reset(seed=42)
for action in optimal_policy:
    action = int(action)
    env.render()
    observation, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        break
