# methods are function defined inside the body of the class. the are used to perform the operations with attributes of our objects. Methods are a key concept of OOP paradigm. for large applications methods are essential.

class Circle:
    pi=3.14

    #circle get instantiated with a radius (default 1)
    def __init__(self, radius=1):
        self.radius=radius
        self.area=radius*radius*Circle.pi

    #method for reseting radius
    def setRadius(self, new_radius):
        self.radius=new_radius
        self.area=new_radius*new_radius*self.pi

    #method for getting circumference
    def getCircumference(self):
        return 2*self.pi*self.radius

a=Circle()
a.setRadius(3)
print('radius is:', a.radius)
print('area is:',a.area)
print('circumference is:',a.getCircumference())


