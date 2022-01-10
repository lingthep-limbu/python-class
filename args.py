# *args-> when a function paaramater start with asterik, it allows for an arbitary number of arguments and functions takes them in a tuple of values

def my_function(*args):
    return sum(args)
x=my_function(20,30,50,60,70)
print(x)