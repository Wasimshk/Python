# Find elements present in one set but not in another.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

diff = {n for n in set1 if n not in set2}
print(diff)

# Difference → items in set1 but not in set2
print("Difference: ", set1 - set2)

# for n in set2:
#     if n in set1:
#         set1.discard(n)
# print(set1)