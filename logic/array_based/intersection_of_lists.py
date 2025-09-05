# Find the intersection of two lists (without set).

list1 = [0, 1, 3, 5, 7, 9, 10, 0, 0, 12, 1]
list2 = [2, 4, 6, 8, 10, 12, 0]

d = {}
intersection = []
for num in list1:
    d[num] = 1

for num in list2:
    if num in d:
        intersection.append(num)
print(intersection)