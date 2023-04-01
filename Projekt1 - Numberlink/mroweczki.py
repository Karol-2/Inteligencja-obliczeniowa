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
