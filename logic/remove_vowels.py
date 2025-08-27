# Remove all vowels from a string. -

str = "Remove all vowels from a string"
consonants = []
vowels = ["a", "e", "i", "o", "u"]
for i in str:
    if i not in vowels:
        # print(i, end="")
        consonants.append(i)
print("".join(consonants))