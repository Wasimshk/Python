# Check if two dictionaries are identical without using ==.

def isidentical(d1, d2):
    isItemsSame = []
    for k, v in d1.items():
        if k in d2 and v == d2[k]:
            isItemsSame.append(True)
        else:
            isItemsSame.append(False)
    return all(isItemsSame)

dict1 = {"name": "Wasim", "age": 29, "role": "SDET"}
dict2 = {"role": "SDET", "age": 29, "name": "Wasim"}  # Same keys and values but different order
dict3 = {"name": "Wasim", "age": 30, "role": "SDET"}  # Different value for 'age'

print(isidentical(dict1, dict2))
print(isidentical(dict1, dict3))