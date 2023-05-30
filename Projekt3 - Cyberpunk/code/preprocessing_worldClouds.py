import csv
import re
import nltk
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


def preprocessing(nazwa, phrases_to_remove, words_to_remove):  # funkcja zajmująca się preprocessingiem
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))

    tweets = []
    with open(nazwa, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            tweet = row['Content']
            tweet = re.sub(r'http\S+|https\S+', '', tweet)  # usuwanie linków z tweetów
            for phrase in phrases_to_remove:
                tweet = tweet.replace(phrase, '')  # usunięcie powtarzajacych się fraz
            tokens = word_tokenize(tweet)  # tokenizacja
            tokens = [token.lower() for token in tokens if token.isalpha()]  # Usunięcie znaków nie będących literami
            tokens = [token for token in tokens if token not in stop_words]  # Usunięcie stopwords
            tokens = [lemmatizer.lemmatize(token) for token in tokens]  # Lematyzacja
            tokens = [token for token in tokens if token not in words_to_remove]  # Usunięcie pojedynczych słów

            processed_tweet = ' '.join(tokens)
            tweets.append(processed_tweet)
    return tweets


def wordClouds(tweets, name):
    wordcloud_text = ' '.join(tweets)

    wordcloud = WordCloud(width=800, height=400).generate(wordcloud_text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(name)
    plt.show()


phrases_to_remove = ['cyberpunk', 'youtube', 'video', 'game', 'liked youtube', 'youtube cyberpunk',
                     'cyberpunk official', 'official trailer', 'official trailer cyberpunk', 'liked youtube',
                     'cyberpunk official', 'liked youtube cyberpunk', "halo infinite", "dying", "light", "devil", "cry",
                     "devil may cry", "dying light", "shadow die", "fallout", "metro exodus", "tomb raider",
                     "kingdom heart", "forza horizon", "microsoft", "division", "xbox", "forza horizon"]
words_to_remove = ['may', 'cry', 'cyberpunk', 'youtube', 'shadow', 'devil', 'die', 'dying', 'trailer', 'gear', 'war']

tweets_first_trailer = preprocessing('ENG_first_trailer.csv', phrases_to_remove, words_to_remove)
tweets_first_gameplay = preprocessing('ENG_first_gameplay.csv', phrases_to_remove, words_to_remove)
tweets_first_move = preprocessing('ENG_first_move.csv', phrases_to_remove, words_to_remove)
tweets_second_move = preprocessing('ENG_second_move.csv', phrases_to_remove, words_to_remove)
tweets_third_move = preprocessing('ENG_third_move.csv', phrases_to_remove, words_to_remove)
tweets_before_release = preprocessing('ENG_before_release.csv', phrases_to_remove, words_to_remove)
tweets_after_release = preprocessing('ENG_after_release.csv', phrases_to_remove, words_to_remove)


def analiza(tweets, topic):
    sia = SentimentIntensityAnalyzer()
    positive_tweets = []
    negative_tweets = []
    for tweet in tweets:
        sentiment = sia.polarity_scores(tweet)
        if sentiment['compound'] >= 0.05:
            positive_tweets.append(tweet)
        elif sentiment['compound'] <= -0.05:
            negative_tweets.append(tweet)

    wordClouds(positive_tweets, 'Pozytywne określenia odnośnie ' + topic)
    wordClouds(negative_tweets, 'Negatywne określenia odnośnie ' + topic)
