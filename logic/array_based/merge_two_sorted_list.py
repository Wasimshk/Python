# Merge two sorted lists into one sorted list (without built-in sorting).

l1 = [1, 3, 5, 6, 2, 4]
l2 = [0, 2, 5, 8, 4, 11, 1]

max = max(l1+l2)
d = {}
l3 = []
for num in (l1+l2):
    d[num] = d.get(num, 0) + 1

for i in range(max+1):
    if i in d:
        while d[i] >= 1:
            l3.append(i)
            d[i] -= 1
print(l3)

