arr = [1, 2, 3, 4, 5]
# list comprehension
print([a**2 for a in arr])

# similar basic for loop
l = []
for a in arr:
    l.append(a**2)
print(l)