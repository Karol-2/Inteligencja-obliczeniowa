import csv
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
tweets = []
with open('ENG_first_trailer.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        tweet = row['Content']
        tokens = word_tokenize(tweet)
        tokens = [token.lower() for token in tokens if token.isalpha()]  # Usunięcie znaków nie będących literami
        tokens = [token for token in tokens if token not in stop_words]  # Usunięcie stopwords
        tokens = [lemmatizer.lemmatize(token) for token in tokens]  # Lematyzacja

        processed_tweet = ' '.join(tokens)
        tweets.append(processed_tweet)
        print(processed_tweet)

print("==============")
print(tweets)
