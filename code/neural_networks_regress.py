'''
This is an implementation of neural networks for multiple output regressing.
data is read as targets and features and the output from ~ data/train_targets.csv and ~data/train_features.csv

@author ~maxwell Aladago 3rd march 2017
'''

from sklearn.neural_network import MLPRegressor
import csv
import numpy as np
from sklearn.metrics import r2_score

# a function to read in a csv file and return a numpy array of the data in that file
# returns an array of the contents of the file
def read_data(filename):
    with open(filename, 'rt') as inputfile:
        data = []  # read rows as arrays and convert to numpy later
        all_data = csv.reader(inputfile)
        # headers = all_data.__next() #skip headers

        for row in all_data:
            data.append(row)
        # convert the data to a numpy array for easy manipulation
        data_in_numpy = np.array(data, dtype='float')
        return data_in_numpy


# read in the various files
features = read_data("../data/train_features.csv")
targets = read_data("../data/train_targets.csv")
test_features = read_data("../data/test_features.csv")
test_targets = read_data("../data/test_targets.csv")

# initialize neural regressor using tanh activations and stochastic gradient as the solver. learning rate is adaptive
wizard = MLPRegressor(hidden_layer_sizes=10000, activation='tanh', solver='adam')
# fit features and corresponding targets
wizard.fit(features, targets)

# test model
predicted_targets = wizard.predict(test_features)

print(predicted_targets)
print(test_targets)

# get the score of the predictions
score = r2_score(test_targets, predicted_targets)

print(score)
