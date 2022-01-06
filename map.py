#the map function allows you to  'map' a function to an iterable object. This means you can call the same function to every time to every item in an iterable such as list.
def square(num):
    return num**2
my_num=[1,2,3,4,5]
a=map(square, my_num)
print(a)

x=list(map(square, my_num))
print(x)

mynames=['ramesh','raghu','sudip','ashim','spriha','bindu','gaurav','sanjay','sanjeev']
def splicer(mytext):
    if len(mytext)%2==0:
        return 'even'
    else:
        return mytext[0]

#mytext is a argument given for myames

abc=list(map(splicer,mynames))
print(abc)