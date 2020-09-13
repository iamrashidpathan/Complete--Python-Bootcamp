def my_func(a, b):
    # return 5% of the sum of a and b
    return sum((a, b)) * 0.05


print(my_func(40, 60))

# in above code number of arguments passed to function is limited.

# Using *args


def my_func(*args):  # *args builds a tuple of all the value passed
    return sum(args) * 0.05


print(my_func(40, 60, 100, 1))

# using **kwargs


def my_func(**kwargs):
    if 'fruit' in kwargs:  # **kwargs builds a dictionary
        print("My fruit of choice is {}", format(kwargs['fruit']))
    else:
        print("I did not find any fruit here")


my_func(fruit='apple', veggie='lettuce')


def my_func(*args, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['food']))


my_func(1, 2, 3, fruit='orange', animal='dog', food='burger')
