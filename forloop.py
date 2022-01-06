list1=[1,3,4,6,7,8,9,10,11,12,13,15]
# for num in list1:
#     print(num)

#print only even number
for num in list1:
    if num % 2 == 0:
        print(num)
    else:
        print('odd number')
#sum of all
sum=0
for num in list1:
    sum=sum+num
    print('the total sum is %d' %sum)

#string
for letters in 'this is  dursikshya':
    print(letters)

#tuple
t=(10,15,12,16,17)
for number in t:
    print(number)
