# tuples are immutable

t =(1, 2, 3)
my_list = [1, 2, 3]
print(type(t))
print(type(my_list))

t = ('one', 2)
print(t[0])
print(t[-1])

t = ('a', 'a', 'b')
print(t.count('b'))
print(t.index('a'))  # first index
print(t.index('b'))

# immutable
print(t)
print(my_list)
my_list[0] = 'ONE'  # but tuples do not support assignment
print(my_list)


