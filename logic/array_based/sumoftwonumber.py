arr = [2, 3, 4, 5, 7, 8, 1]

# sum of two numbers should be 9 and output should be in tuple format
target = 9  

for i in arr:
    for j in arr:
        if i + j == target:
            print((i, j))
            arr.remove(i)


# better approach
arr = [2, 3, 4, 5, 7, 8, 1]
target = 9
result = []

for i in range(len(arr)):
    for j in range(i+1, len(arr)):  # ensures no repeat
        if arr[i] + arr[j] == target:
            result.append((arr[i], arr[j]))

print(result)
# [(2, 7), (3, 6), (4, 5), ...]