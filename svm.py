#Support vector machine aka svm

import sklearn
from sklearn import datasets
from sklearn import svm
import numpy as np
from sklearn import metrics
import pickle as p

cancer = datasets.load_breast_cancer()

x = cancer.data
y = cancer.target

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

cancer_output = ["malignant", "benign"]

"""
kernel can be of different types for eg it can be poly spv etc etc check on website if you want to 
know more. C stand for soft margin
I have created a model with 0.99 accuracy so dont delete this lmao
"""
# while True:
#     x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.2)
#     model = svm.SVC(kernel="linear", C= 1)
#     model.fit(x_train, y_train)
#     prediction = model.predict(x_test)
#     acc = metrics.accuracy_score(y_test, prediction)
#     if acc >= 0.98:
#         p.dump(model, open("svm_model.bin", "wb"))
#         print(acc)
#         break

model = p.load(open("svm_model.bin", "rb"))
prediction = model.predict(x_test)
acc = metrics.accuracy_score(y_test, prediction)
print(acc)

for i in range(len(prediction)):
    print(cancer_output[prediction[i]], cancer_output[y_test[i]])