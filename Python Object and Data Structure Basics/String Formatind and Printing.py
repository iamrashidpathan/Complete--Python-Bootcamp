# .format()
print("This is a string {}".format("dot format"))

#  indexing with .format()
print("The {2} {1} {0}".format('fox', 'brown', 'quick'))  # index starts from zero

#  .format() with keys
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

# float format {value:width.precision f}
result = 100 / 77
print(result)
print("The result was {r:1.3f}".format(r=result))


#  f string
name = "Rashid"
age = 24
print(f"Hello, My name is {name}. I am {age} years old")
