s = "Write Python 3 code in this online editor and run it."
char_count = {}

for ch in s:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1
        
print(char_count)