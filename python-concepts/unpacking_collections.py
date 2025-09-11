# ** → unpack dictionary
# * → unpack list, tuple, set, string



# Dictionary unpacking with **
# ** unpacks dictionaries into key-value pairs.
d1 = {"a": 1}
d2 = {"b": 2}
print({**d1, **d2})  # {'a': 1, 'b': 2}
# unpacking dictionary keys to set, tuple or list
print({*d1, *d2})  # {'b', 'a'}
print([*d1, *d2])  # ['a', 'b']
print((*d1, *d2))  # ('a', 'b')

# List / Tuple / Set unpacking with *
# * unpacks iterables (list, tuple, set, string, etc.).

# List
l1 = [1, 2, 3]
l2 = [4, 5]
print([*l1, *l2])   # [1, 2, 3, 4, 5]

# Tuple
t1 = (1, 2)
t2 = (3, 4)
print((*t1, *t2))   # (1, 2, 3, 4)

# Set
s1 = {1, 2}
s2 = {3, 4}
print({*s1, *s2})   # {1, 2, 3, 4}

# unpacking strings:
word1 = "Wasim"
word2 = "Shaikh"
print([*word1])   # ['W', 'a', 's', 'i', 'm']
print([*word1, *word2])   # ['W', 'a', 's', 'i', 'm', 'S', 'h', 'a', 'i', 'k', 'h']
# directly add - between each character
print("-".join([*word1]))

