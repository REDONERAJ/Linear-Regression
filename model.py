# model.py
import joblib
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression

housing = fetch_california_housing()
X = housing.data[:, [0, 1, 2, 3, 4]]  
y = housing.target

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "model.pkl")
