import numpy as np

words = {"apple": ["appie", "appe", "appal"], "hello" : ["hell", "hallo", "helo"], "new york": ["new yrk", "nev york", "new yurk"]}
word = []
alist = []
index = 0

for i in words:
    alist.append(0)

def wordid(index):
    lst = []
    count = 0
    for i in alist:
        if count == index:
            lst.append(1)
        else:
            lst.append(0)
        count += 1
    return lst

for j in words:
    mainword = wordid(index)
    index += 1
    list1 = " ".join(j).split()
    clist = []
    for k in words[j]:
        blist = []
        list2 = " ".join(k).split()
        for l in list1:
            if l in list2:
                blist.append(1)
            else:
                blist.append(0)
        clist.append(blist)
    final = [mainword, clist]
    word.append(final)

train_x = []
train_y = []
scount = 0

for a in words:
    train_x.append(word[scount][0])
    train_y.append(word[scount][1])
    scount += 1
    





