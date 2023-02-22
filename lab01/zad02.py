import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

miasta = pd.read_csv("miasta.csv")
print("zadanie 2 a")
print(miasta)
print(miasta.values)
print("zadanie 2 b")

new_row = [2010, 460, 555, 405]
miasta.loc[10] = new_row

print(miasta)
print("zadanie 2 c")

plt.plot(miasta['Rok'], miasta['Gdansk'], 'ro-')

years = np.arange(miasta['Rok'].min(), miasta['Rok'].max() + 1, 10)
plt.xticks(years)

plt.title('Ludność Gdańska')
plt.xlabel('Rok')
plt.ylabel('Liczba ludności [w tys.]')
plt.grid()
plt.show()

print("zadanie 2 d")
plt.plot(miasta['Rok'], miasta['Gdansk'], 'bo-', label='Gdańsk')
plt.plot(miasta['Rok'], miasta['Poznan'], 'go-', label='Poznań')
plt.plot(miasta['Rok'], miasta['Szczecin'], 'ro-', label='Szczecin')

plt.xticks(years)
plt.title('Ludność w miastach Polski')
plt.xlabel('Rok')
plt.ylabel('Liczba ludności [w tys.]')
plt.grid()

plt.legend()

plt.show()

print("zadanie 2 e")
kolumny = miasta[['Gdansk', 'Poznan', 'Szczecin']]


def standaryzacja_kolumny(col):
    return (col - col.mean()) / col.std()


miasta_standaryzowane = kolumny.apply(standaryzacja_kolumny, axis=0)

print(miasta_standaryzowane)

srednia = miasta_standaryzowane.mean()
odchylenie = miasta_standaryzowane.std()
print("ŚREDNIA:")
print(srednia)
print("ODCHYLENIE:")
print(odchylenie)

print("zadanie 2 f")


def normalizacja_kolumny(col):
    return (col - col.min()) / (col.max() - col.min())


miasta_normalizowane = kolumny.apply(normalizacja_kolumny, axis=0)

print(miasta_normalizowane)

min = miasta_normalizowane.min()
max = miasta_normalizowane.max()
print("MIN:")
print(min)
print("MAX:")
print(max)
