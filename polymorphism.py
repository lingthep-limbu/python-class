class Dog:
    def __init__(self, name):
        self.name=name

    def speak(self):
        return self.name + ' says woof'

class Cat:
    def __init__(self, name):
        self.name=name

    def speak(self):
        return self.name +' says mew'

a=Dog('shepherd')
b=Cat('garfield')

print(a.speak())
print(b.speak())
