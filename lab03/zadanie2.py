import pygad

labirynt = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '-', '-', '-', '#', '-', '-', '-', '#', '-', '-', '#'],
    ['#', '#', '#', '-', '-', '-', '#', '-', '#', '#', '-', '#'],
    ['#', '-', '-', '-', '#', '-', '#', '-', '-', '-', '-', '#'],
    ['#', '-', '#', '-', '#', '#', '-', '-', '#', '#', '-', '#'],
    ['#', '-', '-', '#', '#', '-', '-', '-', '#', '-', '-', '#'],
    ['#', '-', '-', '-', '-', '-', '#', '-', '-', '-', '#', '#'],
    ['#', '-', '#', '-', '-', '#', '#', '-', '#', '-', '-', '#'],
    ['#', '-', '#', '#', '#', '-', '-', '-', '#', '#', '-', '#'],
    ['#', '-', '#', '-', '#', '#', '-', '#', '-', '#', '-', '#'],
    ['#', '-', '#', '-', '-', '-', '-', '-', '-', '-', '-', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]

start_coord = [1, 1]
exit_coord = [10, 10]
max_kroki = 30
'''
Kierunki ruchu: 
0 - lewo
1 - góra
2 - prawo
3 - dół
'''

# za cofanie się, odbicie się jest punkt karny

gene_space = [0, 1, 2, 3]


def odleglosc(stop, exit):
    return abs(stop[0] - exit[0]) + abs(stop[1] - exit[1])


def fitness_func(solution, solution_idx):
    position = start_coord
    odwiedzone_pola = [position]
    karne_punkty = 0
    dobre_punkty = 0
    cofanie_kara =10
    sciana_kara= 10

    for ruch in solution:
        if ruch == 0:  # lewo
            if labirynt[position[0] - 1][position[1]] == "-":  # sprawdzenie czy nowe pole to nie ściana
                if [position[0] - 1, position[1]] not in odwiedzone_pola:  # sprawdzenie czy się nie cofamy
                    position = [position[0] - 1, position[1]]
                    odwiedzone_pola.append(position)
                    dobre_punkty +=5
                else:
                    karne_punkty += cofanie_kara  # kara za cofanie się

            else:  # kara jeśli chce uderzyć w ścianę
                karne_punkty += sciana_kara

        elif ruch == 1:  # gora
            if labirynt[position[0]][position[1] - 1] == "-":
                if [position[0], position[1] - 1] not in odwiedzone_pola:
                    position = [position[0], position[1] - 1]
                    odwiedzone_pola.append(position)
                    dobre_punkty +=5
                else:
                    karne_punkty += cofanie_kara  # kara za cofanie się
            else:
                karne_punkty += sciana_kara

        elif ruch == 2:  # prawo
            if labirynt[position[0] + 1][position[1]] == "-":
                if [position[0] + 1, position[1]] not in odwiedzone_pola:
                    position = [position[0] + 1, position[1]]
                    odwiedzone_pola.append(position)
                    dobre_punkty +=5
                else:
                    karne_punkty += cofanie_kara  # kara za cofanie się
            else:
                karne_punkty += sciana_kara

        elif ruch == 3:  # dol
            if labirynt[position[0]][position[1] + 1] == "-":
                if [position[0], position[1] + 1] not in odwiedzone_pola:
                    position = [position[0], position[1] + 1]
                    odwiedzone_pola.append(position)
                    dobre_punkty +=5
                else:
                    karne_punkty += cofanie_kara  # kara za cofanie się
            else:
                karne_punkty += sciana_kara

    return odleglosc(position, exit_coord) - karne_punkty + dobre_punkty


fitness_function = fitness_func

# ile chromsomów w populacji
# ile genow ma chromosom
sol_per_pop = 200
num_genes = max_kroki

# ile wylaniamy rodzicow do "rozmanazania" (okolo 50% populacji)
# ile pokolen
# ilu rodzicow zachowac (kilka procent)
num_parents_mating = 25
num_generations = 200
keep_parents = 2

parent_selection_type = "sss"
crossover_type = "single_point"

# mutacja ma dzialac na ilu procent genow?
# trzeba pamietac ile genow ma chromosom
mutation_type = "random"
mutation_percent_genes = 4

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
print("Parameters of the best solution: {solution}".format(solution=solution))
print("Fitness value of the best solution  = {solution_fitness}".format(solution_fitness=solution_fitness))

ga_instance.plot_fitness()
