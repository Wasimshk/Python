"""Implement binary search on a sorted list
Binary Search is an efficient algorithm to find an element in a sorted list.
Instead of scanning one-by-one (like linear search), it cuts the search space in half every step.
note - binary search only works on sorted array and time complexity is O(logn)
if the array is not sorted then it's better to use linear search, because sorting + binary search will be O(nlogn) while linear search is O(n)"""


def bindary_search(arr, target):
    low, high = 0, len(arr)-1

    while low <= high:
        mid = (low + high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 5
print(bindary_search(arr, target))