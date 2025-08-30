import re

text = "The quick brown fox jumps over the lazy dog."

# search for pattern
find = re.search("brown", text) #prints start and end indices of the first occurrence
print(find)
if find:
    print("Match found!")
    print("start index: ", find.start())
    print("end index", find.end())

# find all occurrences
print(findall:=re.findall("the", text, re.IGNORECASE))

# substitute
print(replace := re.sub("dog", "fox", text)) #replace all the occurrences

"""
O/P
<re.Match object; span=(10, 15), match='brown'>
Match found!
start index:  10
end index 15
['The', 'the']
The quick brown fox jumps over the lazy fox.
"""