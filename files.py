my_file=open('test.txt')
print(my_file)
print(my_file.read())
print(my_file.read())
print(my_file.seek(0))
print(my_file.read())

#readlines return a list of the lines in the file
my_file.seek(0)
print(my_file.readlines())

# \n -> next line
my_file.close()

#writing to a file
# open() -> opening the file
# passing w+ let us read and write to the file
# open('test.txt', 'w+') -> this is ill truncates the original, meaning the anything that was before in original file is deleted
my_file= open('test.txt', 'w+')
print(my_file)

my_file.write('this is a new text')
my_file.seek(0)
print(my_file.read())

my_file.write('\nthis is another new line')
my_file.seek(0)
print(my_file.read())
my_file.close()

#appending to the file
newfile=open('hello.text', 'a+')
print(newfile)
newfile.write('this file is added from append methon')
newfile.write('\nthis is a new line')
newfile.seek(0)
print(newfile.read())

#comparison operator

#logical operator
