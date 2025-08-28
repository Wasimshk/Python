# Reverse a list without using reverse() or slicing.

arr = [2, 2, 4, 5, 6, 7, 5, 5]
reversed_arr = []
l = len(arr)
for i in range(len(arr)):
    reversed_arr.append(arr[l-1])
    l -= 1

print(reversed_arr)


# In-place reversal (no extra list, O(1) space):

# left, right = 0, len(arr)-1
left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print(arr)