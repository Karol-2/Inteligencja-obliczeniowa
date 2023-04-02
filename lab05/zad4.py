import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.dummy import DummyClassifier

df = pd.read_csv("iris.csv")

# Podział na zbiór treningowy i testowy
(train_set, test_set) = train_test_split(df, train_size=0.7)

# Macierz zmiennych objaśniających i wektor zmiennej celu dla zbioru treningowego
X_train = train_set.iloc[:, :-1].values
y_train = train_set.iloc[:, -1].values
X_test = test_set.iloc[:, :-1].values
y_test = test_set.iloc[:, -1].values

# DD
dd = DummyClassifier(strategy="stratified")
dd.fit(X_train, y_train)
y_pred = dd.predict(X_test)

acc_DD = round(accuracy_score(y_test, y_pred),2)
mac = confusion_matrix(y_test,y_pred)

print("DD:")
print("Dokładność:", acc_DD ,"%")
print("Macierz błędu:\n",mac)

# 3-NN
knn3 = KNeighborsClassifier(n_neighbors=3)
knn3.fit(X_train, y_train)
y_pred = knn3.predict(X_test)

acc_3 = round(accuracy_score(y_test, y_pred),2)
mac = confusion_matrix(y_test,y_pred)

print("3-NN:")
print("Dokładność:", acc_3 ,"%")
print("Macierz błędu:\n",mac)

# 5-NN
knn5 = KNeighborsClassifier(n_neighbors=5)
knn5.fit(X_train, y_train)
y_pred = knn5.predict(X_test)

acc_5 = round(accuracy_score(y_test, y_pred),2)
mac = confusion_matrix(y_test,y_pred)

print("5-NN:")
print("Dokładność:", acc_5 ,"%")
print("Macierz błędu:\n",mac)

# 11-NN
knn11 = KNeighborsClassifier(n_neighbors=11)
knn11.fit(X_train, y_train)
y_pred = knn11.predict(X_test)

acc_11 = round(accuracy_score(y_test, y_pred),2)
mac = confusion_matrix(y_test,y_pred)

print("11-NN:")
print("Dokładność:", acc_11 ,"%")
print("Macierz błędu:\n",mac)

# NB
nb = GaussianNB()
nb.fit(X_train, y_train)
y_pred = nb.predict(X_test)

acc_nb = round(accuracy_score(y_test, y_pred),2)
mac = confusion_matrix(y_test,y_pred)

print("Naive Bayes:")
print("Dokładność:", acc_nb ,"%")
print("Macierz błędu:\n",mac)

print("============================================")
print("DD:", acc_DD, "%")
print("3NN:", acc_3, "%")
print("5NN:", acc_5, "%")
print("11NN:", acc_11, "%")
print("NB:", acc_nb, "%")

# Nie da się jednoznacznie powiedzieć, który klasyfikator jest zawsze najlepszy, ponieważ to zależy od danych,

# Często najlepsze wyniki osiąga 3NN i NB
