# Write a program to check if two strings are anagrams (without sorting).
from pycparser.c_ast import Return


def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    d1 = {}
    for ch in s1:
        # if ch not in d1:
        #     d1[ch] = 1
        # else:
        #     d1[ch] += 1
        d1[ch] = d1.get(ch, 0) + 1

    d2 = {}
    for ch in s2:
        # if ch not in d2:
        #     d2[ch] = 1
        # else:
        #     d2[ch] += 1
        d2[ch] = d2.get(ch, 0) + 1
    return d1 == d2

print(is_anagram("listen", "silent"))  # True
print(is_anagram("aabb", "baba"))      # True
print(is_anagram("aabb", "ab"))

