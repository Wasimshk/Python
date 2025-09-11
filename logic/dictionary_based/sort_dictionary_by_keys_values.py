# Sort a dictionary by its keys.
# Sort a dictionary by its values.

d = {'name': 'Wasim', 'Age': 29, 'Qualification': 'Engineering', 'Role': 'SDET'}

# by default looping will print keys
keys = [key for key in d]
print(keys)

# using values() method will print values
values = [value for value in d.values()]
print(values)

# without using values() method
values = [d[key] for key in d]
print(values)

# creating dictionary from key and value lists using zip() and dict constructor
d2 = dict(zip(keys, values))
print(d2)







