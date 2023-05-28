import csv
import re
from wordcloud import WordCloud
import nltk
from matplotlib import pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


def wordClouds(tweets):
    wordcloud_text = ' '.join(tweets)

    wordcloud = WordCloud(width=800, height=400).generate(wordcloud_text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()


lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
phrases_to_remove = []
words_to_remove = []

tweets = []
with open('ENG_after_release.csv', 'r',encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        tweet = row['Content']
        tweet = re.sub(r'http\S+|https\S+', '', tweet) # usuwanie linków
        for phrase in phrases_to_remove:
            tweet = tweet.replace(phrase, '') # usunięcie powtarzajacych się fraz
        tokens = word_tokenize(tweet) # tokenizacja
        tokens = [token.lower() for token in tokens if token.isalpha()]  # Usunięcie znaków nie będących literami
        tokens = [token for token in tokens if token not in stop_words]  # Usunięcie stopwords
        tokens = [lemmatizer.lemmatize(token) for token in tokens]  # Lematyzacja
        tokens = [token for token in tokens if token not in words_to_remove]
        #print(tokens)
        processed_tweet = ' '.join(tokens)
        tweets.append(processed_tweet)


sia = SentimentIntensityAnalyzer()
positive_tweets=[]
negative_tweets=[]
for tweet in tweets:
    sentiment = sia.polarity_scores(tweet)
    if sentiment['compound'] >= 0.05:
        positive_tweets.append(tweet)
    elif sentiment['compound'] <= -0.05:
        negative_tweets.append(tweet)

wordClouds(positive_tweets)
wordClouds(negative_tweets)

