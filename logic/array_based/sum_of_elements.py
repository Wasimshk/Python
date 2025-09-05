# Find the sum of elements in a list without using sum().
from functools import reduce

arr = [0, 1, 10, 13, 2, 3, 0, 4, 0, 5]
# solution 1
sum_arr = reduce(lambda a, b: a+b, arr)
print(sum_arr)

# solution 2
sum_arr1 = arr[0]
for i in range(1, len(arr)):
    sum_arr1 = sum_arr1 + arr[i]
print(sum_arr1)