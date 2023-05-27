import pandas as pd
from googletrans import Translator

df = pd.read_csv('cyberpunk_after_release.csv')
translator = Translator()

def translate_to_english(text, lang):
    if lang == 'en':
        return text
    else:
        translation = translator.translate(text, src=lang, dest='en')
        return translation.text

df['Content'] = df.apply(lambda row: translate_to_english(row['Content'], row['Lang']), axis=1)

df.to_csv('ENG_after_release.csv', index=False)
