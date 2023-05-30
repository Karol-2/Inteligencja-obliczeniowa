import pandas as pd

# Wczytaj plik CSV
data = pd.read_csv('ENG_daily_tweets.csv')

# Przekształć kolumnę 'Date' na format daty
data['Date'] = pd.to_datetime(data['Date'])

# Grupuj tweety według dat i zliczaj liczbę tweetów w każdej dacie
tweet_counts = data.groupby(data['Date'].dt.date).size().reset_index(name='Tweet Count')

# Wyświetl wynik
print(tweet_counts)