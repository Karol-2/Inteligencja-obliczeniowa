import string
from collections import Counter
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# A)
print("A)")
with open('artykul.txt', 'r') as file:
    text = file.read()

# B)
print("B)")
tokens = word_tokenize(text.lower())
print("Liczba słów po tokenizacji:", len(tokens))
#print(tokens)

# C)
print("C)")

stop_words = set(stopwords.words('english'))
# print(stop_words)

filtered_sentence = []

for w in tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

#print(filtered_sentence)
print("Liczba słów po usuwaniu stop-words:", len(filtered_sentence))

# D)
print("D)")
filtered_sentence = [word for word in filtered_sentence if word not in string.punctuation]  # usunięcie znaków interpnkcyjnych
addictional_interpunct = ['`', "\"", "'s", "''", "``"]
second_filter_sentence = []
for w in filtered_sentence:
    if w not in addictional_interpunct:
        second_filter_sentence.append(w)

print("Liczba słów po dodatkowym filtrowaniu:", len(second_filter_sentence))

# E)
print("E)")
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(token) for token in second_filter_sentence]

# print(lemmatized_words)
print("Liczba słów po lematyzacji:", len(lemmatized_words))

# F)
print("F)")
word_counter = Counter(lemmatized_words)
most_common_words = word_counter.most_common(10)
words, counts = zip(*most_common_words)
print(most_common_words)

plt.bar(words, counts)
plt.xlabel('Słowa')
plt.ylabel('Liczba wystąpień')
plt.title('Najczęściej występujące słowa')
plt.xticks(rotation='vertical')
plt.show()

# G)
print("G)")

wordcloud_text = ' '.join(lemmatized_words)

wordcloud = WordCloud(width=800, height=400).generate(wordcloud_text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
