#list means in sequence and they are mutuable(changeable)

my_list=[1, 6, 9, 35, 49]
print(my_list)
print(my_list[0:3])
print(my_list[2:])

#use append method to add item in list
my_list.append('hello')
print(my_list)

#use pop to remove item from the list pop by default delets the last item
my_list.pop()
print(my_list)

#use indexing to remove items from any position
my_list.pop(1)
print(my_list)

#sort ->ascending
my_list.sort()
print(my_list)

#reverse
my_list.reverse()
print(my_list)

my_text=['hello', 'moring', 'afternoon', 'welcome', 'hy']
my_text.sort()
print(my_text)

#nested list -> list inside list
list1=[4,8,12]
list2=[5,10,15]
list3=[2,4,6]
final_list=[list1, list2, list3]
print(final_list)


print(final_list[0])

print(final_list[0][1])


