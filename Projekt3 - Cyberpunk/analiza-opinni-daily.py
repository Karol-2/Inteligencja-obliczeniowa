import csv

import matplotlib.dates as mdates
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import text2emotion as te


def save_to_csv(data, file_name):
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Emotions'])  # Nagłówek kolumny

        for batch in data:
            for tweet in batch:
                writer.writerow([tweet])
def calculate_average_emotions(file):
    emotions = ['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']
    tweets = 0
    tweets_per_day = 300
    data = pd.read_csv(file)
    all_emotions = []

    data['Date'] = pd.to_datetime(data['Date'])
    unikalne_daty = data['Date'].dt.date.unique()
    print(unikalne_daty)

    for date in unikalne_daty:
        subset = data[data['Date'].dt.date == date]
        content = subset['Content'].tolist()

        for i in range(0, len(content), tweets_per_day):
            batch = content[i:i + tweets_per_day]
            averages = {emotion: 0 for emotion in emotions}
            for content in batch:
                tweets += 1

                result = te.get_emotion(content)
                print(tweets)

                for emotion in emotions:
                    averages[emotion] += result[emotion]

            for emotion in emotions:
                averages[emotion] = averages[emotion] / tweets_per_day

            all_emotions.append(averages)
            print(all_emotions)

    save_to_csv(all_emotions,'all_emotions.csv')
    save_to_csv(unikalne_daty, 'dates.csv')
    plot_emotion_changes(unikalne_daty,all_emotions)



def plot_emotion_changes(dates, emotions):
    x = [datetime.strptime(date, "%Y-%m-%d %H:%M:%S%z") for date in dates]
    y_happy = [emotion['Happy'] for emotion in emotions]
    y_angry = [emotion['Angry'] for emotion in emotions]
    y_surprise = [emotion['Surprise'] for emotion in emotions]
    y_sad = [emotion['Sad'] for emotion in emotions]
    y_fear = [emotion['Fear'] for emotion in emotions]

    fig, ax = plt.subplots()
    ax.yaxis.tick_left()
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))

    # Dodawanie danych emocji na wykres
    ax.plot(x, y_happy, label='Happy', color='g', marker='o')
    ax.plot(x, y_angry, label='Angry', color='r', marker='o')
    ax.plot(x, y_surprise, label='Surprise', color='c', marker='o')
    ax.plot(x, y_sad, label='Sad', color='b', marker='o')
    ax.plot(x, y_fear, label='Fear', color='m', marker='o')

    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    ax.set_xlabel('Data')
    ax.set_ylabel('Poziom Emocji')
    plt.xticks(rotation=45)

    ax.grid()
    plt.title('Analiza Czasowa Emocji')
    plt.savefig('Analiza Czasowa Emocji - daily.png')
    plt.show()


file= 'ENG_daily_tweets.csv'
calculate_average_emotions(file)
