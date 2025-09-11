# The pipe symbol | has different meanings depending on context:

# Dictionaries → merge operator
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = d1 | d2
print(merged) # {'a': 1, 'b': 3, 'c': 4}

# Sets → union operator
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 | s2)   # {1, 2, 3, 4, 5}

# integers → Bitwise OR:
print(5 | 3)  # 7 (binary 101 | 011 = 111)


"""

So:
dict | dict = merge dictionaries
set | set = union of sets
int | int = bitwise OR

"""