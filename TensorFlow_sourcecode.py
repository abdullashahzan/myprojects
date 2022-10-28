import tensorflow as tf
import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt

n = int(input("Enter the label: "))

data = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = data.load_data()

plt.imshow(test_images[n], cmap = 'gray' , vmin = 0, vmax = 255)
plt.show()

model = keras.Sequential([
    #input layer for neural network
    keras.layers.Flatten(input_shape = (28,28)),
    #Hidden layer for neural network
    keras.layers.Dense(units = 128, activation = tf.nn.relu),
    #output layer for neural network
    keras.layers.Dense(units = 10, activation = tf.nn.softmax)
    ])

model.compile(optimizer = tf.optimizers.Adam(), loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])
model.fit(train_images, train_labels, epochs = 5)
test_loss = model.evaluate(test_images, test_labels)
predictions = model.predict(test_images)
fo = list(predictions[n]).index(max(predictions[n]))

if fo == 0:
    print("The above image is of T-shirt/top")
elif fo == 1:
    print("The above image is of Trouser")
elif fo == 2:
    print("The above image is of Pullover")
elif fo == 3:
    print("The above image is of Dress")
elif fo == 4:
    print("The above image is of Coat")
elif fo == 5:
    print("The above image is of Sandal")
elif fo == 6:
    print("The above image is of Shirt")
elif fo == 7:
    print("The above image is of Sneaker")
elif fo == 8:
    print("The above image is of Bag")
elif fo == 9:
    print("The above image is of Ankle Boot")


print("Code ran successfully")