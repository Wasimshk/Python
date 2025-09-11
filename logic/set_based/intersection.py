# Find common elements between two sets without using &
# its called intersection
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
common = {n for n in set1 if n in set2}
print(common)

# using &
# Intersection → items present in both sets
print("Intersection: ", set1 & set2)


