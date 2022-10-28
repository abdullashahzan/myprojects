import random, json, pickle, nltk
import numpy as np
from nltk.stem import WordNetLemmatizer as wnl
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

lemmatizer = wnl()
file = "memory.json"
a = json.loads(open(file).read())

words, classes, documents, ignore_letters = [], [], [], ['?', ".", "!", ","]

for i in a['intents']:
    for j in i['patterns']:
        a = j.replace(" ", "#")
        b = ''.join(e for e in a if e.isalnum() or e == "#").replace("#", " ")
        word_list = nltk.word_tokenize(b)
        words.extend(word_list)
        documents.append((word_list, i['tag']))
        if i['tag'] not in classes:
            classes.append(i['tag'])

"""
Notes:
Documents = [ (['hello', 'how', 'are', 'you'], greetings), (['bye', 'bye'], goodbye) ]
Documents contain list of tuples which contain the sentence in the form of list and its tag

classes = ['greetings', 'goodbye', 'health']
Classes contain all the tags which are saved in the json file
"""

words = [lemmatizer.lemmatize(aaa.lower()) for aaa in words]
words = sorted(set(words))
classes = sorted(set(classes))

pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

training, output_empty = [], [0] * len(classes)

for k in documents:
    bag = []
    questions = k[0]
    questions = [lemmatizer.lemmatize(kkk.lower()) for kkk in questions]
    for l in words:
        if l in questions:
            bag.append(1)
        else:
            bag.append(0)
    
    output_row = list(output_empty)
    output_row[classes.index(k[1])] = 1
    training.append([bag, output_row])

random.shuffle(training)
training = np.array(training)

train_x = list(training[:, 0])
train_y = list(training[:, 1])
print(train_x[0])

#Neural networks start from here

model = Sequential()
model.add(Dense(256, input_shape = (len(train_x[0]),), activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(128, activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation = 'softmax'))

sgd = SGD(lr = 0.01, decay = 1e-6, momentum=0.9, nesterov=True)
model.compile(loss = 'categorical_crossentropy', optimizer = sgd, metrics=['accuracy'])
hist =  model.fit(np.array(train_x), np.array(train_y), epochs = 2000, batch_size= 10, verbose=1)
model.save('rem.h5', hist)

print("Code executed successfully")