my_string = "Hello"
my_list = []
for letter in my_string:
    my_list.append(letter)
print(my_list)

print()  # leaving a line

my_list = [l for l in my_string]
print(my_list)

print()  # leaving a line

my_list = [x for x in 'jimmy']
print(my_list)

print()  # leaving a line

my_list = [num for num in range(0, 11)]
print(my_list)

print()  # leaving a line

my_list = [num**2 for num in range(0, 11)]
print(my_list)

print()  # leaving a line

my_list = [num for num in range(0, 11) if num % 2 == 0]
print(my_list)

print()  # leaving a line

celsius = [0, 10, 20, 34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celsius]
print(fahrenheit)

print()  # leaving a line
# using else with list comprehension. advised to avoid using it
result = [x if x % 2 == 0 else 'ODD' for x in range(0, 11)]
print(result)

print()  # leaving a line

# nested loops
my_list = []
for x in [2, 4, 6]:
    for y in [1, 10, 100]:
        my_list.append(x*y)
print(my_list)

print()  # leaving a line

my_list = [x * y for x in [2, 4, 6] for y in [1, 10, 100]]
print(my_list)
