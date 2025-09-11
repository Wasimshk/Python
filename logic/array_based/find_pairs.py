# Find pairs in a list that sum up to a target number.
# sum of two numbers should be 9 and output should be in tuple format

arr = [2, 3, 4, 5, 7, 8, 1]
target = 9
pairs = []
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i]+arr[j] == target:
            pairs.append((arr[i], arr[j]))
print(pairs)