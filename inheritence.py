# inheritence is to form new classes from classes that have been already defined. the newly formed classes are called derived class, the class that we derive from are called baseclass. the derived class override or extend the functionality of base class

class Animal:

    def __init__(self):
        print('Animal class Created')

    def whoIs(self):
        print('Animal')

    def eat(self):
        print('Animal who Eats')

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog class Created')

    def whoIs(self):
        print('Dog')

    def bark(self):
        print('woof')

d=Dog()
print(d)
d.whoIs()
d.eat()