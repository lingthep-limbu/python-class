#**kwargs-> it builds a dictionary of key/value pairs
def my_function(**kwargs):
    if 'fruit' in kwargs:
        print(f"my favourite fruit is {kwargs['fruit']}")

    else:
        print("don't like that fruit")
        
my_function(fruit='apple')

# try except -> error handeling
# scope-> local scope and global scope

x=25 # global scope
def func():
    x=20 #-> local scope