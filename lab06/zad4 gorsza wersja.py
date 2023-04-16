import pandas as pd
from keras.utils import plot_model
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np



# Wczytanie danych z pliku diabetes.csv
df = pd.read_csv('diabetes.csv')

# Podział danych na wejście i wyjście
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

# Zamiana wartości w kolumnie 'class' z 'tested_positive' i 'tested_negative' na 1 i 0 odpowiednio
y = [1 if i == 'tested_positive' else 0 for i in y]
y = np.array(y)
# Podział danych na zestaw uczący i testowy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

optimizers = ['adam', 'sgd']
activations = ['relu', 'sigmoid']
for optimizer_name in optimizers:
    for activation_name in activations:
        # Tworzenie modelu
        model = Sequential()

        # Dodawanie warstw ukrytych
        model.add(Dense(6, input_dim=X_train.shape[1], activation='relu'))
        model.add(Dense(3, activation='relu'))

        # Wyjściowa warstwa z jednym neuronem i funkcją aktywacji sigmoidalną
        model.add(Dense(1, activation='sigmoid'))

        # Kompilacja modelu
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

        # Trenowanie modelu
        history = model.fit(X_train, y_train, epochs=100, batch_size=10, verbose=0, validation_data=(X_test, y_test))


        # Ocena skuteczności modelu na zestawie testowym
        loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
        print(f"{optimizer_name} - {activation_name} model")
        print(f'Test Loss: {loss:.3f}, Test Accuracy: {accuracy:.3f}')

        # Wyświetlenie krzywej uczenia się
        plt.plot(history.history['accuracy'])
        plt.plot(history.history['val_accuracy'])
        plt.title('Model accuracy')
        plt.ylabel('Accuracy')
        plt.xlabel('Epoch')
        plt.legend(['Train', 'Test'], loc='upper left')
        plt.show()
        plot_model(model,show_shapes=True,show_layer_names=True,
                   to_file=f'{optimizer_name} - {activation_name} model.png')

        # Wyświetlenie macierzy błędu
        y_pred = model.predict(X_test)
        y_pred = (y_pred > 0.5)
        cm = confusion_matrix(y_test, y_pred)
        print(cm)
