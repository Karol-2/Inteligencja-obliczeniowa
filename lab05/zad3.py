from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import export_text
from sklearn.metrics import confusion_matrix
import pandas as pd

df = pd.read_csv("iris.csv")
(train_set,test_set) = train_test_split(df.values,train_size=0.7,random_state=278874)

# A)
all_inputs = df[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].values
all_classes = df['species'].values

(train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7, random_state=1)

train_df = pd.DataFrame(train_set, columns=df.columns)
test_df = pd.DataFrame(test_set, columns=df.columns)

print("Zbiór treningowy:")
print(train_df)
print("\nZbiór testowy:")
print(test_df)

# B)
dtc = DecisionTreeClassifier()
# C)
dtc.fit(train_inputs, train_classes)
dtc.score(test_inputs, test_classes)

# D)
tree_rules = export_text(dtc, feature_names=['sepal.length', 'sepal.width', 'petal.length', 'petal.width'])
print("\nDrzewo decyzyjne:")
print(tree_rules)

# E)
print(f"Dokładność klasyfikacji na zbiorze testowym: {dtc.score(test_inputs, test_classes)} %")

# F)
y_pred = dtc.predict(test_inputs)
macierz= confusion_matrix(test_classes, y_pred)
print("\nMacierz błędów:")
print(macierz)
# trochę lepszy niż mój
