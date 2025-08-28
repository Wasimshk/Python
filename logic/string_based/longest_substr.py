str = "Find the longest word in a given sentence"

l = str.split()
templongest = 0
longestWord = None
for word in l:
    if len(word) > templongest:
        templongest = len(word)
        longestWord = word
print(longestWord)
