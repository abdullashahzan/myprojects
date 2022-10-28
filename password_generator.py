#Password generator

import random as r

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

while True:
    try:
        length = int(input("How many letters would you like in your password: "))
        if length == 0:
            print("The length of password cannot be zero")
        else:
            break
    except:
        print("Please enter a correct number")

while True:
    try:
        sym = int(input("How many symbols would you like in your password: "))
        break
    except:
        print("Please enter a correct number")

while True:
    try:
        num = int(input("How many numbers would you like in your password: "))
        break
    except:
        print("Please enter a correct number")

pas = ''

for i in range(length):
    pas += r.choice(letters)
for j in range(sym):
    pas += r.choice(symbols)
for k in range(num):
    pas += r.choice(numbers)

apas = " ".join(pas)
bpas = apas.split(" ")
r.shuffle(bpas)
password = "".join(bpas)

print(f"Your password is: {password}")
