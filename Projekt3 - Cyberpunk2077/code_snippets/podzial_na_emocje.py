from text2emotion import get_emotion
from wordcloud import WordCloud
import matplotlib.pyplot as plt
def wordClouds(tweets, name):
    wordcloud_text = ' '.join(tweets)

    wordcloud = WordCloud(width=800, height=400).generate(wordcloud_text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(name)
    plt.show()
def process_tweets(all_tweets):
    happy_tweets = []
    sadness_tweets = []
    anger_tweets = []
    fear_tweets = []
    surprise_tweets = []

    for tweet in all_tweets:
        emotions = get_emotion(tweet)
        dominant_emotion = max(emotions, key=emotions.get)

        if dominant_emotion == 'Happy':
            happy_tweets.append(tweet)
        elif dominant_emotion == 'Sad':
            sadness_tweets.append(tweet)
        elif dominant_emotion == 'Angry':
            anger_tweets.append(tweet)
        elif dominant_emotion == 'Fear':
            fear_tweets.append(tweet)
        elif dominant_emotion == 'Surprise':
            surprise_tweets.append(tweet)



    wordClouds(happy_tweets,"Happy tweets")
    wordClouds(sadness_tweets,"Sad tweets")
    wordClouds(anger_tweets,"Angry tweets")
    wordClouds(fear_tweets,"Fear tweets")
    wordClouds(surprise_tweets,"Surprise tweets")


process_tweets(all_tweets)