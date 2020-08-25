#  indentation are very important for Python statements

a = 5
b = 3
if a > b:
    print(f"{a} is bigger")
else:
    print(f"{b} is bigger")

if True:
    print("ITS TRUE")

if 3 > 2:
    print("ITS TRUE")

hungry = True
if hungry:
    print("FEED ME!")
else:
    print("I am not hungry")

loc = 'Bank'

if loc == 'Auto Shop':
    print("Cars are cool")
elif loc == "Bank":
    print("Money is cool")
elif loc == "Store":
    print("Welcome to the store")
else:
    print("I do not know much")

name = "Sammy"
if name == "Frankie":
    print("Hello Frankie!")
elif name == "Sammy":
    print("Hello Sammy!")
else:
    print("What is your name?")
