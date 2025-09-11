# Find elements present either in set1 or in set2, but not in both
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

symmetric_diff = {n for n in set1 if n not in set2}
for n in set2:
    if n not in set1:
        symmetric_diff.add(n)

print(symmetric_diff)

# Symmetric difference → items in either set1 or set2, but not in both
print("Symmetric difference: ", set1 ^ set2)

# this is more efficiant
symmetric_diff2 = set1.copy()
for n in set2:
    if n not in symmetric_diff2:
        symmetric_diff2.add(n)
    elif n in symmetric_diff2:
        symmetric_diff2.discard(n)
print(symmetric_diff2)