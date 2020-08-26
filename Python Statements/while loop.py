x = 0
while x < 5:
    print(f'The current value of x is {x}')
    x += 1
else:
    print('X IS NOT LESS THANK 5')

print()  # leaving a line

# break, continue and pass
# break - breaks out of current closest loop
# continue - goes to the top of the closest enclosing loop
# pass - does nothing at all

x = [1, 2, 3]

for item in x:
    # comment
    pass
print('End of script')

print()  # leaving a line

my_string = "Jimmy"
for letter in my_string:
    if letter == "i":
        continue
    print(letter)

print()  # changing the line

for letter in my_string:
    if letter == "i":
        break
    print(letter)

print()

x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1


