# Ways to create a dictionary
# 1. Using Curly Braces {}
d = {'a': 1, 'b': 2, 'c': 3}
print(d)

# 2. Using dict() Constructor
d = dict(a=1, b=2, c=3)     # Keyword arguments
print(d)         
d = dict([('a', 1), ('b', 2)])     # From list of tuples
print(d)

# 3. From zip()
keys = ['a', 'b', 'c']
values = [1, 2, 3]
z = zip(keys, values)
print(list(z))  # [('a', 1), ('b', 2), ('c', 3)]
d = dict(zip(keys, values))
print(d)

# 4. Dictionary Comprehension
# new_dict = {key_expression: value_expression for item in iterable if condition}
d = {x: x**2 for x in range(1, 6)}
print(d)

# 5. From JSON String
import json
d = json.loads('{"a": 1, "b": 2, "c": 3}')
print(d)

# empty dictionary

dict1 = {}
dict1["Name"] = "Wasim"
dict1["Age"] = 29
print(dict1)


print("///////////////////////////////////////////////////////////////")
# In Python, a for loop can be used to iterate through a dictionary in several ways:

# Iterating through keys (default behavior): When a for loop is applied directly to a dictionary, it iterates over its keys by default.
my_dict = {"name": "Wasim", "age": 29, "city": "Pune"}
for key in my_dict:
    print(key)

# Iterating through values: The .values() method can be used to iterate directly over the values of a dictionary.
for value in my_dict.values():
    print(value)

# Iterating through key-value pairs: The .items() method returns key-value pairs as tuples, which can be unpacked directly within the for loop. This is a common and efficient way to access both keys and values simultaneously.

for key, value in my_dict.items():
    print(f"for the key-{key} the value is: {value}")

# Accessing values using keys during key iteration: If iterating through keys, the corresponding value can be accessed within the loop by using the key as an index.
for key in my_dict:
    value = my_dict[key]
    print(f"for the key-{key} the value is: {value}")

print("///////////////////////////////////////////////////////////////")

# Dictionary comprehention
# normal 
normal_dict = {x: x**2 for x in range(1, 10)}
print(normal_dict)
# Conditional
even_squares = {x: x**2 for x in range(1, 10) if x % 2 == 0}
print(even_squares)
# Creating a dictionary from an existing dictionary:
original_dict = {'a': 1, 'b': 2, 'c': 3}
new_dict = {key: value * 10 for key, value in original_dict.items()}
print(new_dict)