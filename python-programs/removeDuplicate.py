arr = [2, 2, 4, 5, 6, 7, 5, 5]
for num in arr:
    if arr.count(num) > 1:
        arr.remove(num)

print(arr)

