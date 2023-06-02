import csv
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# Inicjalizacja analizatora sentymentu
sia = SentimentIntensityAnalyzer()

# Inicjalizacja list na pozytywne i negatywne tweety
positive_tweets = []
negative_tweets = []

# Inicjalizacja list na długość tablicy positive i negative
positive_lengths = []
negative_lengths = []
dates = []

# Otwarcie pliku CSV
with open('../data_ENGLISH/ENG_daily_tweets.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    # Iteracja przez wiersze w pliku CSV
    for i, row in enumerate(reader):
        tweet = row['Content']
        date = row['Date']
        date = date[:10]  # Pobierz tylko pierwsze 10 znaków (rok, miesiąc, dzień)

        # Analiza sentymentu
        sentiment = sia.polarity_scores(tweet)

        # Podział na pozytywne i negatywne tweety
        if sentiment['compound'] >= 0.05:
            positive_tweets.append(tweet)
        elif sentiment['compound'] <= -0.05:
            negative_tweets.append(tweet)

        # Sprawdzenie, czy osiągnięto 300 tweetów
        if (i + 1) % 300 == 0:
            positive_lengths.append(len(positive_tweets))
            negative_lengths.append(len(negative_tweets))
            negative_tweets = []
            positive_tweets = []
            dates.append(date)

# Obliczenie liczby pozytywnych i negatywnych tweetów dla każdej partii
df = pd.DataFrame({'Positive': positive_lengths, 'Negative': negative_lengths}, index=dates)

# Wykres liniowy
df.plot(kind='line', figsize=(10, 6))
plt.grid()
plt.title('Liczba pozytywnych i negatywnych tweetów od listopada 2020 do lutego 2021')
plt.xlabel('Data')
plt.ylabel('Liczba tweetów')
plt.legend()
plt.show()
