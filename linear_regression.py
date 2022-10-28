#Linear regression

import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style

data = pd.read_csv("student-mat.csv", sep= ";")
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

predict = "G3"

"""Basically in x we gonna add all the attributes aka columns except the G3 column because 
we want to predict it in other words want machine to predict it"""
"""y is what we want to predict and x is the data that we give to the computer"""

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

"""So the model splits the data in training data and testing data and since we wrote the
test size = 0.1, the testing data will be 10% of 395 which is ~40"""
#This thing gave me error because i didnt seperate the values correctly
#x_train, y_train, x_test, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

#The correct format is this
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x,y, test_size= 0.1)

"""You can comment out this much part because we dont want to train our data
again and again
P.S. we will put this in for loop and save the file which has the highest accuracy
STARTING from here----------- """

# while True:
#     x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x,y, test_size= 0.1)
    
#     # linear is the name of our model, we can save it for future use
#     linear = linear_model.LinearRegression()
#     linear.fit(x_train, y_train)
#     accuracy = linear.score(x_test, y_test)
    
#     if accuracy > 0.97:
#         print(accuracy)
#         # Saving the model
#         with open("student.bin", "wb") as f:
#             pickle.dump(linear, f)
#         break

"""TILL HERE-------------- """

#loading the model
linear = pickle.load(open("student.bin", "rb"))

predictions = linear.predict(x_test)

for i in range(len(predictions)):
    print("Computer's prediction: ", int(predictions[i]) , "Real prediction: ", y_test[i])


#This part is only for showing pyplot

p = "studytime"
style.use("ggplot")
pyplot.scatter(data[p], data["G3"])
pyplot.xlabel(p)
pyplot.ylabel("Final grades")
pyplot.show()







