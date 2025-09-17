names = ["w@$im", "Sha!kh", "SD#T", "Engin**r"]

pos = {}
for i in range(len(names)):
    for j in range(len(names[i])):
        if names[i][j].isalpha() != True:
            pos.setdefault(i+1, []).append(j+1)
print(pos)


pos2 = {}
numbers = ["12999&9945", "12999%9945", "1299999*45"]
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        if numbers[i][j].isdigit() != True:
            pos2.setdefault(i+1, []).append(j+1)
print(pos2)
