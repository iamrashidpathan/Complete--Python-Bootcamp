print('hello')
print("world")
print('this is also a string')
print("I'm going on a run")
print("hello \tworld")

print(len("I am hungry"))

# Indexing
my_string = "Hello World"
print(my_string)
print(my_string[0])
print(my_string[8])
print(my_string[9])
print(my_string[-2])

# Slicing
my_string = "abcdefghijk"
print(my_string)
print(my_string[2:])
print(my_string[:3])
print(my_string[3:6])
print(my_string[1:3])

# step size
print(my_string[::2])  # 2 is the step size
print(my_string[2:7:2])
print(my_string[::-1])

# Immutability
name = "Sam"
# name[0] = "P" this is not supported as strings are immutable.
print(name)

last_letters = name[1:]
# String concatenation
name = 'P'+last_letters
print(name)

x = 'Hello World'
x = x + " it is beautiful outside"
print(x)

# String multiplication
letter = 'z'
print(letter*10)

# Strings methods
x = 'Hello World'
print(x.upper())  # to uppercase
print(x)
print(x.lower())  # to lowercase
print(x.split())  # list of all words
x = "Hi this is a string"
print(x.split())
print(x.split('i'))
