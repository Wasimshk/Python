# Separate even and odd numbers from a list. -

arr  = [5, 7, 34, 1, 4, 9, 2, 5, 7, 2, 5, 12, 5, 2, 5]

even = [n for n in arr if n%2==0]
odd = [n for n in arr if n%2==1]

print("Even: ", even, "\nOdd: ", odd)