# Count the frequency of words in a sentence using a dictionary.

str = "Count the frequency of words in a sentence using a dictionary."

freq = {}

for char in str:
    # # method 1
    # if char not in freq:
    #     freq[char] = 1
    # else:
    #     freq[char] += 1

    # method 2
    freq[char] = freq.get(char, 0) + 1

print(freq)