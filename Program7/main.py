import sklearn.metrics as sm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture

# Importing Dataset
dataset = datasets.load_iris()

# Attribute Variable(s)
X = pd.DataFrame(dataset.data)
X.columns = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width']
# Target Variable
y = pd.DataFrame(dataset.target)
y.columns = ['Targets']

plt.figure(figsize=(14, 7))
colormap = np.array(['darkorange', 'navy', 'darkgreen'])

# REAL PLOT
plt.subplot(1, 3, 1)
plt.scatter(X.Petal_Length, X.Petal_Width, c=colormap[y.Targets], s=40)
plt.title('Real Classification')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')

# K-PLOT
plt.subplot(1, 3, 2)
model = KMeans(n_clusters=3)
model.fit(X)
predY = np.choose(model.labels_, [0, 1, 2]).astype(np.int64)
plt.scatter(X.Petal_Length, X.Petal_Width, c=colormap[predY], s=40)
plt.title('K-Means')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
print('K-Means Algorithm')
print('The Accuracy Score Of K-Mean Algorithm: ', sm.accuracy_score(y, model.labels_))
print('The Confusion Matrix Of K-Mean Algorithm:\n', sm.confusion_matrix(y, model.labels_))

# EM PLOT
scaler = preprocessing.StandardScaler()
scaler.fit(X)
xsa = scaler.transform(X)
xs = pd.DataFrame(xsa, columns=X.columns)
gmm = GaussianMixture(n_components=3)
gmm.fit(xs)
y_gmm = gmm.predict(xs)
plt.subplot(1, 3, 3)
plt.scatter(X.Petal_Length, X.Petal_Width, c=colormap[y_gmm], s=40)
plt.title('GMM Classification')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
print('EM Algorithm')
print('The Accuracy Score Of EM Algorithm: ', sm.accuracy_score(y, y_gmm))
print('The Confusion Matrix Of EM Algorithm:\n', sm.confusion_matrix(y, y_gmm))

plt.show()