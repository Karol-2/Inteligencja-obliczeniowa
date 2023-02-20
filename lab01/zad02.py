import pandas as pd
import matplotlib.pyplot as plt

miasta = pd.read_csv("miasta.csv")
print("zadanie 2 a")
print(miasta)
print(miasta.values)
print("zadanie 2 b")

new_row = [2010,460,555,405]
df = pd.DataFrame(miasta)
df.loc[len(df)] = new_row

print(df)
print("zadanie 2 c")
df.plot(kind='line',x="Rok",xticks=df.Rok,y="Gdansk",color="red", xlabel="Lata",
        ylabel="Liczba ludności (w tys.)",
        legend=False,title="Ludność w Gdańsku", style='.-'
        )
plt.gca().set_aspect('auto')

plt.show()

print("zadanie 2 d")

df.plot(kind='line',x="Rok",xticks=df.Rok, xlabel="Lata",
        ylabel="Liczba ludności (w tys.)",
        title="Ludność w miastach Polski", style='.-')
plt.show()