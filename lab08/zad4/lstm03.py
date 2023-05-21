# Load LSTM network and generate text
import sys
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import LSTM
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.utils import to_categorical
# load ascii text and covert to lowercase
filename = "wonderland.txt"
raw_text = open(filename, 'r', encoding='utf-8').read()
raw_text = raw_text.lower()
# create mapping of unique chars to integers, and a reverse mapping
chars = sorted(list(set(raw_text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))
int_to_char = dict((i, c) for i, c in enumerate(chars))
# summarize the loaded data
n_chars = len(raw_text)
n_vocab = len(chars)
print("Total Characters: ", n_chars)
print("Total Vocab: ", n_vocab)
# prepare the dataset of input to output pairs encoded as integers
seq_length = 100
dataX = []
dataY = []
for i in range(0, n_chars - seq_length, 1):
	seq_in = raw_text[i:i + seq_length]
	seq_out = raw_text[i + seq_length]
	dataX.append([char_to_int[char] for char in seq_in])
	dataY.append(char_to_int[seq_out])
n_patterns = len(dataX)
print("Total Patterns: ", n_patterns)
# reshape X to be [samples, time steps, features]
X = np.reshape(dataX, (n_patterns, seq_length, 1))
# normalize
X = X / float(n_vocab)
# one hot encode the output variable
y = to_categorical(dataY)
# define the LSTM model
model = Sequential()
model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2])))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation='softmax'))
# load the network weights
#filename = "weights-improvement-03-2.7199.hdf5"
filename = "IMPROVED-weights-improvement-03-2.5125.hdf5"
model.load_weights(filename)
model.compile(loss='categorical_crossentropy', optimizer='adam')
# pick a random seed
start = np.random.randint(0, len(dataX)-1)
pattern = dataX[start]
print("Seed:")
print("\"", ''.join([int_to_char[value] for value in pattern]), "\"")
# generate characters
for i in range(500):
	x = np.reshape(pattern, (1, len(pattern), 1))
	x = x / float(n_vocab)
	prediction = model.predict(x, verbose=0)
	index = np.argmax(prediction)
	result = int_to_char[index]
	seq_in = [int_to_char[value] for value in pattern]
	sys.stdout.write(result)
	pattern.append(index)
	pattern = pattern[1:len(pattern)]
print("\nDone.")

'''
Poczatkowe: 
" e could be no doubt that it had
a _very_ turn-up nose, much more like a snout than a real nose; also "
e th the tar  “he soet to the toe toe toe toe toe toe toe toe toe toe toe toe toe toet th the tar  “he soet to the toe toe toe toe toe toe toe toe toe toe toe toe toe toet th the tar  “he soet to the toe toe toe toe toe toe toe toe toe toe toe toe toe toet th the tar  “he soet to the toe toe toe toe toe toe toe toe toe toe toe toe toe toet th the tar  “he soet to the toe toe toe toe toe toe toe toe toe toe toe toe toe toet th the tar  “he soet to the toe toe toe toe toe toe toe toe toe toe toe t

Dotrenowany:
“suppose we change the subject,” the march hare interrupted, yawning.
“i’m g "
 sas io the wout an an an aale ”huh tou den to tee tou do whu ”hu soue tou de tou dal to tee tou do whu sou do whu sou do whu sou do whu so tee tou do an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an a

'''