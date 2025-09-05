# Move all zeroes to the end of the list (maintaining order).

# best approach Time: O(n), Space: O(1).
arr = [0, 1, 10, 13, 2, 3, 0, 4, 0, 5]
pos = 0
for num in arr:
    if num != 0:
        arr[pos] = num
        pos += 1
while pos < len(arr):
    arr[pos] = 0
    pos += 1
print(arr)

# bad  approach Time: O(n²)
arr = [0, 1, 10, 13, 2, 3, 0, 4, 0, 5]
for i in range(len(arr)):
    if arr[i] == 0:
        arr.remove(0)  
        arr.append(0)
print(arr)


# good approach Time: O(n), Space: O(n)
arr2 = [0, 1, 10, 13, 2, 3, 0, 4, 0, 5]

zeros = 0
new_arr = []
for num in arr2:
    if num == 0:
        zeros += 1
    else:
        new_arr.append(num)

for i in range(zeros):
    new_arr.append(0)

print(new_arr)
