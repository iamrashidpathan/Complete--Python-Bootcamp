# Map


def square(num):
    return num**2


my_nums = [1, 2, 3, 4, 5]

for item in map(square, my_nums):
    print(item)

my_list = list(map(square, my_nums))
print(my_list)


def splicer(my_string):
    if len(my_string) % 2 == 0:
        return 'EVEN'
    else:
        return my_string[0]


names = ['Andy', 'Eve', 'Sally']

my_st_list = list(map(splicer, names))
print(my_st_list)

# Filter


def check_even(num):
    return num % 2 == 0


my_nums = [1, 2, 3, 4, 5, 6]

even = list(filter(check_even, my_nums))
print(even)

# Lambda

square = lambda num: num ** 2
print(square(3))

my_list = list(map(lambda num: num**2, my_nums))

print(my_list)

even_list = list(filter(lambda num: num % 2 == 0, my_nums))
print(even_list)
