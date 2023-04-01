import numpy as np
import pygad
import csv
from functools import reduce



def zapisz_indeksy(plansza):
    """
    Funkcja analizuje plansze iu w formie słownika zapisuje wymagane pola - ich koordynaty i wartość
    """
    indeksy = {}
    for i in range(len(plansza)):
        for j in range(len(plansza[i])):
            if plansza[i][j] != '-':
                indeksy[(i,j)] = int(plansza[i][j])
    return indeksy


def sprawdz_sasiedztwo(macierz,pos_x,pos_y,wartosc):
    """
    Funkcja sprawdza czy dla pola o podanych koordynatach jest inne z tą samą wartoscią
    """
    if pos_x > 0 and macierz[pos_x - 1][pos_y] == wartosc:
        return True
    if pos_x < len(macierz) - 1 and macierz[pos_x + 1][pos_y] == wartosc:
        return True
    if pos_y > 0 and macierz[pos_x][pos_y - 1] == wartosc:
        return True
    if pos_y < len(macierz[0]) - 1 and macierz[pos_x][pos_y + 1] == wartosc:
        return True
    return False


def czy_ma_dwoch_sasiadow(macierz,x,y):
    """
    Funkcja sprawdza czy dla pola o podanych koordynatach jest TYLKo 2 sąsiadów, jeśli jest inaczej zwraca False
    """
    wartosc = macierz[y][x]
    sasiedzi = [(x - 1,y),(x + 1,y),(x,y - 1),(x,y + 1)]
    ilosc = 0
    for sasiedzi in sasiedzi:
        if 0 <= sasiedzi[0] < len(macierz) and 0 <= sasiedzi[1] < len(macierz[0]) and macierz[sasiedzi[0]][
            sasiedzi[1]] == wartosc:
            ilosc += 1

    return ilosc == 2


def punkt_nie_solo(macierz,i,j):
    """
    Sprawdza, czy w macierzy 'matrix' w pozycji (i,j) znajduje się liczba 0, 1 lub 2, która nie ma żadnego sąsiada o tej samej wartości.
    czyli szuka solowych punktów
    """
    wartosc = macierz[i][j]
    sasiedzi = [(i - 1,j),(i + 1,j),(i,j - 1),(i,j + 1)]

    for sasaid in sasiedzi:
        if 0 <= sasaid[0] < len(macierz) and sasaid[1] >= 0 and sasaid[1] < len(macierz[0]) and macierz[sasaid[0]][
            sasaid[1]] == wartosc:
            return True

    return False

def porownaj_macierze(macierzA,macierzB):
    """
    Funkcja która porównuje procentowe podobieństwo naszego rozwiązania i idealnego
    """
    n = len(macierzA)
    m = len(macierzA[0])
    te_same = 0

    for i in range(n):
        for j in range(m):
            if macierzA[i][j] == macierzB[i][j]:
                te_same += 1

    return str((te_same / (n * m)) * 100) + "% idealnego rozwiązania"
def wiecej_niz_2(matrix,wymagane_pole):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (i, j) in wymagane_pole:
                continue
            value = matrix[i][j]
            count = 0
            for x in range(max(0, i-1), min(len(matrix), i+2)):
                for y in range(max(0, j-1), min(len(matrix[i]), j+2)):
                    if (x, y) in wymagane_pole:
                        continue
                    if x == i and y == j:
                        continue
                    if matrix[x][y] == value:
                        count += 1
            if count != 2:
               # print("NIE MA")
                return True
    return False
def fitness_func(solution,solution_idx):
    punkty = 0
    suma_dlugosci = 0
    kara = 0
    macierz = np.array(solution).reshape((len(plansza),len(plansza)))  # zmieniamy tablicę liczb w macierz
    brak_obowiazkowych_pol = 0

    for wiersz,kolumna in wymagane_pola.keys():  # na początku sprawdzamy czy wymagane wartości podane na planszy istnieją
        if macierz[wiersz][kolumna] != wymagane_pola[(wiersz,kolumna)]:
            brak_obowiazkowych_pol += 1000
            '''
             ilość brakujących pól wlicza się do ostatecznej wartości fitness
             kara jest podana w tysiącach, bo nie możemy pozwolić aby nie było tych wartości
             '''

     # Sprawdzamy, czy w macierzy nie znajdują się żadne samotne punkty bez żadnego połączenia
    for i in range(len(macierz)):
        for j in range(len(macierz[0])):  # oprócz miejsc start/stop
            if macierz[i][j] not in wymagane_pola and not punkt_nie_solo(macierz,i,j):
                kara += 200

    if not wiecej_niz_2(macierz,wymagane_pola):
        punkty += 100
    else:
        kara +=200

    for liczba in liczby_do_polaczenia:  # interujemy po każdej liczbie
        key_list = list(wymagane_pola.keys())
        val_list = list(wymagane_pola.values())
        pos = val_list.index(liczba)

        start_pozycja = 0
        stop_pozycja = 0

        for key,value in wymagane_pola.items():  # szukamy w wymaganych polach koordynatów miejsa startu dla danej liczby
            if value == 0:
                start_pozycja = key
                break
        count_zero = 0

        for key,value in wymagane_pola.items():  # szukamy w wymaganych polach koordynatów miejsa stopu dla danej liczby
            if value == 0:
                count_zero += 1
                if count_zero == 2:
                    stop_pozycja = key
                    break

        pos_x = key_list[pos][0]
        pos_y = key_list[pos][1]

        if (pos_x,pos_y) not in wymagane_pola:  # pomijamy pola start/stop
            if czy_ma_dwoch_sasiadow(macierz,pos_x,
                                     pos_y):  # sprawdzamy czy dla danych koordynatów jest dokładnie 2 sąsaidów
                punkty += 50
            else:
                kara += 50

        # #sprawdzanie czy pole startowe ma sąsiada
        if sprawdz_sasiedztwo(macierz,pos_x,pos_y,liczba):
            punkty += 50
        else:
            kara += 70

        # algorytm DFS, do przeszukania macierzy według aktualnej liczby

        visited = set()  # zbiór odwiedzonych wierzchołków
        stack = [start_pozycja]  # stos wierzchołków do odwiedzenia
        while stack:
            current = stack.pop()  # pobierz ostatni wierzchołek ze stosu
            if current == stop_pozycja:  # jeśli znaleziono cel
                punkty += 50
                break
            visited.add(current)  # dodaj do odwiedzonych
            suma_dlugosci += 1  # zachęcanie szukania kolejnych wierzchołków

            # znajdź sąsiadujące wierzchołki, które nie są odwiedzone
            neighbors = [(current[0] - 1,current[1]),(current[0] + 1,current[1]),
                         (current[0],current[1] - 1),(current[0],current[1] + 1)]
            for neighbor in neighbors:
                if neighbor[0] < 0 or neighbor[0] >= len(macierz) or neighbor[1] < 0 or neighbor[1] >= len(macierz[0]):
                    continue  # pomijaj wierzchołki poza granicami macierzy
                if macierz[neighbor[0]][neighbor[1]] == macierz[start_pozycja[0]][start_pozycja[1]] \
                        and neighbor not in visited:
                    stack.append(neighbor)  # dodaj do stosu do odwiedzenia

    return punkty + suma_dlugosci - brak_obowiazkowych_pol - kara


plansza = [
    ["-","-","-","-","-"],
    ["-","1","-","-","-"],
    ["-","-","2","-","-"],
    ["-","-","1","-","-"],
    ["0","2","0","-","-"],
]

idealne = [
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,2,2,1,0],
    [0,2,1,1,0],
    [0,2,0,0,0]
]

wymagane_pola = zapisz_indeksy(plansza)
rozmiar = len(plansza) * len(plansza)
liczby_do_polaczenia = reduce(lambda re,x: re + [x] if x not in re else re,wymagane_pola.values(),[])

gene_space = liczby_do_polaczenia
fitness_function = fitness_func

sol_per_pop = 80  # ilość chromsomów w populacji
num_genes = rozmiar  # ilość genow w chromosomie

num_parents_mating = 40  # (okolo 50% populacji)
num_generations = 4000  # ilosc pokolen
keep_parents = 5  # ilosc rodzicow do zachowania

parent_selection_type = "sss" # typ seleckji
crossover_type = "single_point" #typ łączenia

mutation_type = "random"  # mutacja ma dzialac na ilu procent genow?
mutation_percent_genes = 15  # trzeba pamietac ile genow ma chromosom
for i in range(101):
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
    print(i)
    solution,solution_fitness,solution_idx = ga_instance.best_solution()
    #print("Parameters of the best solution:\n {solution}".format(solution=np.array(solution).reshape((5,5))))
    #print("Fitness = {solution_fitness}".format(solution_fitness=solution_fitness))
    #print(porownaj_macierze(idealne,solution.reshape((len(plansza),len(plansza)))))
    #ga_instance.plot_fitness()
    #print(list(solution))

    with open('plik.csv',mode='a') as plik_csv:
        writer = csv.writer(plik_csv)
        writer.writerow([i, solution,porownaj_macierze(idealne,solution.reshape((len(plansza),len(plansza))))])
