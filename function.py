# function -> a block of code to perform a particular task. A function is reusable
# a function is always define usong def keywprds
# calling a function with this ()

#define the function
def demo():
    print('hello world')
#call the function
demo()

#accepting parameters or an arguments
#define the function
def people_name(name):
    # print('hello' +name)
    print(f'hello {name}')
#call the function with paramaters
people_name('Raghu')

#return type
#define
def add(x,y):
    return x+y

#call the function
abc=add(5,2)
print(abc)
