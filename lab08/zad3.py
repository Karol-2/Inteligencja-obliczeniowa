import snscrape.modules.twitter as sntwitter
# nie działa bo elon zepsuł twittera
def get_tweets_by_hashtag(hashtag, num_tweets):
    query = f'#{hashtag}'

    tweets = []
    for tweet in sntwitter.TwitterHashtagScraper(query).get_items():
        tweets.append(tweet)

        if len(tweets) >= num_tweets:
            break

    return tweets

hashtag = "ukraine"
num_tweets = 100

tweets = get_tweets_by_hashtag(hashtag, num_tweets)

for tweet in tweets:
    print(tweet.content)