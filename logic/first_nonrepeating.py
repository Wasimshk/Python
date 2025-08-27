# Find the first non-repeating character in a string.
from itertools import count

str = "Find the first non-repeating character in a string."

for i in str:
    if str.lower().count(i) == 1:
        print("this is the first non repeating character: ", i)
        break
