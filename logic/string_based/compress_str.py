# Compress a string (e.g., "aaabbc" → "a3b2c1").


def compress_string(s):
    arr = []
    counter = 1
    current_char = s[0]
    for i in range(1, len(s)):
        if s[i] == current_char:
            counter +=1
        else:
            arr.append(current_char+str(counter))
            counter = 1
            current_char = s[i]
    # append last character with char count
    arr.append(current_char + str(counter))
    return "".join(arr)


s = "aaabbcacb"
print(compress_string(s))







