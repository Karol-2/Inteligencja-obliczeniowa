import matplotlib.dates as mdates
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import text2emotion as te


def calculate_average_emotions(files):
    emotions = ['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']
    dates = []
    tweets = 0
    all_emotions = []

    for file in files:
        print(file)
        averages = {emotion: 0 for emotion in emotions}
        data = pd.read_csv(file)
        file_length = len(data)
        dates.append(data['Date'].values[0])

        for content in data['Content']:
            tweets += 1
            result = te.get_emotion(content)
            print(tweets)

            for emotion in emotions:
                averages[emotion] += result[emotion]

        for emotion in emotions:
            averages[emotion] = averages[emotion] / file_length

        all_emotions.append(averages)

    plot_emotion_changes(dates,all_emotions)



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
    plt.savefig('Analiza Czasowa Emocji - 129676.png')
    plt.show()


file_paths = ['ENG_first_trailer.csv', 'ENG_first_gameplay.csv', 'ENG_first_move.csv',
              'ENG_second_move.csv', 'ENG_third_move.csv', 'ENG_before_release.csv', 'ENG_after_release.csv']
calculate_average_emotions(file_paths)
