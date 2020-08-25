my_iterable = [1, 2, 3]
for i in my_iterable:
    print(i)

print()  # leaving a line

# list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in my_list:
    print(num)

print()  # leaving a line

for num in my_list:
    # Check for even
    if num % 2 == 0:
        print(num)
    else:
        print(f"Odd Number {num}")

print()  # leaving a line

list_sum = 0
for num in my_list:
    list_sum = list_sum + num
print(list_sum)

print()  # leaving a line

for letter in "Hello World!":
    print(letter)

print()  # leaving a line

# tuple
tup = (1, 2, 3)
for item in tup:
    print(item)

print()  # laving a line

my_list = [(1, 2), (3, 4), (5, 6), (7, 8)]
print(len(my_list))
print()  # leaving a line
for item in my_list:
    print(item)
print()  # leaving a line
for (a, b) in my_list:  # tuple unpacking
    print(a)
    print(b)

print()  # leaving a line

d = {'k1': 1, 'k2': 2, 'k3': 3}
for item in d:
    print(item)
print()  # leaving a line
for item in d.items():
    print(item)
print()  # leaving a line
for (key, value) in d.items():
    print(value)
