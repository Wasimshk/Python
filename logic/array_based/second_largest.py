# Find the second largest number in a list without sorting.


arr  = [5, 7, 34, 1, 4, 9, 27, 25, 12]

largest = sec_largest = 0

for num in arr:
    if largest < num:
        sec_largest = largest
        largest = num
    elif sec_largest < num and sec_largest != largest:
        sec_largest = num

print(largest)
print(sec_largest)

