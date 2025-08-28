# Find the maximum and minimum number in a list without using max() or min().

arr = [2, 3, 4, 5, 9,1, 7, 8, 2]

# with sort
arr.sort()
print(f"min = {arr[0]}, max = {arr[-1]}")

# with loop
min = max = arr[0]
for i in arr:
    if i > max:
        max = i
    if i < min:
        min = i

print(f"min = {min}, max = {max}")