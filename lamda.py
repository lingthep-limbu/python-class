def square(num):
    return num**2

x=square(3)
print(x)


square=lambda num: num**2
y= square(5)
print(y)


my_nums=[0,1,2,3,4,5,6,7,8,9,10]
filter_data=list(filter(lambda nume: nume%2==0, my_nums))

print(filter_data)


