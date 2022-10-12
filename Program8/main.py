import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Importing Dataset
dataset = datasets.load_iris()
X = pd.DataFrame(dataset.data)
y = pd.DataFrame(dataset.target)

# Splitting The Dataset Into Training Set And Testing Set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model Fit And Prediction
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train.values.ravel())

accuracy_train = knn.score(X_train, y_train)
accuracy_test = knn.score(X_test, y_test)

print("Training Accuracy\n", accuracy_train)
print("Testing Accuracy\n", accuracy_test)

available_class = pd.DataFrame(dataset.target_names)
print("Dataset Classes\n", available_class)

example = np.array([5.7, 3, 4.2, 1.2])
example = example.reshape(1, -1)
print("Input Sample\n", example)

example_prediction = int(knn.predict(example))
print("Predicted Class\n", available_class[0][example_prediction])
