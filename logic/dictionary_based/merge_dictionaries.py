# Merge two dictionaries manually (without using update()).

d1 = {"name":"Wasim", "Age": 29}
d2 = {"Qualification": "Engineering", "Role": "SDET", "name": "Shaikh"}

# using kwargs
def merge_dicts(**kwargs):
    return kwargs
# print(merge_dicts(**d1, **d2)) #this will through "TypeError, for multiple values for keyword argument 'name'"

# instead of using kwargs we can use unpacking dictionaries
merge1 = {**d1, **d2}
print(merge1)

# merge using dictionary merge (|) operator:
merge2 = d1 | d2 #Equivalent to unpacking
print(merge2)

# |= (in-place merge): d1 will be updated with d2
d1 |= d2 #This modifies d1 directly, similar to .update(), i.e d1.update(d2
print(d1)

# manual way with loop
merge = {}
for key, value in d1.items():
    merge[key] = value
for key, value in d2.items():
    merge[key] = value
print(merge)

