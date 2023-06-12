import gym
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

env = gym.make('FrozenLake-v1', render_mode="human")

action = ctrl.Antecedent(np.arange(0, 4, 1), 'action')
value = ctrl.Consequent(np.arange(0, 1, 0.1), 'value')

action['left'] = fuzz.trimf(action.universe, [0, 0, 1])
action['down'] = fuzz.trimf(action.universe, [0, 1, 2])
action['right'] = fuzz.trimf(action.universe, [1, 2, 3])
action['up'] = fuzz.trimf(action.universe, [2, 3, 3])

value['low'] = fuzz.trimf(value.universe, [0, 0, 0.5])
value['medium'] = fuzz.trimf(value.universe, [0, 0.5, 1])
value['high'] = fuzz.trimf(value.universe, [0.5, 1, 1])

rule1 = ctrl.Rule(action['left'], value['low'])
rule2 = ctrl.Rule(action['down'], value['low'])
rule3 = ctrl.Rule(action['right'], value['medium'])
rule4 = ctrl.Rule(action['up'], value['high'])

value_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])
value_sim = ctrl.ControlSystemSimulation(value_ctrl)
gamma = 0.9
epsilon = 1e-8

V = np.zeros(env.observation_space.n)

while True:
    delta = 0

    for s in range(env.observation_space.n):
        max_value = float('-inf')
        for a in range(env.action_space.n):
            value_sim.input['action'] = a
            value_sim.compute()

            q_value = env.P[s][a]
            expected_value = 0

            for prob, next_state, reward, done in q_value:
                expected_value += prob * (reward + gamma * V[next_state])

            if expected_value > max_value:
                max_value = expected_value

        delta = max(delta, abs(V[s] - max_value))
        V[s] = max_value

    if delta < epsilon:
        break

policy = np.zeros(env.observation_space.n)

for s in range(env.observation_space.n):
    max_value = float('-inf')
    best_action = None

    for a in range(env.action_space.n):
        value_sim.input['action'] = a
        value_sim.compute()

        q_value = env.P[s][a]
        expected_value = 0

        for prob, next_state, reward, done in q_value:
            expected_value += prob * (reward + gamma * V[next_state])

        if expected_value > max_value:
            max_value = expected_value
            best_action = a

    policy[s] = best_action

print(policy)
observation = env.reset()
done = False

while not done:
    env.render()

    if isinstance(observation, tuple):
        observation = observation[0]

    action = policy[observation]
    observation, reward, terminated, truncated, info = env.step(int(action))

    if terminated or truncated:
        done = True
