# Find the union of multiple sets manually.

sets = [{1, 2, 3}, {3, 4, 5}, {5, 6, 7}, {1, 7, 8}]
unions = set()
for s in sets:
     unions.update(s)
print(unions)
