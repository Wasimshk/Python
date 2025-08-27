# Reverse a string without using slicing or [::-1]

str = "Reverse a string without using slicing"

l = len(str)
for i in range(l):
    print(str[(l-1)-i], end="")
