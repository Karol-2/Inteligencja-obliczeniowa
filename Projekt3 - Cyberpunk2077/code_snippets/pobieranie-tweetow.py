import csv
from datetime import datetime, timedelta

import snscrape.modules.twitter as sntwitter

max_len = 300


def save_to_csv(name, tweets):
    fieldnames = ['ID', 'Content', 'User', 'Date', 'Lang', 'Place', 'Hashtags']
    with open(name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames)
        writer.writeheader()
        for tweet in tweets:
            writer.writerow({'ID': tweet.id,
                             'Content': str(tweet.rawContent).replace('\n', ''),
                             'User': tweet.user.username,
                             'Date': tweet.date,
                             'Lang': tweet.lang,
                             'Place': tweet.place,
                             'Hashtags': tweet.hashtags})

    print(f"Pobrane tweety zostały zapisane do pliku: {name}")

def q8():
    start_date = '2020-11-01'
    end_date = '2021-02-28'
    query_template = '(#cyberpunk2077) until:{end_date} since:{start_date}'
    tweets = []
    i = 0

    current_date = datetime.strptime(start_date, "%Y-%m-%d")
    data_koncowa = datetime.strptime(end_date, "%Y-%m-%d") + timedelta(days=1)

    while current_date + timedelta(days=1) < data_koncowa:
        next_day = current_date + timedelta(days=1)
        query = query_template.format(start_date=current_date.strftime("%Y-%m-%d"), end_date=next_day.strftime("%Y-%m-%d"))

        for tweet in sntwitter.TwitterSearchScraper(query).get_items():
            tweets.append(tweet)
            i += 1
            print(i, tweet.date, query)

            if i >= max_len:
                i=0
                break

        if current_date + timedelta(days=1) > data_koncowa:
            break

        current_date = next_day

    csv_file = '../data_MIXED/daily_tweets.csv'
    save_to_csv(csv_file, tweets)

def q1():
    query = '(#cyberpunk2077) until:2018-06-12 since:2018-06-10'
    tweets = []
    i = 0

    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        tweets.append(tweet)
        i += 1
        print(i, tweet.date, query)

        if len(tweets) >= max_len:
            break

    csv_file = '../data_MIXED/daily_tweets.csv'
    save_to_csv(csv_file, tweets)


def q2():
    query = '(#cyberpunk2077) until:2018-08-29 since:2018-08-27'
    tweets = []
    i = 0

    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        tweets.append(tweet)
        i += 1
        print(i, tweet.date, query)

        if len(tweets) >= max_len:
            break

    csv_file = '../data_MIXED/cyberpunk_first_gameplay.csv'
    save_to_csv(csv_file, tweets)


def q3():
    query = '(#cyberpunk2077) until:2020-01-17 since:2020-01-16'
    tweets = []
    i = 0

    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        tweets.append(tweet)
        i += 1
        print(i, tweet.date, query)

        if len(tweets) >= max_len:
            break

    csv_file = '../data_MIXED/cyberpunk_first_move.csv'
    save_to_csv(csv_file, tweets)


def q4():
    query = '(#cyberpunk2077) until:2020-06-19 since:2020-06-18'
    tweets = []
    i = 0

    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        tweets.append(tweet)
        i += 1
        print(i, tweet.date, query)

        if len(tweets) >= max_len:
            break

    csv_file = '../data_MIXED/cyberpunk_second_move.csv'
    save_to_csv(csv_file, tweets)


def q5():
    query = '(#cyberpunk2077) until:2020-09-30 since:2020-09-29'
    tweets = []
    i = 0

    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        tweets.append(tweet)
        i += 1
        print(i, tweet.date, query)

        if len(tweets) >= max_len:
            break

    csv_file = '../data_MIXED/cyberpunk_third_move.csv'
    save_to_csv(csv_file, tweets)

def q6(): # dwa dni przed premiera
    query = '(#cyberpunk2077) until:2020-12-10 since:2020-12-08'
    tweets = []
    i = 0

    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        tweets.append(tweet)
        i += 1
        print(i, tweet.date, query)

        if len(tweets) >= max_len:
            break

    csv_file = '../data_MIXED/cyberpunk_before_release.csv'
    save_to_csv(csv_file, tweets)
def q7(): # dwa dni po premierze
    query = '(#cyberpunk2077) until:2020-12-12 since:2020-12-10'
    tweets = []
    i = 0

    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        tweets.append(tweet)
        i += 1
        print(i, tweet.date, query)

        if len(tweets) >= max_len:
            break

    csv_file = '../data_MIXED/cyberpunk_after_release.csv'
    save_to_csv(csv_file, tweets)

