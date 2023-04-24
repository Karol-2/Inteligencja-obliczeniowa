import numpy as np
from matplotlib import pyplot as plt

# tworzymy tablice o wymiarach 128x128x3 (3 kanaly to RGB)
# uzupelnioną zerami = kolor czarny
data = np.zeros((128, 128, 3), dtype=np.uint8)


# chcemy zeby obrazek byl czarnobialy,
# wiec wszystkie trzy kanaly rgb uzupelniamy tymi samymi liczbami
# napiszmy do tego funkcje
def draw(img, x, y, color):
    img[x, y] = [color, color, color]




# zamalowanie 4 pikseli w lewym górnym rogu
draw(data, 5, 5, 100)
draw(data, 6, 6, 100)
draw(data, 5, 6, 255)
draw(data, 6, 5, 255)


# rysowanie kilku figur na obrazku
for i in range(128):
    for j in range(128):
        if (i-64)**2 + (j-64)**2 < 900:
            draw(data, i, j, 200)
        elif i > 100 and j > 100:
            draw(data, i, j, 255)
        elif (i-15)**2 + (j-110)**2 < 25:
            draw(data, i, j, 150)
        elif (i-15)**2 + (j-110)**2 == 25 or (i-15)**2 + (j-110)**2 == 26:
            draw(data, i, j, 255)

# konwersja macierzy na obrazek i wyświetlenie
plt.imshow(data, interpolation='nearest')
plt.show()
# ZADANIE B
kernel = np.array([
    [1, 0, -1],
[1, 0, -1],
[1, 0, -1]])

def convolve2d(img, kernel, stride):
    output_shape = ((img.shape[0] - kernel.shape[0]) // stride) + 1, ((img.shape[1] - kernel.shape[1]) // stride) + 1
    output = np.zeros(output_shape)
    kernel_size = kernel.shape[0]
    padding = kernel_size // 2
    img_padded = np.pad(img, padding, mode='constant', constant_values=0)
    for i in range(0, img.shape[0]-kernel_size+1, stride):
        for j in range(0, img.shape[1]-kernel_size+1, stride):
            output[i//stride, j//stride] = np.sum(kernel * img_padded[i:i+kernel_size, j:j+kernel_size])
    return output


result = convolve2d(data[:, :, 0], kernel, stride=1)
plt.imshow(result, cmap='gray')
plt.show()
# zADANIE C
result = convolve2d(data[:, :, 0], kernel, stride=2)
plt.imshow(result, cmap='gray')
plt.show()

# ZADANIE D
kernel = np.array([
    [1, 1,1],
[0,0,0],
[-1,-1,-1]])
result = convolve2d(data[:, :, 0], kernel, stride=1)
plt.imshow(result, cmap='gray')
plt.show()
result = convolve2d(data[:, :, 0], kernel, stride=2)
plt.imshow(result, cmap='gray')
plt.show()