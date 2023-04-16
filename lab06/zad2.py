from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
iris = load_iris()

# Podział na część testową i treningową
datasets = train_test_split(iris.data, iris.target,
                            test_size=0.7)

train_data, test_data, train_labels, test_labels = datasets
'''
tykiety klas są reprezentowane przez liczby całkowite od 0 do 2, gdzie:
0 odpowiada klasie "Iris Setosa"
1 odpowiada klasie "Iris Versicolor"
2 odpowiada klasie "Iris Virginica"
'''
scaler = StandardScaler()
scaler.fit(train_data)
# przeskalowanie danych
train_data = scaler.transform(train_data)
test_data = scaler.transform(test_data)

# model sieci neuronowej z czteroneuronową warstwą
# wejściową, jedną ukrytą warstwą z dwoma
# neuronami i warstwą wyjściową z jednym neuronem
model1 = MLPClassifier(hidden_layer_sizes=(2,), max_iter=2000)

model1.fit(train_data, train_labels)
print("Model 1")
predictions_test = model1.predict(test_data)
print(accuracy_score(predictions_test, test_labels))

# model sieci neuronowej z czteroneuronową warstwą
# wejściową, jedną ukrytą warstwą z trzema
# neuronami i warstwą wyjściową z jednym neuronem
model2 = MLPClassifier(hidden_layer_sizes=(3,), max_iter=2000)
model2.fit(train_data, train_labels)
print("Model 2")
predictions_test = model2.predict(test_data)
print(accuracy_score(predictions_test, test_labels))

# model sieci neuronowej z czteroneuronową warstwą
# wejściową, dwoma ukrytymi warstwami z trzema
# neuronami każda i warstwą wyjściową z jednym neuronem
model3 = MLPClassifier(hidden_layer_sizes=(3,3), max_iter=2000)
model3.fit(train_data, train_labels)
print("Model 3")
predictions_test = model3.predict(test_data)
print(accuracy_score(predictions_test, test_labels))

# model 2 ma najlepszą dokładność
