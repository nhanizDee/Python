# Import packages and functions
import numpy as np

import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Import dataset
sleep = pd.read_csv('sleep1.csv')

# Create input matrix X and output matrix y
X = sleep[['awake', 'brainwt']]
y = sleep[['vore']]

knnModel = KNeighborsClassifier(n_neighbors=4)
knnModel = knnModel.fit(X.values, np.ravel(y.values))

# Create a 2D array for the guinea pigs' REM sleep cycles and awake hours
guinea_pig_data = np.array([[0.8, 14.6]])

# Use the kneighbors() method to find the instances closest to the guinea pigs
distances, neighbors = knnModel.kneighbors(guinea_pig_data)


# Print neighbors
print(neighbors)

# Challenge 2

