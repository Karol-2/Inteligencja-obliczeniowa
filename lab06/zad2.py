from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()

datasets = train_test_split(iris.data, iris.target,
                            test_size=0.7)

train_data, test_data, train_labels, test_labels = datasets
