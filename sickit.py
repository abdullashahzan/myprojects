from sklearn.linear_model import LinearRegression
import numpy as np

model = LinearRegression()

#Data

X = np.array([
    [8,2],
    [9,0],
    [11,2],
    [16,2],
    [12,0]
    ])

y = [11, 8.5, 15, 18, 11]

model.fit(X, y)

print(model.predict(np.array([[40,24]])))
