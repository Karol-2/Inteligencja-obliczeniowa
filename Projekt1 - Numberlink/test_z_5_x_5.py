import numpy as np
import pygad

from functools import reduce


def zapisz_indeksy(plansza):
    indeksy = {}
    for i in range(len(plansza)):
        for j in range(len(plansza[i])):
            if plansza[i][j] != '-':
                indeksy[(i,j)] = int(plansza[i][j])
    return indeksy


plansza = [
    ["-","-","-","-","-"],
    ["-","1","-","-","-"],
    ["-","-","2","-","-"],
    ["-","-","1","-","-"],
    ["0","2","0","-","-"],

]

wymagane_pola = zapisz_indeksy(plansza)

print("wymagane pola",wymagane_pola)
rozmiar = 5 * 5


def odleglosc(stop,exit):
    return abs(stop[0] - exit[0]) + abs(stop[1] - exit[1])


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

def has_valid_neighbors(matrix, i, j):
    """
    Sprawdza, czy w macierzy 'matrix' w pozycji (i,j) znajduje się liczba 0, 1 lub 2, która nie ma żadnego sąsiada o tej samej wartości.
    """
    options=[0,1,2]
    value = matrix[i][j]
    neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    connections = 0
    for neighbor in neighbors:
        if neighbor[0] >= 0 and neighbor[0] < len(matrix) and neighbor[1] >= 0 and neighbor[1] < len(matrix[0]) and matrix[neighbor[0]][neighbor[1]] == value:
            return False

    return True
def fitness_func(solution,solution_idx):
    punkty = 0
    suma_dlugosci = 0
    kara_dwa_polaczenia = 0
    kara = 0
    macierz = np.array(solution).reshape((5,5))
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

        # #sprawdzanie czy pole startowe ma sąsiada
        if sprawdz_sasiedztwo(macierz,pos_x,pos_y,szukana):
            punkty += 5
        else:
            kara += 10
        #  Sprawdza, czy w macierzy nie znajdują się żadne samotne punkty bez żadnego połączenia
        for i in range(len(macierz)):
            for j in range(len(macierz[0])):
                if macierz[i][j] not in [0,1,2] and not has_valid_neighbors(macierz,i,j):
                    kara += 200

        # algorytm DFS
        visited = set()  # zbiór odwiedzonych wierzchołków
        stack = [start_pozycja]  # stos wierzchołków do odwiedzenia
        while stack:
            current = stack.pop()  # pobierz ostatni wierzchołek ze stosu
            if current == stop_pozycja:  # jeśli znaleziono cel
                punkty += 10
                break
            visited.add(current)  # dodaj do odwiedzonych
            suma_dlugosci += 1
            # znajdź sąsiadujące wierzchołki, które nie są odwiedzone
            neighbors = [(current[0] - 1,current[1]),(current[0] + 1,current[1]),
                         (current[0],current[1] - 1),(current[0],current[1] + 1)]
            for neighbor in neighbors:
                if neighbor[0] < 0 or neighbor[0] >= len(macierz) \
                        or neighbor[1] < 0 or neighbor[1] >= len(macierz[0]):
                    # kara += 20
                    continue  # pomijaj wierzchołki poza granicami macierzy
                if macierz[neighbor[0]][neighbor[1]] == macierz[start_pozycja[0]][start_pozycja[1]] \
                        and neighbor not in visited:
                    stack.append(neighbor)  # dodaj do stosu do odwiedzenia

    return -(-punkty - suma_dlugosci + (brak_obowiazkowych_pol * 1000) + kara + kara_dwa_polaczenia)


'''
dla każdego elementu znalazła ścieżkę,  a następnie sprawdzała czy gdzies indziej w macierzy też występują niepołączone fragmenty - jeśli tak to daje karę,

NIE MOGĄ SIĘ PRZECINAĆ I WSZYSTKO MUSI BYĆ ZAPEŁNIONE
kara większa za przecięcia niż za nie wypełnienie
'''

gene_space = [0,1,2]
fitness_function = fitness_func

sol_per_pop = 81  # ile chromsomów w populacji
num_genes = rozmiar  # ile genow ma chromosom

num_parents_mating = 40  # ile wylaniamy rodzicow do "rozmanazania" (okolo 50% populacji)
num_generations = 5000  # ile pokolen
keep_parents = 30  # ilu rodzicow zachowac (kilka procent)

parent_selection_type = "sss"
crossover_type = "single_point"

mutation_type = "random"  # mutacja ma dzialac na ilu procent genow?
mutation_percent_genes = 15  # trzeba pamietac ile genow ma chromosom

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
print("Parameters of the best solution:\n {solution}".format(solution=np.array(solution).reshape((5,5))))
print("Fitness = {solution_fitness}".format(solution_fitness=solution_fitness))
ga_instance.plot_fitness()

idealne = [
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,2,2,1,0],
    [0,2,1,1,0],
    [0,2,0,0,0]
]


def compare_matrices(matrix1,matrix2):
    n = len(matrix1)
    m = len(matrix1[0])
    same_count = 0

    for i in range(n):
        for j in range(m):
            if matrix1[i][j] == matrix2[i][j]:
                same_count += 1

    return str((same_count / (n * m)) * 100) + "% idealnego rozwiązania"


print(compare_matrices(idealne,solution.reshape((5,5))))
