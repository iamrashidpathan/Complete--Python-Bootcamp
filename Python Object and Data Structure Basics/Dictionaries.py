my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict)
print(my_dict['key1'])

price_lookup = {'apple': 2.99, 'oranges': 1.99, 'milk': 5.80}
print(price_lookup['apple'])

d = {'k1': 123, 'k2': [0, 1, 2], 'k3': {'insideKey': 100}}
print(d['k1']+1)
print(d['k2'][1])
print(d['k3']['insideKey'])

d = {'k1': ['a', 'b', 'c']}
my_list = d['k1']
letter = my_list[2]
print(letter)
print(letter.upper())
print(letter)

print(d)

# adding a new value
d = {'k1': 100, 'k2': 200}
print(d)
d['k3'] = 300
print(d)
d['k1'] = 'NEW VALUE'
print(d)

# dictionary methods
d = {'k1': 100, 'k2': 200, 'k3': 300}
print(d.keys())
print(d.values())
print(d.items())

di = {1: 'one', 2: 'two'}
print(di[1])
