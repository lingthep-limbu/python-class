#**kwargs-> it builds a dictionary of key/value pairs
def my_function(**kwargs):
    if 'fruit' in kwargs:
        print(f"my favourite fruit is {kwargs['fruit']}")

    else:
        print("don't like that fruit")
        
my_function(fruit='apple')