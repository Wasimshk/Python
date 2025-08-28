arr = [2, 2, 4, 5, 6, 7, 5, 5]

# without using set
for i in arr:
    if arr.count(i) > 1:
        arr.remove(i)
print(arr)

# # using set:
# s = set(arr)
# print(s)

