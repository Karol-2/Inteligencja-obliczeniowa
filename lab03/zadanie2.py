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
gene_space = [0, 1, 2, 3]
'''
Kierunki ruchu: 
0 - lewo
1 - góra
2 - prawo
3 - dół
'''


def odleglosc(stop, exit):
    return abs(stop[0] - exit[0]) + abs(stop[1] - exit[1])


def fitness_func(solution, solution_idx):
    position = start_coord
    odwiedzone_pola = [position]
    karne_punkty = 0
    dobre_punkty = 0
    cofanie_kara = 2
    sciana_kara = 1

    for ruch in solution:
        if ruch == 0:  # lewo
            kolejne_pole = labirynt[position[1]][position[0] - 1]
            if kolejne_pole == "-":  # sprawdzenie czy nowe pole to nie ściana
                position = [position[0] - 1, position[1]]  # jeśli nie ściana to wchodzimy
                if position not in odwiedzone_pola:  # sprawdzenie czy już tu nie byliśmy wczesniej
                    odwiedzone_pola.append(position)  # jeśli nowe pole dodajemy pozytywne pkt
                    dobre_punkty += 5
                else:
                    karne_punkty += cofanie_kara  # kara za chodzenie po poprzednich polach

            else:  # kara jeśli chce uderzyć w ścianę
                karne_punkty += sciana_kara

        elif ruch == 1:  # gora
            kolejne_pole = labirynt[position[1] - 1][position[0]]
            if kolejne_pole == "-":
                position = [position[0], position[1] - 1]
                if position not in odwiedzone_pola:
                    odwiedzone_pola.append(position)
                    dobre_punkty += 5
                else:
                    karne_punkty += cofanie_kara  # kara za cofanie się
            else:
                karne_punkty += sciana_kara

        elif ruch == 2:  # prawo
            kolejne_pole = labirynt[position[1]][position[0] + 1]

            if kolejne_pole == "-":
                position = [position[0] + 1, position[1]]
                if position not in odwiedzone_pola:
                    odwiedzone_pola.append(position)
                    dobre_punkty += 5
                else:
                    karne_punkty += cofanie_kara  # kara za cofanie się

            else:
                karne_punkty += sciana_kara

        elif ruch == 3:  # dol
            kolejne_pole = labirynt[position[1] + 1][position[0]]
            if kolejne_pole == "-":
                position = [position[0], position[1] + 1]
                if position not in odwiedzone_pola:
                    odwiedzone_pola.append(position)
                    dobre_punkty += 5
                else:
                    karne_punkty += cofanie_kara  # kara za cofanie się
            else:
                karne_punkty += sciana_kara

    return -odleglosc(position, exit_coord) - karne_punkty


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


def rysowanie(solution):
    position = start_coord
    odwiedzone_pola = [position]
    cofniecia = 0
    uderzenia = 0

    for ruch in solution:
        if ruch == 0:  # lewo
            kolejne_pole = labirynt[position[1]][position[0] - 1]
            if kolejne_pole == "-":
                position = [position[0] - 1, position[1]]
                if position not in odwiedzone_pola:
                    odwiedzone_pola.append(position)
                else:
                    cofniecia += 1
            else:
                uderzenia += 1

        elif ruch == 1:  # gora
            kolejne_pole = labirynt[position[1] - 1][position[0]]
            if kolejne_pole == "-":
                position = [position[0], position[1] - 1]
                if position not in odwiedzone_pola:
                    odwiedzone_pola.append(position)
                else:
                    cofniecia += 1
            else:
                uderzenia += 1

        elif ruch == 2:  # prawo
            kolejne_pole = labirynt[position[1]][position[0] + 1]

            if kolejne_pole == "-":
                position = [position[0] + 1, position[1]]
                if position not in odwiedzone_pola:
                    odwiedzone_pola.append(position)
                else:
                    cofniecia += 1
            else:
                uderzenia += 1

        elif ruch == 3:  # dol
            kolejne_pole = labirynt[position[1] + 1][position[0]]
            if kolejne_pole == "-":
                position = [position[0], position[1] + 1]
                if position not in odwiedzone_pola:
                    odwiedzone_pola.append(position)
                else:
                    cofniecia += 1
            else:
                uderzenia += 1
        if exit_coord in odwiedzone_pola:
            print(f"ZNALEZIONO WYJSCIE!!, w {len(odwiedzone_pola)-1} krokach")
            break
    print(odwiedzone_pola)
    print("uderzenia w ścianę: ", uderzenia)
    print("cofnięcia: ", cofniecia)


rysowanie(solution)
ga_instance.plot_fitness()

'''
Parameters of the best solution: [2. 2. 3. 3. 0. 0. 3. 3. 2. 3. 2. 3. 2. 1. 2. 1. 2. 1. 2. 3. 3. 2. 2. 3.
 2. 1. 3. 0. 3. 3.]
Fitness value of the best solution  = -2
[[1, 1], [2, 1], [3, 1], [3, 2], [3, 3], [2, 3], [1, 3], [1, 4], [1, 5], [2, 5], [2, 6], [3, 6], [3, 7], [4, 7], [4, 6], [5, 6], [5, 5], [6, 5], [6, 4], [7, 4], [7, 5], [7, 6], [8, 6], [9, 6], [9, 7], [10, 7], [10, 8], [10, 9], [10, 10]]

Parameters of the best solution: [1. 1. 2. 2. 3. 2. 2. 1. 2. 2. 3. 3. 3. 0. 0. 3. 3. 2. 3. 3. 3. 0. 3. 3.
 2. 2. 2. 3. 2. 3.]
Fitness value of the best solution  = -6


'''
