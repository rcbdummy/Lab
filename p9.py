#9) Regression algorithm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
tou = 0.5
data = pd.read_csv('9.csv')
x_train = np.array(data.total_bill)
print(x_train)
x_train = x_train[:,np.newaxis]
print(len(x_train))
y_train = np.array(data.tip)
x_test = np.array([i/10 for i in range(500)])
x_test = x_test[:,np.newaxis]
y_test = []
count = 0
for r in range(len(x_test)):
    wts = np.exp(-np.sum((x_train-x_test[r])**2,axis=1)/(2*tou**2))
    W = np.diag(wts)
    factor1 = np.linalg.inv(x_train.T.dot(W).dot(x_train))
    parameters = factor1.dot(x_train.T).dot(W).dot(y_train)
    prediction = x_test[r].dot(parameters)
    y_test.append(prediction)
    count += 1
print(len(y_test))
y_test = np.array(y_test)
plt.plot(x_train.squeeze(),y_train,'o')
plt.plot(x_test.squeeze(),y_test,'o')
plt.show()