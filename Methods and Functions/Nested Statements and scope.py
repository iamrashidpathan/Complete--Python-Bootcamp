x = 25


def printer():
    x = 50
    return x


print(x)
print(printer())
print(x)

# LEGB : Local, Enclosing function, Global, Built-in

name = "This is Global String"


def greet():
    name = "Jimmy"

    def hello():
        name = "I am Local String"
        print("Hello "+name)
    hello()


greet()
print(name)

