import csv
import snscrape.modules.twitter as sntwitter

def download_tweets_with_hashtags(hashtags, max_tweets):
    # Utwórz pustą listę na pobrane tweety
    tweets = []

    # Przejdź przez każdy hashtag
    for hashtag in hashtags:
        # Utwórz zapytanie do pobrania tweetów z danym hasztagiem
        query = f'#{hashtag}'
        number = 0

        # Pobierz tweety zgodne z zapytaniem
        for tweet in sntwitter.TwitterHashtagScraper(query).get_items():
            tweets.append(tweet)
            number+=1
            print(number)

            # Jeśli osiągnięto maksymalną liczbę pobranych tweetów, zakończ pobieranie
            if len(tweets) >= max_tweets:
                return tweets

    return tweets

hashtags = ['bejba','Blankazrezygnuj', 'eurovison', 'blanka']  # Lista hasztagów do wyszukiwania
max_tweets = 10  # Maksymalna liczba tweetów do pobrania

# Pobierz tweety
downloaded_tweets = download_tweets_with_hashtags(hashtags, max_tweets)

# Zapisz tweety do pliku CSV
csv_file = 'pobrane_tweety3.csv'
fieldnames = ['ID', 'Treść', 'Autor', 'Data']
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for tweet in downloaded_tweets:
        writer.writerow({'ID': tweet.id,
                         'Treść': tweet.content,
                         'Autor': tweet.user.username,
                         'Data': tweet.date})

print(f"Pobrane tweety zostały zapisane do pliku: {csv_file}")
