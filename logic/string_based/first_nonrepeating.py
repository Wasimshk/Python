# Find the first non-repeating character in a string.
from itertools import count

def firstUniqueChar(str):

    lower_str = str.lower()
    count = {}

    for ch in lower_str:
        count[ch] = count.get(ch, 0) + 1
    for ch in lower_str:
        if count[ch] == 1:
            return f"'{ch}' is the first unique character of the string"

print(firstUniqueChar("Find the first non-repeating character in a string."))