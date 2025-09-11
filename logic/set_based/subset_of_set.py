# Check if a set is a subset of another set. -

set1 = {1, 2, 3, 4, 5, 6}
set2 = {7, 4, 5, 6}

def is_subset(set1, set2):
    arr = set()
    for n in set2:
        if n not in set1:
            arr.add(False)
        else:
            arr.add(True)
    return all(arr)

if len(set1) >= len(set2):
    print(is_subset(set1, set2))
else:
    print(is_subset(set2, set1))



set1 = {1, 2, 3, 4, 5, 6}
set2 = {1, 4, 5, 6}
u = set1 | set2
if len(set1) >= len(set2):
    if u == set1:
        print(True)
    else:
        print(False)
else:
    if u == set2:
        print(True)
    else:
        print(False)




