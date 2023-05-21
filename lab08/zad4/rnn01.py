import numpy as np
from keras.layers import SimpleRNN

inputs = np.random.random([32, 10, 8]).astype(np.float32) # z 10 kroków czasowych (czyli jest 10 powtórzeń), pobieramy dane wielkości 8
# np. dane z 10 dni i za każdym razem mierzymy 8 różnych warunków pogodowych
# 32 wielkość batcha, ile takich próbek chemy, czyli 32x 80 parometrowe próbki
print("Inputs: ")
print(inputs)

simple_rnn = SimpleRNN(4)#  4 - przekazujemy 4 stany ukryte, cała wiedza o przeszłości będzie zakodowana w 4 liczbach zmiennoprzcinkowcyh

output = simple_rnn(inputs)  # The output has shape `[32, 4]`.
print("Output: ")
print(output)

simple_rnn = SimpleRNN(
    4, return_sequences=True, return_state=True)

# whole_sequence_output has shape `[32, 10, 4]`.
# final_state has shape `[32, 4]`.
whole_sequence_output, final_state = simple_rnn(inputs)