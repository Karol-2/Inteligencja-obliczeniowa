from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
iris = load_iris()

datasets = train_test_split(iris.data, iris.target,
                            test_size=0.7)

train_data, test_data, train_labels, test_labels = datasets
# TODO: jak train_labels i test_labels są skonwertowane na liczby, jakie to liczby, jakim napisom odpowiadają
scaler = StandardScaler()

# we fit the train data
scaler.fit(train_data)
# TODO: na czym polega skalowanie danych
# scaling the train data
train_data = scaler.transform(train_data)
test_data = scaler.transform(test_data)

model1 = MLPClassifier(hidden_layer_sizes=(2,), max_iter=2000)

# let's fit the training data to our model
model1.fit(train_data, train_labels)
print("Model 1")
predictions_test = model1.predict(test_data)
print(accuracy_score(predictions_test, test_labels))

model2 = MLPClassifier(hidden_layer_sizes=(3,), max_iter=2000)

model2.fit(train_data, train_labels)
print("Model 2")
predictions_test = model2.predict(test_data)
print(accuracy_score(predictions_test, test_labels))

model3 = MLPClassifier(hidden_layer_sizes=(3,3), max_iter=2000)

model3.fit(train_data, train_labels)
print("Model 3")
predictions_test = model3.predict(test_data)
print(accuracy_score(predictions_test, test_labels))
# model 2 ma najlepszą dokładność
