# Count the frequency of every character in a string (without Counter)
str = "dawdawhdagwjdh gahwdfawdfy giouawpok dalw"
d = {}
# d['a'] = d.get('a', 0) + 1

for i in str:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)