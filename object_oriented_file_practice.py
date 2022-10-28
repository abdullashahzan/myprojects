class zoo:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def intro(self):
        print(f"i am {self.name} and i am {self.age} years old")
    def speak(self):
        print("I cant speak yet")

class cow(zoo):
    def speak(self):
        print("Moo")

class crow(zoo):
    def speak(self):
        print("Kaw Kaw")
        
        
a = zoo("Hen", 2)
a.intro()
a.speak()

b = cow("Cow", 35)
b.intro()
b.speak()

c = crow("Crow", 3)
c.intro()
c.speak()