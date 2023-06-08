import gym
import pygad
import numpy as np


# Funkcja fitness
def fitness_func(solution, solution_idx):
    env = gym.make('FrozenLake-v1',is_slippery=False)
    env.reset(seed=42)

    total_reward = 0

    for action in solution:
        _, reward, done, _ = env.step(action)
        total_reward += reward

        if done:
            break

    return total_reward


# Konfiguracja środowiska FrozenLake
env = gym.make('FrozenLake-v1',is_slippery=False)
num_actions = env.action_space.n

# Długość chromosomów
chromosome_length = 100

# Konfiguracja algorytmu genetycznego
num_generations = 50
num_parents_mating = 4
sol_per_pop = 8
num_genes = chromosome_length
parent_selection_type = "sss"
keep_parents = num_parents_mating
crossover_type = "single_point"
mutation_type = "random"
mutation_percent_genes = 10

# Inicjalizacja populacji początkowej
initial_population = pygad.initial_population(sol_per_pop, num_genes)

# Tworzenie instancji klasy pygad.GA
ga_instance = pygad.GA(
    num_generations=num_generations,
    num_parents_mating=num_parents_mating,
    initial_population=initial_population,
    fitness_func=fitness_func,
    parent_selection_type=parent_selection_type,
    keep_parents=keep_parents,
    crossover_type=crossover_type,
    mutation_type=mutation_type,
    mutation_percent_genes=mutation_percent_genes,
)

# Uruchomienie algorytmu genetycznego
ga_instance.run()

# Pobranie najlepszego rozwiązania
solution, solution_fitness, solution_idx = ga_instance.best_solution()

# Testowanie najlepszego rozwiązania
env.reset(seed=42)
for action in solution:
    env.render()
    _, _, done, _ = env.step(action)
    if done:
        break

# Wyświetlenie wyników
print("Najlepsze rozwiązanie: ", solution)
print("Fitness najlepszego rozwiązania: ", solution_fitness)
