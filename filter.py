def check_even(num):
    return num%2==0

def greater_5(num):
    return num>5

nums=[0,1,2,3,4,5,6,7,8]
x=list(filter(check_even, nums))
print(x)

y=list(filter(greater_5,nums))
print(y)