import pandas as pd
from googletrans import Translator


# pip install googletrans==3.1.0a0


def translate_to_english(text, lang):
    translate_to_english.call_counter += 1
    print(translate_to_english.call_counter, lang)
    if lang == 'en':
        return text
    elif lang == 'und' or lang == 'qme' or lang == 'qht':
        return text
    elif lang == 'zh':
        translator = Translator(service_urls=['translate.googleapis.com'])
        translation = translator.translate(text, dest='en', src='zh-tw')
        return translation.text
    elif lang == 'in':
        translator = Translator(service_urls=['translate.googleapis.com'])
        translation = translator.translate(text, dest='en', src='es')
        return translation.text
    else:
        translator = Translator(service_urls=['translate.googleapis.com'])
        translation = translator.translate(text, dest='en', src=lang)
        return translation.text


translate_to_english.call_counter = 0

def q8():
    translate_to_english.call_counter = 0
    df = pd.read_csv('../data_MIXED/daily_tweets.csv')
    df['Content'] = df.apply(lambda row: translate_to_english(row['Content'], row['Lang']), axis=1)

    df.to_csv('ENG_daily_tweets.csv', index=False)
def q1():
    translate_to_english.call_counter = 0
    df = pd.read_csv('../data_MIXED/cyberpunk_first_move.csv')
    df['Content'] = df.apply(lambda row: translate_to_english(row['Content'], row['Lang']), axis=1)

    df.to_csv('ENG_first_move.csv', index=False)


def q2():
    translate_to_english.call_counter = 0
    df = pd.read_csv('../data_MIXED/cyberpunk_second_move.csv')
    df['Content'] = df.apply(lambda row: translate_to_english(row['Content'], row['Lang']), axis=1)

    df.to_csv('ENG_second_move.csv', index=False)


def q3():
    translate_to_english.call_counter = 0
    df = pd.read_csv('../data_MIXED/cyberpunk_third_move.csv')
    df['Content'] = df.apply(lambda row: translate_to_english(row['Content'], row['Lang']), axis=1)

    df.to_csv('ENG_third_move.csv', index=False)


def q4():
    translate_to_english.call_counter = 0
    df = pd.read_csv('../data_MIXED/cyberpunk_after_release.csv')
    df['Content'] = df.apply(lambda row: translate_to_english(row['Content'], row['Lang']), axis=1)

    df.to_csv('ENG_after_release.csv', index=False)


def q5():
    translate_to_english.call_counter = 0
    df = pd.read_csv('../data_MIXED/cyberpunk_before_release.csv')
    df['Content'] = df.apply(lambda row: translate_to_english(row['Content'], row['Lang']), axis=1)

    df.to_csv('ENG_before_release.csv', index=False)


def q6():
    translate_to_english.call_counter = 0
    df = pd.read_csv('../data_MIXED/cyberpunk_first_trailer.csv')
    df['Content'] = df.apply(lambda row: translate_to_english(row['Content'], row['Lang']), axis=1)

    df.to_csv('ENG_first_trailer.csv', index=False)


def q7():
    translate_to_english.call_counter = 0
    df = pd.read_csv('../data_MIXED/cyberpunk_first_gameplay.csv')
    df['Content'] = df.apply(lambda row: translate_to_english(row['Content'], row['Lang']), axis=1)

    df.to_csv('ENG_first_gameplay.csv', index=False)


