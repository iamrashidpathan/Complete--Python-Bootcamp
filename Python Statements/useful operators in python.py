# range(start, stop, step)
for num in range(0, 10, 2):
    print(num)

# list is a generator.it does not save the data. user has to save it manually
print(range(0, 10, 2))

print(list(range(0, 10, 2)))

print()  # leaving a line

index_count = 0
word = "abcde"
for letter in word:
    print("At index {} the letter is {}".format(index_count, letter))
    print(word[index_count])
    index_count += 1

print()  # leaving a line

# enumerate returns a tuple of index and value
# enumerate can take any kind of iterable object
for item in enumerate(word):
    print(item)

print()  # leaving a line

# we can use tuple unpacking as well
for index, value in enumerate(word):
    print(index)
    print(value)
    print()

# zip - zips together two lists, giving a tuple
my_list1 = [1, 2, 3, 4, 5, 6]
my_list2 = ['a', 'b', 'c', 'd', 'e', 'f']

for item in zip(my_list1, my_list2):
    print(item)


my_list3 = [100, 200, 300, 400, 500, 600]
print()  # leaving a line

for item in zip(my_list1, my_list2, my_list3):
    print(item)

print()  # leaving a line
print(list(zip(my_list1, my_list2)))

print(list([1, 2]))

print()  # leaving a line

# using in. it returns a boolean based on the condition
print('x' in [1, 2, 3])
print('x' in ['x', 'y', 'z'])
print(2 in [1, 2, 3])
print('j' in 'jimmy')
print('my_key' in {'my_key': 345, 'your_key': 321})
d = {'my_key': 345, 'your_key': 321}
print(345 in d.values())
print(345 in d.keys())
print('my_key' in d)

print()  # leaving a line

my_list = [10, 20, 30, 40, 100]
print(min(my_list))
print(max(my_list))

print()  # leaving a line

from random import shuffle
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffle(my_list)  # shuffle does not return anything. its an inplace function
print(my_list)

print()  # leaving a line
from random import randint
num = randint(1, 300)  # randint returns an integer so it can be stored
print(num)

print()  # leaving a line
# taking user input
# input function takes input as string. type casting has to be used
number = input("Enter a number:\n")
print(int(number) + 1)

