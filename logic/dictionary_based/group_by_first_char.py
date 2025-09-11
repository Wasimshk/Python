# Write a program to group words by their first letter into a dictionary.
words = ["apple", "banana", "apricot", "blueberry", "cherry", "avocado"]

d ={}
for word in words:
    d.setdefault(word[0], []).append(word)
print(d)

d1 = {}

for word in words:
    if word[0] not in d1:
        d1[word[0]] = [word]
    else:
        d1[word[0]].append(word)
print(d1)