my_file = open('test.txt')
print(my_file.read())
my_file.seek(0)
print(my_file.read())
my_file.seek(0)
contents = my_file.read()
print(contents)

my_file.seek(0)
contents_list = my_file.readlines()
print(contents_list)
my_file.close()

with open('test.txt') as my_file:
    contents = my_file.read()
print(contents)

with open('test.txt', mode='r') as my_file:
    print(my_file.read())

with open('test.txt', mode='a') as f:
    f.write("\nFour on fourth")

with open('test.txt', mode='r') as my_file:
    print(my_file.read())

with open('new_test.txt', mode='w') as f:
    f.write('I created this file')

with open('new_test.txt', mode='r') as file:
    print(file.read())

