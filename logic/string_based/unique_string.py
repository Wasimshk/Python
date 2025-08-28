

str = input("Enter a string: ")
l = []

for i in range(len(str)):
    l.append(str[i])

s = set(l)

print(True if len(s)==len(l) else False)