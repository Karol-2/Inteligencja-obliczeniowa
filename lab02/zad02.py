import time

import numpy
import pygad

przedmioty = ["zegar", "obraz-pejzaż", "obraz-portret", "radio", "laptop", "lampka nocna", "srebrne sztućce",
              "porcelana", "figurka z brązu", "skórzana torebka", "odkurzacz"]
wartosci = [100, 300, 200, 40, 500, 70, 100, 250, 300, 280, 300]
wagi = [7, 7, 6, 2, 5, 6, 1, 3, 10, 3, 15]
udzwig = 25

# definiujemy parametry chromosomu
# geny to liczby: 0 lub 1
gene_space = [0, 1]


# definiujemy funkcję fitness
def fitness_func(solution, solution_idx):
    waga = 0
    wartosc = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            waga += wagi[i]
            wartosc += wartosci[i]
    if waga > udzwig:
        wartosc = 0
    return wartosc


fitness_function = fitness_func

# ile chromsomów w populacji
# ile genow ma chromosom
sol_per_pop = 100
num_genes = len(wartosci)

# ile wylaniamy rodzicow do "rozmanazania" (okolo 50% populacji)
# ile pokolen
# ilu rodzicow zachowac (kilka procent)
num_parents_mating = 5
num_generations = 1000
keep_parents = 2

# jaki typ selekcji rodzicow?
# sss = steady, rws=roulette, rank = rankingowa, tournament = turniejowa
parent_selection_type = "sss"

# w il =u punktach robic krzyzowanie?
crossover_type = "single_point"

# mutacja ma dzialac na ilu procent genow?
# trzeba pamietac ile genow ma chromosom
mutation_type = "random"
mutation_percent_genes = 10

# inicjacja algorytmu z powyzszymi parametrami wpisanymi w atrybuty
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
                       mutation_percent_genes=mutation_percent_genes,
                       stop_criteria=["reach_1600.0"])  # zadanie 2 a

start = time.time()
# uruchomienie algorytmu
ga_instance.run()

end = time.time()

# podsumowanie: najlepsze znalezione rozwiazanie (chromosom+ocena)
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

# tutaj dodatkowo wyswietlamy sume wskazana przez jedynki
prediction = numpy.sum(wagi * solution)
print("Predicted output based on the best solution : {prediction}".format(prediction=prediction))

# wyswietlenie wykresu: jak zmieniala sie ocena na przestrzeni pokolen
# ga_instance.plot_fitness()

print("=============================================================")
suma_wartosci = 0
suma_wag = 0
for i in range(len(solution)):
    if solution[i] == 1:
        print(przedmioty[i], "- waga", wagi[i], ", wartość", wartosci[i])
        suma_wartosci += wartosci[i]
        suma_wag += wagi[i]

print("=============================================================")
print("Łączna wartość: ", suma_wartosci)
print("Łączna waga: ", suma_wag)

print("Liczba pokoleń: ", solution_idx + 1)  # zadanie 2 b
print("Obliczono w czasie: ", end - start)  # zadanie 2 c

'''
zadanie 2 d
1 - 0.005000114440917969
2 - 0.007998466491699219
3 - 0.018010854721069336
4 - 0.012999534606933594
5 - 0.01248788833618164
6 - 0.010999917984008789
7 - 0.010978221893310547
8 - 0.019999980926513672
9 - 0.011996269226074219
10 - 0.004517316818237305

średnia = 0.011599976434893501
'''
