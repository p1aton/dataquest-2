## 2. Introduction To The Data ##

import pandas as pd

data = pd.read_csv('AmesHousing.txt', sep='\t')
train = data.iloc[:1460]
test = data.iloc[1460:]

train.info()

target = 'SalePrice'


## 3. Simple Linear Regression ##

import matplotlib.pyplot as plt
# For prettier plots.
import seaborn

plt.scatter(data['Garage Area'], data['SalePrice'])
plt.show()
plt.scatter(data['Gr Liv Area'], data['SalePrice'])
plt.show()
plt.scatter(data['Overall Cond'], data['SalePrice'])
plt.show()


## 5. Using Scikit-Learn To Train And Predict ##

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(train[['Gr Liv Area']], train['SalePrice'])
print(lr.coef_)
print(lr.intercept_)
a0 = lr.intercept_
a1 = lr.coef_


## 6. Making Predictions ##

import numpy as np
from sklearn.metrics import mean_squared_error

lr = LinearRegression()
lr.fit(train[['Gr Liv Area']], train['SalePrice'])

train_predictions  = lr.predict(train[['Gr Liv Area']])
test_predictions = lr.predict(test[['Gr Liv Area']])

train_mse = mean_squared_error(train_predictions, train['SalePrice'])
test_mse = mean_squared_error(test_predictions, test['SalePrice'])

train_rmse = np.sqrt(train_mse)
test_rmse = np.sqrt(test_mse)

print(train_rmse)
print(test_rmse)


## 7. Multiple Linear Regression ##

cols = ['Overall Cond', 'Gr Liv Area']

lr.fit(train[cols], train['SalePrice'])
train_predictions = lr.predict(train[cols])
test_predictions = lr.predict(test[cols])

train_rmse_2 = np.sqrt(mean_squared_error(train_predictions, train['SalePrice']))
test_rmse_2 = np.sqrt(mean_squared_error(test_predictions, test['SalePrice']))

print(train_rmse_2)
print(test_rmse_2)
