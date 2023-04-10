import math


def forwardPass(wiek, waga, wzrost):
    hidden1 = -0.46122 * wiek + waga * 0.97314 + wzrost * -0.39203
    hidden1_po_aktywacji =f(hidden1 + 0.80109)
    hidden2 = wiek * 0.78548 + waga * 2.10584 + wzrost * -0.57847
    hidden2_po_aktywacji = f(hidden2 + 0.43529)
    output = hidden1_po_aktywacji * -0.81546 + hidden2_po_aktywacji * 1.03775
    return output + -0.2368


def f(x): # funkcja aktywacji
    return 1 / (1 + math.e ** (-x))


# forwardPass(23,75,176) = 0.798528
print(forwardPass(23, 75, 176))

print(forwardPass(25,67,180))
# wyniki sa bardzo bliskie oczekiwanym, różnice wynikają najprawdopodobniej z powodu zaokrągleń wyników

