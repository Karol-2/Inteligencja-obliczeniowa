import skfuzzy as fuzz
from matplotlib import pyplot as plt
from skfuzzy import control as ctrl
import gym
import numpy as np

# Prędkość lądownika
velocity = ctrl.Antecedent(np.arange(-1, 1, 0.1), 'velocity')
velocity['negative'] = fuzz.trimf(velocity.universe, [-1, -1, 0])
velocity['zero'] = fuzz.trimf(velocity.universe, [-0.1, 0, 0.1])
velocity['positive'] = fuzz.trimf(velocity.universe, [0, 1, 1])

# Kąt lądownika
angle = ctrl.Antecedent(np.arange(-1, 1, 0.1), 'angle')
angle['negative'] = fuzz.trimf(angle.universe, [-1, -1, 0])
angle['zero'] = fuzz.trimf(angle.universe, [-0.1, 0, 0.1])
angle['positive'] = fuzz.trimf(angle.universe, [0, 1, 1])

# Przyspieszenie silnika
engine_power = ctrl.Consequent(np.arange(-1, 1, 0.1), 'engine_power')
engine_power['low'] = fuzz.trimf(engine_power.universe, [-1, -1, -0.5])
engine_power['medium'] = fuzz.trimf(engine_power.universe, [-0.7, 0, 0.7])
engine_power['high'] = fuzz.trimf(engine_power.universe, [0.5, 1, 1])

# velocity.view()
# plt.show()
# angle.view()
# plt.show()
# engine_power.view()
# plt.show()

rule1 = ctrl.Rule(velocity['negative'] & angle['negative'], engine_power['high'])
rule2 = ctrl.Rule(velocity['negative'] & angle['zero'], engine_power['high'])
rule3 = ctrl.Rule(velocity['negative'] & angle['positive'], engine_power['medium'])
rule4 = ctrl.Rule(velocity['zero'] & angle['negative'], engine_power['medium'])
rule5 = ctrl.Rule(velocity['zero'] & angle['zero'], engine_power['low'])
rule6 = ctrl.Rule(velocity['zero'] & angle['positive'], engine_power['medium'])
rule7 = ctrl.Rule(velocity['positive'] & angle['negative'], engine_power['low'])
rule8 = ctrl.Rule(velocity['positive'] & angle['zero'], engine_power['low'])
rule9 = ctrl.Rule(velocity['positive'] & angle['positive'], engine_power['low'])

rules = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])

engine = ctrl.ControlSystemSimulation(rules)
env = gym.make('LunarLanderContinuous-v2')

observation = env.reset()
done = False

while not done:
    env.render()
    observation = observation[0]
    # Oblicz wejścia dla kontrolera rozmytego
    velocity_value = observation[1]
    angle_value = observation[4]

    # Wylicz sterowanie z wykorzystaniem kontrolera rozmytego
    engine.input['velocity'] = velocity_value
    engine.input['angle'] = angle_value
    engine.compute()

    engine_power_value = engine.output['engine_power']

    # Podjęcie akcji na podstawie sterowania
    action = np.array([engine_power_value])
    observation, reward, done, info = env.step(action)

env.close()
