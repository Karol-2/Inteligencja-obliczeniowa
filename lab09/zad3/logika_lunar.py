import gym
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np
import matplotlib.pyplot as plt

# E)
position = ctrl.Antecedent(np.arange(-1.2, 1.21, 0.01), 'position')
velocity = ctrl.Antecedent(np.arange(-0.07, 0.071, 0.001), 'velocity')
angle = ctrl.Antecedent(np.arange(-np.pi, np.pi + 0.01, 0.01), 'angle')
angular_velocity = ctrl.Antecedent(np.arange(-np.pi, np.pi + 0.01, 0.01), 'angular_velocity')

action = ctrl.Consequent(np.arange(0, 4, 1), 'action')




position['negative'] = fuzz.trimf(position.universe, [-1.2, -1.2, 0])
position['zero'] = fuzz.trimf(position.universe, [-1.2, 0, 1.2])
position['positive'] = fuzz.trimf(position.universe, [0, 1.2, 1.2])

velocity['negative'] = fuzz.trimf(velocity.universe, [-0.07, -0.07, 0])
velocity['zero'] = fuzz.trimf(velocity.universe, [-0.07, 0, 0.07])
velocity['positive'] = fuzz.trimf(velocity.universe, [0, 0.07, 0.07])

angle['negative'] = fuzz.trimf(angle.universe, [-np.pi, -np.pi, 0])
angle['zero'] = fuzz.trimf(angle.universe, [-np.pi, 0, np.pi])
angle['positive'] = fuzz.trimf(angle.universe, [0, np.pi, np.pi])

angular_velocity['negative'] = fuzz.trimf(angular_velocity.universe, [-np.pi, -np.pi, 0])
angular_velocity['zero'] = fuzz.trimf(angular_velocity.universe, [-np.pi, 0, np.pi])
angular_velocity['positive'] = fuzz.trimf(angular_velocity.universe, [0, np.pi, np.pi])

action['do_nothing'] = fuzz.trimf(action.universe, [0, 0, 0])
action['fire_left'] = fuzz.trimf(action.universe, [0, 0, 1])
action['fire_main'] = fuzz.trimf(action.universe, [1, 2, 3])
action['fire_right'] = fuzz.trimf(action.universe, [2, 3, 3])

# F)
rules = [
    ctrl.Rule(position['negative'] | velocity['negative'], action['fire_left']),
    ctrl.Rule(angle['positive'] | angular_velocity['positive'], action['fire_right']),
    ctrl.Rule(position['zero'] | velocity['zero'], action['do_nothing']),
    ctrl.Rule(position['positive'] | velocity['positive'], action['fire_main'])
]

controller = ctrl.ControlSystem(rules)
simulation = ctrl.ControlSystemSimulation(controller)
env = gym.make("LunarLanderContinuous-v2",render_mode="human")
state = env.reset()

done = False
while not done:
    env.render()

    simulation.input['position'] = state[0][0]
    simulation.input['velocity'] = state[0][1]
    simulation.input['angle'] = state[0][2]
    simulation.input['angular_velocity'] = state[0][3]

    simulation.compute()
    ac = simulation.output
    action_value = np.argmax(ac['action'])
    ac_val=(list(action_value))

    state, reward, terminated,trunctuated, info = env.step(ac_val)
    if terminated or trunctuated:
        break

# position.view()
# velocity.view()
# angle.view()
# angular_velocity.view()
# action.view()
# plt.show()