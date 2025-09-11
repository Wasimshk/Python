# Remove all occurrences of a given element from a list.

arr  = [5, 7, 34, 1, 4, 9, 2, 5, 7, 2, 5, 12, 5, 2, 5]
n = int(input("Enter a number to remove from the list: "))

# 
print(removed_occurrences := [num for num in arr if num != n])

# using filter function
filtered_list = list(filter(lambda x: x != n, arr))
print(filtered_list)