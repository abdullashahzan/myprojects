import calendar as c

inbut = input("Enter the year, month(optional): ")
inbut = inbut.split(",")

print("---------------------x---------------------\n")

if len(inbut) == 2:
    inbut.append('')

    if inbut[0] != "" and inbut[1] != '':
        print(c.month(int(inbut[0]), int(inbut[1])))

elif inbut[0] != "":
    print(c.calendar(int(inbut[0])))

else:
    print("You cant leave input empty!")