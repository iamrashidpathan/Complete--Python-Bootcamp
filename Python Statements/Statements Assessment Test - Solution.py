# Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s S in this sentence'
for word in st.split():
    if word[0] == 's' or word[0] == 'S':
        print(word)

print()  # leaving a line

# Use range() to print all the even numbers from 0 to 10.
for num in range(0, 11):
    if num % 2 == 0:
        print(num)
# or
for num in range(0, 11, 2):
    print(num)

print()  # leaving a line

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
div_3 = [x for x in range(1, 51) if x % 3 == 0]
print(div_3)

print()  # leaving a line

# Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word) % 2 == 0:
        print(f"{word} has even length")

print()  # leaving a line

# Write a program that prints the integers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number,
# and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

print()  # leaving a line

# Use List Comprehension to create a list of the
# first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
st_list = [word[0] for word in st.split()]
print(st_list)
