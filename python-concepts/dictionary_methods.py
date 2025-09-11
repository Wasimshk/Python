# get(), get(key, default)
# it finds the key in dictionary if it finds the key then it will get the value if dont find then it will set the default value to the key
# example
d = {"name":"wasim"}

key = "name"
d[key] = d.get(key, None)
print(d) # {'name': 'wasim'}

key = "role"
print(d.get(key, None)) # None
d[key] = d.get(key, None) # set key "role" with None value
print(d) # {'name': 'wasim', 'role': None}

# use case

# count frequency of each char
str = "Count the frequency of words in a sentence using a dictionary."
freq = {}
for char in str:
    freq[char] = freq.get(char, 0) + 1
print(freq)

#/////////////////////////////////////////////////////////////////////////////////
# setdefault(), setdefault(key, default)
"""The setdefault() method in Python dictionaries is used to retrieve the value associated with a given key. 
If the key exists in the dictionary, it returns the corresponding value. 
If the key does not exist, setdefault() inserts the key into the dictionary with a specified default value and then returns that default value. """

d3 = {"name":"wasim"}
key = "name"
value = "shaikh"
d3.setdefault(key, value) # it returns the value "wasim" as it is present in the dict
print(d3) #o/p {'name': 'wasim'}

key1 = "Role"
value1 = "SDET"
d3.setdefault(key1, value1) # it sets the key1 "Role" and returns the value1 "SDET" as it is not present in the dict
print(d3) #o/p {'name': 'wasim', 'Role': 'SDET'}


# Use case
# group each word with first char
words = ["apple", "banana", "apricot", "blueberry", "cherry", "avocado"]
d ={}
for word in words:
    d.setdefault(word[0], []).append(word)
    # initializes the key with an empty list [] if it’s not already in the dictionary.
    # Then .append(word) adds the word to that list.
print(d) #o/p {'a': ['apple', 'apricot', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}

# invert a list
d = {"a": 1, "b": 2, "c": 1}
inverted = {}
for k, v in d.items():
    inverted.setdefault(v, []).append(k)

print(inverted)   # {1: ['a', 'c'], 2: ['b']}
