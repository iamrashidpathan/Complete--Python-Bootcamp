# def keyword
def name_of_function(name):
    """
    Docstring explains the function
    """
    print("Hello " + name)


name_of_function("Jimmy")


def say_hello(name="Default"):
    print(f"Hello {name}")


say_hello("Jimmy")


def add_num(num1, num2):
    return num1 + num2


result = add_num(10, 20)
print(result)


# Adding Logic to Internal Function Operations
def even_check(number):
    return number % 2 == 0


print(even_check(20))
print(even_check(21))

print()  # leaving a line


def check_even_list(num_list):
    even_number_list = [x for x in num_list if even_check(x)]
    print(even_number_list)
    for num in num_list:
        if even_check(num):  # calling the predefined even_check to check if the number is even
            print(f"{num} is even")
            return True
        else:
            pass
    return False


print(check_even_list([1, 2, 3, 5, 8, 7]))

print()  # leaving a line

# Returning Tuples for Unpacking
stock_prices = [('Apple', 200), ('GOOGLE', 400), ("MICROSOFT", 100)]
for item in stock_prices:
    print(item)

for ticker, price in stock_prices:
    print(ticker)

print()  # leaving a line
work_hours = [('Abby', 100), ('Billy', 400), ('Cassie', 800)]


def employee_check(work_hours):
    current_max = 0
    employee_of_the_month = ""
    for name, hours in work_hours:
        if hours > current_max:
            employee_of_the_month = name
            current_max = hours

    return employee_of_the_month, current_max


name, hours = (employee_check(work_hours))
print(name, hours)

print() # leaving a line
# interaction between function
from random import shuffle

example = [1, 3, 4, 7, 8, 2]


def shuffle_list(my_list):
    shuffle(my_list)
    return my_list


print(shuffle_list(example))
#  print(shuffle_list(my_list))


def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("pick a number 0, 1 or 2: ")
    return int(guess)


def check_guess(my_list, guess):
    if my_list[guess] == 'O':
        print("Correct!")
        return True
    else:
        print("Wrong guess!")
        print(my_list)


while (True):
    # Initial list
    my_list = [' ', 'O', ' ']

    # Shuffle list
    mixed_list = shuffle_list(my_list)

    # User guess
    user_index = player_guess()

    # Check guess
    check = check_guess(mixed_list, user_index)

    if check:
        break

