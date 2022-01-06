text='welcome to python world'
#string length
print(len(text))

#uppercase use upper
print(text.upper())

#lowercase use lower
print(text.lower())

#split()
print(text.split())

#formating  with placeholder for the use %s
print('this is a %s class.' %'python') 

#for multiple words
print('%s is mainly used for %s' %('python', 'machine learning'))

#indexing
print(text[0])
print(text[0:7])
print(text[:7])

#grab everything after index 5
print(text[5:])

#grab everything
print(text[:])