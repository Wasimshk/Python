# Reverse each word in a string (e.g., "hello world" → "olleh dlrow").

str = "hello world"
l = str.split()

for word in l:
    print(word[::-1], end=" ")