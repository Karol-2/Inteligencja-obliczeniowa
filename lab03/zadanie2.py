import time

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

    cofanie_kara = 2
    sciana_kara = 1

    for ruch in solution:
        if ruch == 0:  # lewo
            kolejne_pole = labirynt[position[1]][position[0] - 1]
            if kolejne_pole == "-":  # sprawdzenie czy nowe pole to nie ściana
                position = [position[0] - 1, position[1]]  # jeśli nie ściana to wchodzimy
                if position not in odwiedzone_pola:  # sprawdzenie czy już tu nie byliśmy wczesniej
                    odwiedzone_pola.append(position)  # jeśli nowe pole dodajemy pozytywne pkt

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

                else:
                    karne_punkty += cofanie_kara
            else:
                karne_punkty += sciana_kara

        elif ruch == 2:  # prawo
            kolejne_pole = labirynt[position[1]][position[0] + 1]

            if kolejne_pole == "-":
                position = [position[0] + 1, position[1]]
                if position not in odwiedzone_pola:
                    odwiedzone_pola.append(position)

                else:
                    karne_punkty += cofanie_kara

            else:
                karne_punkty += sciana_kara

        elif ruch == 3:  # dol
            kolejne_pole = labirynt[position[1] + 1][position[0]]
            if kolejne_pole == "-":
                position = [position[0], position[1] + 1]
                if position not in odwiedzone_pola:
                    odwiedzone_pola.append(position)

                else:
                    karne_punkty += cofanie_kara
            else:
                karne_punkty += sciana_kara

        if position == exit_coord:
            return -odleglosc(position, exit_coord) - karne_punkty

    return -odleglosc(position, exit_coord) - karne_punkty


fitness_function = fitness_func

sol_per_pop = 144  # ile chromsomów w populacji
num_genes = max_kroki  # ile genow ma chromosom

num_parents_mating = 25  # ile wylaniamy rodzicow do "rozmanazania" (okolo 50% populacji)
num_generations = 200  # ile pokolen
keep_parents = 2  # ilu rodzicow zachowac (kilka procent)

parent_selection_type = "sss"
crossover_type = "single_point"

mutation_type = "random"  # mutacja ma dzialac na ilu procent genow?
mutation_percent_genes = 4  # trzeba pamietac ile genow ma chromosom

start = time.time()
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
end = time.time()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution: {solution}".format(solution=solution))
print("Fitness = {solution_fitness}".format(solution_fitness=solution_fitness))
print("Obliczono w czasie: ", end - start, "s.")


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
            print(f"ZNALEZIONO WYJSCIE!!\nw {len(odwiedzone_pola)-1} krokach")
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

'''

'''
Index - Czas
1 - 2.4201695919036865
2 - 2.468787670135498
3 - 2.208211898803711
4 - 2.163158416748047
5 - 2.282962322235107
6 - 2.082779884338379
7 - 2.1157240867614746
8 - 2.5850048065185547
9 - 2.088573694229126
10 - 2.0761518478393555

ŚREDNI CZAS = 2.2676 s.

'''
