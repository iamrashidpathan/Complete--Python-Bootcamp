
my_list = [1, 2, 3]
print(my_list)

my_list = ['STRING', 100, 23.2]
print(my_list)

length = len(my_list)
print(length)

# indexing and slicing
my_list = ['one', 'two', 'three']
print(my_list[0])
print(my_list[1:])

# concatenate
another_list = ['four', 'five']
full_list = my_list + another_list
print(full_list)

# changing items
full_list[0] = 'ONE ALL CAPS'
print(full_list)

# append helps to add a new item to a list
full_list.append('six')
print(full_list)

# removing items from a list
pop_out = full_list.pop()
print(full_list)
print(pop_out)
pop_two = full_list.pop(1)
print(pop_two)
print(full_list)

# sorting list
alp_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4, 1, 8, 3]
alp_list.sort()
print(alp_list)
num_list.reverse()
print(num_list)
num_list.sort()
print(num_list)
