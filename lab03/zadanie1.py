import math
import random

import pygad


# definiujemy parametry chromosomu
# geny to liczby: 0 do 1

def losuj():
    return random.uniform(0, 1)


gene_space = [losuj(), losuj(), losuj(), losuj(), losuj(), losuj()]


def endurance(x, y, z, u, v, w):
    return math.exp(-2 * (y - math.sin(x)) ** 2) + math.sin(z * u) + math.cos(v * w)


# definiujemy funkcję fitness
def fitness_func(solution, solution_idx):
    fit = endurance(solution[0], solution[1], solution[2], solution[3], solution[4], solution[5])
    return fit


fitness_function = fitness_func

# ile chromsomów w populacji
# ile genow ma chromosom
sol_per_pop = 10
num_genes = 6

# ile wylaniamy rodzicow do "rozmanazania" (okolo 50% populacji)
# ile pokolen
# ilu rodzicow zachowac (kilka procent)
num_parents_mating = 5
num_generations = 100
keep_parents = 4

# jaki typ selekcji rodzicow?
# sss = steady, rws=roulette, rank = rankingowa, tournament = turniejowa
parent_selection_type = "sss"

# w il =u punktach robic krzyzowanie?
crossover_type = "single_point"

# mutacja ma dzialac na ilu procent genow?
# trzeba pamietac ile genow ma chromosom
mutation_type = "random"
mutation_percent_genes = 20


ga_instance = pygad.GA(gene_space=gene_space,
                       num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes)

ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Best solution: {}".format(solution))
print("Best fitness: {}".format(solution_fitness))

ga_instance.plot_fitness()
# Best solution: [0.99965839 0.82935113 0.99965839 0.99965839 0.14897972 0.14897972]
# Best fitness: 2.840570554400673
