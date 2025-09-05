"""
Time Complexity:
how many operations(steps) a program takes with respect to the input size


O(1)       Constant time      Access by index
O(logn)    logarithmic time   Binary search
O(n)       linear time        Loop through list
O(nlogn)   log-linear time    Merge sort/quicksort
O(n**2)    quadratic time     Nested loops
O(n**3)    polynomial time    double nested
O(2**n)    exponential time   Recursive Fibonacci
O(n!)      factorial time     Permutations

/////////////////////////////////////////////////////////////////////////////

Space Complexity:
how much extra memory (RAM) a program takes apart from inputs.


O(1)	    Constant Space          Few variables, iterative loops
O(log n)    logarithmic space   	Recursive binary search, quicksort stack
O(n)	    linear space            Extra array, hash map, recursion stack
O(n²)	    quadratic space         2D DP tables, adjacency matrices
O(n!)	    factorial space         Storing all permutations

"""

# Time Complexity

# O(1) → Constant time
# Doesn’t depend on input size.
arr = [10, 20, 30, 40, 50]
print(arr[3])   # Direct index access


# O(log n) → Logarithmic time
# Divide input in half each step (like binary search).
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

# O(n) → Linear time
# Grows linearly with input size.
for x in arr:
    print(x)

# O(n log n) → Linearithmic time
# Common in sorting algorithms (merge sort, quicksort, Timsort).
arr.sort()  # Python’s built-in sort (Timsort)

# O(n²) → Quadratic time
# Two nested loops.
for i in arr:
    for j in arr:
        print(i, j)

# O(2ⁿ) → Exponential time
# Grows extremely fast, common in brute-force recursion.
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# O(n!) → Factorial time
# Worst-case, like generating all permutations.
import itertools
arr = [1, 2, 3, 4]
for perm in itertools.permutations(arr):
    print(perm)



# ///////////////////////////////////////////////////////////
# space Complexity

# O(1) → Constant space
#
# Uses a fixed number of variables, no matter how big the input.

arr = [1,2,3,4,5]
total = 0
for x in arr:
    total += x   # Only "total" variable


# O(n) → Linear space
# Memory grows directly with input size.
arr = [1,2,3,4,5]
new_arr = [x*2 for x in arr]  # Creates another array of same size

# O(n²) → Quadratic space
# When you build a 2D structure.
n = 5
matrix = [[0]*n for _ in range(n)]

# O(n!) → Factorial space
# Rare, but happens if you store all permutations.
import itertools
arr = [1,2,3]
all_perms = list(itertools.permutations(arr))