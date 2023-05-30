import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('CDP-kursy.csv')

df['Data'] = pd.to_datetime(df['Data'])

# Utworzenie wykresu
plt.figure(figsize=(10, 6))
plt.plot(df['Data'], df['Zamknięcie'])
plt.xlabel('Data')
plt.ylabel('Zamknięcie')
plt.title('Wykres kursu spółki')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()
