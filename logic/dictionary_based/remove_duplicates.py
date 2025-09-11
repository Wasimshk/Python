# Remove duplicates from a list using a dict

arr = [2, 4, 2, 5, 6, 7, 7, 8, 5, 9, 5]
d = dict.fromkeys(arr)

print(d.keys())
print(list(d))

