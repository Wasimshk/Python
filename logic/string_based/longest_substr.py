str = "Find the longest word in a given sentence"

l = str.split()
longestWord = l[0]
for word in l:
    if len(word) > len(longestWord):
        longestWord = word
print(longestWord)
