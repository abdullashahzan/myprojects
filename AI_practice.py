import pandas as pd
from sklearn.model_selection import train_test_split as t
import tensorflow as tf

dataset = pd.read_csv("cancer.csv")
x = dataset.drop(columns = ["diagnosis(1=m, 0=b)"])
y = dataset["diagnosis(1=m, 0=b)"]

x_train, x_test, y_train, y_test = t(x, y, test_size= 0.2)

m = tf.keras.models.Sequential()

m.add(tf.keras.layers.Dense(64, input_shape = x_train.shape, activation = 'sigmoid'))
m.add(tf.keras.layers.Dense(64, activation = 'sigmoid'))
m.add(tf.keras.layers.Dense(1, activation = 'sigmoid'))

m.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

m.fit(x_train, y_train, epochs = 10)

m.evaluate(x_test, y_test)

print('success')