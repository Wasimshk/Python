# Compress a string (e.g., "aaabbc" → "a3b2c1").
str = "aaabbca"
arr =[]
for i in str:
    if str.count(i) > 1 and i not in arr:
        arr.append(i)
        arr.append(str.count(i)-1)
    elif str.count(i) == 1:
        arr.append(i)
print(arr)



