arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]


squared = list(map(lambda x: x**2, arr))
floated = list(map(float, arr))
stringed = list(map(str, arr))

even = list(filter(lambda x: x % 2 == 0, arr))
odd = list(filter(lambda x: x % 2 != 0, arr))

print("Original array:", arr)
print("Squared array:", squared)
print("Floated array:", floated)
print("Stringed array:", stringed)
print("Even numbers:", even)
print("Odd numbers:", odd)
