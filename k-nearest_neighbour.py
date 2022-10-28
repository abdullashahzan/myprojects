import sklearn 
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import preprocessing

data = pd.read_csv("car.data")

"""Changing string values like vhigh, low, unacc etc into integers. Sklearn does that for us
through a function called preprocessing"""
pp = preprocessing.LabelEncoder()

buying = pp.fit_transform(list(data["buying"]))
maint = pp.fit_transform(list(data["maint"]))
door = pp.fit_transform(list(data["door"]))
persons = pp.fit_transform(list(data["persons"]))
lug = pp.fit_transform(list(data["lug_boot"]))
safety = pp.fit_transform(list(data["safety"]))
clss = pp.fit_transform(list(data["class"]))

predict = "class"

x = list(zip(buying, maint, door, persons, lug, safety, clss))
y = list(clss)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x,y, test_size=0.1)

model = KNeighborsClassifier(n_neighbors= 3)


model.fit(x_train, y_train)
acc = model.score(x_test, y_test)

predicted = model.predict(x_test)

names = ["unacc", "acc", "good", "vgood"]

for x in range(len(predicted)):
    print("Predicted: ", names[predicted[x]]) 
    print("Actual: ", names[y_test[x]])
    #This will show you the neighbours it found and their distance to the object!
    yo = model.kneighbors([x_test[x]], 9, True)
    #print("N: ", yo)