#inheritance is to form new classes from classes that have been already defined. The newly formed classes are called derived class, the class that we derive are called base class.

class Animal:
    def __init__(self):
        print('Animal Class Created')

    def whoIs(self):
        print('Animal')

    def eat(self):
        print('Animal who eat')

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog Class Created')

    def whoIs(self):
        print('Dog')

    def bark(self):
        print('woof')

d=Dog()
print(d)
d.whoIs()
d.eat()