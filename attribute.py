# attribute is the characteristic or propoerties of an object

# the syantx for creating attribute is 
# self.attribute= something
#there is a special method called
# __init__()

class Dog:
    #class object attribute
    species='mammals'

    def __init__(self, breed): #self is used to define the characteristic inside the object and its must to use 
        self.breed =breed #self.breed ie instead of breed any name can be called...eg self.mybreed..but recomended is to keep the same name
        
a= Dog(breed='Pitbull')
print(a.breed)
b=Dog(breed='shepherd')
print(b.breed)
print(a.species)