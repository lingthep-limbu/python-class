#similar to object from other programming language
# dict={'key1': 'value1'}

student={'name':'Bindu', 'age':20, 'height': 5.5, 'gender':'female'}
print(student['name'])
print(student['name'].upper())

student={'name':'Bindu', 'age':20, 'height': 5.5, 'gender':'female', 'subject':['Python', 'django','restapi','react','next']}

print(student['subject'])
print(student['subject'][0])

#nesting with dictionaries
x={'key1':{'nestkey':{'subnestkey':'values'}}}
print(x['key1']['nestkey']['subnestkey'])

#print all the keys
print(student.keys())

#print all the values
print(student.values())

print(student['age'])

#method to return tuples of all items
print(student.items())
