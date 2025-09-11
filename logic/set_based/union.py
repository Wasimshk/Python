# find elements present in both sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

union = set1.copy()
for n in set2:
    union.add(n)
print(union)

# Union of set1 and set2 → all items from both sets
print("Union: ", set1 | set2)