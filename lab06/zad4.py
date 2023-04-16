import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical,plot_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt


# Wczytanie danych
df = pd.read_csv('diabetes.csv')
pd.set_option('display.max_columns', None)

# Podział na cechy i etykiety
target_column = ['class']
predictors = list(set(list(df.columns))-set(target_column))
df[predictors] = df[predictors]/df[predictors].max()

X = df[predictors].values
y = df[target_column].values.ravel()

# Kodowanie etykiet kategorialnych
le = LabelEncoder()
y = le.fit_transform(y)

# Podział na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=40)

# Konwersja etykiet na wektory kategorialne
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)


# Definicja modelu i jego trenowanie oraz wizualizacja wyników
optimizers = ['adam', 'sgd']
activations = ['relu', 'sigmoid']

for optimizer_name in optimizers:
    for activation_name in activations:
        model = Sequential()
        model.add(Dense(6, input_dim=8, activation=activation_name))
        model.add(Dense(3, activation=activation_name))
        model.add(Dense(2, activation='sigmoid'))
        model.compile(loss='categorical_crossentropy', optimizer=optimizer_name, metrics=['accuracy'])
        history = model.fit(X_train, y_train, epochs=100, batch_size=10, validation_data=(X_test, y_test), verbose=0)

        # Dokładność i macierz błędu
        y_pred = model.predict(X_test)
        y_pred_classes = y_pred.argmax(axis=-1)
        y_test_classes = y_test.argmax(axis=-1)
        accuracy = accuracy_score(y_test_classes, y_pred_classes)
        conf_matrix = confusion_matrix(y_test_classes, y_pred_classes)
        print(f"Model {optimizer_name}, {activation_name}")
        print("Zbior testowy:")
        print("Dokladnosc:", accuracy)
        print("Macierz bledu:\n", conf_matrix)

        # Wykres krzywej uczenia się
        plt.plot(history.history['loss'], label='Train')
        plt.plot(history.history['val_loss'], label='Test')
        plt.title(f'Model loss ({optimizer_name}, {activation_name})')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.legend()
        plt.savefig(f"{optimizer_name} - {activation_name} wykres.png",format="png")
        plt.show()


        plot_model(model,show_shapes=True,show_layer_names=True,to_file=f'{optimizer_name} - {activation_name} model.png')

'''
Tak, ważne jest, aby przerwać trenowanie w pewnym momencie, aby uniknąć przeuczenia modelu. 
Przeuczenie (overfitting) występuje, gdy model zbyt dokładnie dopasowuje się do zbioru treningowego, a nie jest w stanie ogólniejszych wzorców i zależności występujących w danych.

Można odczytać, czy model jest przeuczony z wykresu funkcji straty (loss). Funkcja straty na zbiorze treningowym będzie maleć, a funkcja straty na zbiorze testowym może zacząć rosnąć lub przynajmniej przestanie maleć. 

Jeśli model jest niedouczony (underfitting), to funkcja straty będzie wysoka zarówno na zbiorze treningowym, jak i testowym, a skuteczność na obu zbiorach będzie niska.
'''

'''
połączenie adam i relu daje najlepsze wyniki
'''