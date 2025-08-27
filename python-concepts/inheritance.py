class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("This is my sound: ", end="")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof! Woof!")

class Cat(Animal):
    def speak(self):
        super().speak()
        print("Meaww! Meaww!")

d = Dog("Bruno")
d.speak()

c = Cat("Nimmi")
c.speak()