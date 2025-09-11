# Invert a dictionary (keys become values and values become keys).

d = {'name': 'Wasim', 'Age': 29, 'Qualification': 'Engineering', 'Role': 'SDET'}

inverted_dict = {value:key for key, value in d.items()}
print(inverted_dict)
# there is an issue with the approach, when there are same values for unique keys
"""d = {"a": 1, "b": 2, "c": 1}
If we just do {v: k for k, v in d.items()}, then:
{1: 'c', 2: 'b'}   # key "a" is lost because value 1 was already used
"""

inverted = {}
# we will use setvalues() method instead
for k, v in d.items():
    inverted.setdefault(v, []).append(k) #this means if key(v) not present then create empty [] and append value(k), if key is present then, directly append to existing list
print(inverted)

