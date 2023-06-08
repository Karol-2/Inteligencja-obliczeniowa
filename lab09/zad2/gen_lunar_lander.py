import gym
import pygad


def fitness_func(solution, solution_idx):
    env = gym.make('FrozenLake8x8-v1', is_slippery=False)
    env.reset(seed=42)

    total_reward = 0

    for action in solution:
        observation, reward, terminated, truncated, info = env.step(action)
        total_reward += reward

        if terminated or truncated:
            break

    return total_reward


env = gym.make('FrozenLake8x8-v1', is_slippery=False, render_mode="human")
env.reset(seed=42)

num_actions = env.action_space.n
chromosome_length = 50
gene_space = [0, 1, 2, 3]

num_generations = 200
num_parents_mating = 4
sol_per_pop = 8
num_genes = chromosome_length
parent_selection_type = "sss"
keep_parents = num_parents_mating
crossover_type = "single_point"
mutation_type = "random"
mutation_percent_genes = 10

ga_instance = pygad.GA(
    gene_space=gene_space,
    num_generations=num_generations,
    num_parents_mating=num_parents_mating,
    fitness_func=fitness_func,
    sol_per_pop=sol_per_pop,
    num_genes= num_genes,
    parent_selection_type=parent_selection_type,
    keep_parents=keep_parents,
    crossover_type=crossover_type,
    mutation_type=mutation_type,
    mutation_percent_genes=mutation_percent_genes,
)

ga_instance.run()
#ga_instance.plot_fitness()
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Najlepsze rozwiązanie: ", solution)
print("Fitness najlepszego rozwiązania: ", solution_fitness)

for action in solution:
    action = int(action)
    env.render()
    observation, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        break

'''
Chromosomy:
Chromosom to tablica liczb z przedziału 0 do 3
Każda liczba odpowiada jednemu możliwemu działaniu agenta w środowisku FrozenLake8x8
0 - w lewo, 1 - w prawo, 2 - w górę, 3 - w dół

Funkcja fitness:
Funkcja fitness polega na zasymulowaniu krok po kroku ruchów
Wartością oceniającą jest reward i bazuje ona na danych ze środowiska
0 jeśli trafi na dziurę, 0 jeśli nie dojdzie do końca, 1 jeśli dojdzie do końca
'''