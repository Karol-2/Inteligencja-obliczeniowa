import numpy as np
import pygad
import random

from functools import reduce


# def los():
#     return random.randint(0,6)


# plansza = [
#     [0, los(), los(), los(), los(), los(), los(), los(), 1],
#     [1, los(), los(), los(), los(), los(), los(), los(), los()],
#     [los(), los(), los(), los(), 3, los(), los(), 4, los()],
#     [los(), los(), los(), los(), los(), 2, los(), los(), los()],
#     [los(), los(), los(), los(), los(), 5, los(), los(), los()],
#     [los(), los(), los(), los(), 3, los(), los(), los(), los()],
#     [los(), 0, los(), los(), 4, los(), los(), los(), los()],
#     [los(), los(), los(), los(), 6, los(), los(), 6, los()],
#     [5, los(), los(), los(), 2, los(), los(), los(), los()]
# ]

def zapisz_indeksy(plansza):
    indeksy = {}
    for i in range(len(plansza)):
        for j in range(len(plansza[i])):
            if plansza[i][j] != '-':
                indeksy[(i,j)] = int(plansza[i][j])
    return indeksy


plansza = [
    ["0","-","-","-","-","-","-","-","1"],
    ["1","-","-","-","-","-","-","-","-"],
    ["-","-","-","-","3","-","-","4","-"],
    ["-","-","-","-","-","2","-","-","-"],
    ["-","-","-","-","-","5","-","-","-"],
    ["-","-","-","-","3","-","-","-","-"],
    ["-","0","-","-","4","-","-","-","-"],
    ["-","-","-","-","6","-","-","6","-"],
    ["5","-","-","-","2","-","-","-","-"],
]
wymagane_pola = zapisz_indeksy(plansza)

print("wymagane pola",wymagane_pola)
rozmiar = 9 * 9


def odleglosc(stop,exit):
    return abs(stop[0] - exit[0]) + abs(stop[1] - exit[1])

def find_path(matrix, start, end): # algorytm DFS
    visited = set() # zbiór odwiedzonych wierzchołków
    stack = [start] # stos wierzchołków do odwiedzenia
    while stack:
        current = stack.pop() # pobierz ostatni wierzchołek ze stosu
        if current == end: # jeśli znaleziono cel
            return True
        visited.add(current) # dodaj do odwiedzonych
        # znajdź sąsiadujące wierzchołki, które nie są odwiedzone
        neighbors = [(current[0]-1, current[1]), (current[0]+1, current[1]),
                     (current[0], current[1]-1), (current[0], current[1]+1)]
        for neighbor in neighbors:
            if neighbor[0] < 0 or neighbor[0] >= len(matrix) \
                or neighbor[1] < 0 or neighbor[1] >= len(matrix[0]):
                continue # pomijaj wierzchołki poza granicami macierzy
            if matrix[neighbor[0]][neighbor[1]] == matrix[start[0]][start[1]] \
                and neighbor not in visited:
                stack.append(neighbor) # dodaj do stosu do odwiedzenia
    return False # nie znaleziono połączenia


def sprawdz_sasiedztwo(matrix,pos_x,pos_y,szukana):
    if pos_x > 0 and matrix[pos_x - 1][pos_y] == szukana:
        return True,"L"
    if pos_x < len(matrix) - 1 and matrix[pos_x + 1][pos_y] == szukana:
        return True,"P"
    if pos_y > 0 and matrix[pos_x][pos_y - 1] == szukana:
        return True,"G"
    if pos_y < len(matrix[0]) - 1 and matrix[pos_x][pos_y + 1] == szukana:
        return True,"D"
    return False


def fitness_func(solution,solution_idx):
    punkty = 0
    kara = 0
    macierz = np.array(solution).reshape((9,9))
    brak_obowiazkowych_pol = 0

    for wiersz,kolumna in wymagane_pola.keys():
        if macierz[wiersz][kolumna] != wymagane_pola[(wiersz,kolumna)]:
            brak_obowiazkowych_pol += 1

    unikalne_liczby = reduce(lambda re,x: re + [x] if x not in re else re,wymagane_pola.values(),[])

    for szukana in unikalne_liczby:
        key_list = list(wymagane_pola.keys())
        val_list = list(wymagane_pola.values())
        pos = val_list.index(szukana)
        start_pozycja = 0
        stop_pozycja = 0

        for key,value in wymagane_pola.items():
            if value == 0:
                start_pozycja = key
                break
        count_zero = 0

        for key,value in wymagane_pola.items():
            if value == 0:
                count_zero += 1
                if count_zero == 2:
                    stop_pozycja = key
                    break

        pos_x = key_list[pos][0]
        pos_y = key_list[pos][1]

        if sprawdz_sasiedztwo(macierz,pos_x,pos_y,szukana):
            punkty += 5
        else:
            kara += 10

        visited = set()  # zbiór odwiedzonych wierzchołków
        stack = [start_pozycja]  # stos wierzchołków do odwiedzenia
        while stack:
            current = stack.pop()  # pobierz ostatni wierzchołek ze stosu
            if current == stop_pozycja:  # jeśli znaleziono cel
                punkty +=50
                break
            visited.add(current)  # dodaj do odwiedzonych
            # znajdź sąsiadujące wierzchołki, które nie są odwiedzone
            neighbors = [(current[0] - 1,current[1]),(current[0] + 1,current[1]),
                         (current[0],current[1] - 1),(current[0],current[1] + 1)]
            for neighbor in neighbors:
                if neighbor[0] < 0 or neighbor[0] >= len(macierz) \
                        or neighbor[1] < 0 or neighbor[1] >= len(macierz[0]):
                    continue  # pomijaj wierzchołki poza granicami macierzy
                if macierz[neighbor[0]][neighbor[1]] == macierz[start_pozycja[0]][start_pozycja[1]] \
                        and neighbor not in visited:
                    stack.append(neighbor)  # dodaj do stosu do odwiedzenia
     #   return False  # nie znaleziono połączenia

    return -(-punkty + (brak_obowiazkowych_pol * 1000) + kara)


'''
NIE MOGĄ SIĘ PRZECINAĆ I WSZYSTKO MUSI BYĆ ZAPEŁNIONE
kara większa za przecięcia niż za nie wypełnienie
'''

gene_space = [0,1,2,3,4,5,6]
fitness_function = fitness_func

sol_per_pop = 81  # ile chromsomów w populacji
num_genes = rozmiar  # ile genow ma chromosom

num_parents_mating = 40  # ile wylaniamy rodzicow do "rozmanazania" (okolo 50% populacji)
num_generations = 1000  # ile pokolen
keep_parents = 30  # ilu rodzicow zachowac (kilka procent)

parent_selection_type = "sss"
crossover_type = "single_point"

mutation_type = "random"  # mutacja ma dzialac na ilu procent genow?
mutation_percent_genes = 5  # trzeba pamietac ile genow ma chromosom

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

solution,solution_fitness,solution_idx = ga_instance.best_solution()
print(list(solution))
print("Parameters of the best solution:\n {solution}".format(solution=np.array(solution).reshape((9,9))))
print("Fitness = {solution_fitness}".format(solution_fitness=solution_fitness))
ga_instance.plot_fitness()

idealne = [
    [0,0,1,1,1,1,1,1,1],
    [1,0,1,2,2,2,2,2,2],
    [1,0,1,2,3,3,3,4,1],
    [1,0,1,2,2,2,3,4,2],
    [1,0,1,5,5,5,3,4,1],
    [1,0,1,5,3,3,3,4,1],
    [1,0,1,5,4,4,4,4,1],
    [1,1,1,5,6,6,6,6,2],
    [5,5,5,5,2,2,2,2,2]

]
def compare_matrices(matrix1, matrix2):
    n = len(matrix1)
    m = len(matrix1[0])
    same_count = 0

    for i in range(n):
        for j in range(m):
            if matrix1[i][j] == matrix2[i][j]:
                same_count += 1

    return str((same_count / (n*m)) * 100) + "%"

print(compare_matrices(idealne,solution.reshape((9,9))))
