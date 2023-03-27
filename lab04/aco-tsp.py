import random
import time

import matplotlib.pyplot as plt
from aco import AntColony

plt.style.use("dark_background")

COORDS = (
    (20, 52),
    (43, 50),
    (20, 84),
    (70, 65),
    (29, 90),
    (87, 83),
    (73, 23),

    (30, 70),
    (15, 120),
    (55, 33),
    (50, 70),
    (5, 5),

    # (18, 18),
    # (55, 60),
    # (19, 89),
    # (18, 11),
    # (20, 23)
)


def random_coord():
    r = random.randint(0, len(COORDS))
    return r


def plot_nodes(w=12, h=8):
    for x, y in COORDS:
        plt.plot(x, y, "g.", markersize=15)
    plt.axis("off")
    fig = plt.gcf()
    fig.set_size_inches([w, h])


def plot_all_edges():
    paths = ((a, b) for a in COORDS for b in COORDS)

    for a, b in paths:
        plt.plot((a[0], b[0]), (a[1], b[1]))


plot_nodes()
start = time.time()
colony = AntColony(COORDS, ant_count=300, alpha=0.5, beta=1.2,
                   pheromone_evaporation_rate=0.40, pheromone_constant=1000.0,
                   iterations=300)

optimal_nodes = colony.get_path()
end = time.time()
for i in range(len(optimal_nodes) - 1):
    plt.plot(
        (optimal_nodes[i][0], optimal_nodes[i + 1][0]),
        (optimal_nodes[i][1], optimal_nodes[i + 1][1]),
    )

plt.show()
print("Obliczono w czasie: ", end - start, "s.")
'''
7 wierzchołków - długość drogi 240.655 - 28s
12 wierzchołków - długość drogi 448.086 - 40s
17 wierzchołków - długość drogi 465.487 - 72s

ant_count - W przypadku większej liczby mrówek algorytm może działać wolniej, ponieważ trzeba śledzić większą liczbę 
mrówek. Zwiększenie liczby mrówek może zwiększyć czas potrzebny na znalezienie rozwiązania, ale może również poprawić 
jakość rozwiązania.

alpha - Wysoka wartość alfa oznacza, że mrówka bardziej koncentruje się na śladach feromonów, co może prowadzić do 
bardziej intensywnego przeszukiwania wokół aktualnie najlepszego rozwiązania. Z drugiej strony, niska wartość alfa 
oznacza, że mrówka będzie bardziej skłonna do losowego przeszukiwania przestrzeni rozwiązań, co może prowadzić do 
znalezienia lepszych wyników w dłuższej perspektywie.

beta -  Wysoka wartość beta oznacza, że mrówka bardziej skupia się na informacjach o jakości rozwiązania, 
które pochodzą z samego problemu. Zwiększenie wartości beta oznacza, że mrówka będzie bardziej skłonna do 
przeszukiwania obszarów przestrzeni rozwiązań, które wydają się być obiecujące z punktu widzenia heurystyki.

pheromone_evaporation_rate -  Wysoka wartość współczynnika parowania oznacza, że ślady feromonów szybciej się 
rozprzestrzeniają i znikały, co może prowadzić do mniejszej intensywności przeszukiwania obszarów przestrzeni 
rozwiązań. Z drugiej strony, niska wartość współczynnika parowania oznacza, że ślady feromonów pozostają dłużej i 
mogą skłonić mrówki do powtarzania tych samych ścieżek, co może prowadzić do zbyt intensywnego przeszukiwania

pheromone_constant - Wysoka wartość oznacza, że feromony są szybciej dodawane do ścieżek, co może prowadzić do 
intensywniejszego przeszukiwania obszarów przestrzeni rozwiązań, gdzie już wcześniej znajdowały się dobre 
rozwiązania. Zwiększenie stałej feromonów może poprawić jakość rozwiązania, kosztem czasu

iterations - Wysoka liczba iteracji oznacza, że algorytm będzie działał dłużej, co może pomóc w znalezieniu lepszych 
rozwiązań, ale może również spowodować przeszukiwanie tych samych obszarów przestrzeni rozwiązań wielokrotnie. Niska 
liczba może nie znaleźć najlepszego rozwiązania
'''
