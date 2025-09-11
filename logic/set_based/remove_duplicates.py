# Remove duplicates from a list using a set (without using set() directly in one line).

arr = [2, 4, 2, 5, 6, 7, 7, 8, 5, 9, 5]
s = set()
for n in arr:
    s.add(n)
print(list(s))

# without using below
# print(set(arr))

print(dict.fromkeys(arr))

