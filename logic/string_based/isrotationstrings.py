# Check if a string is a rotation of another (e.g., "abcde", "cdeab").

def is_rotation_string(s1, s2):
    # if s1 == s2:
    #     return True
    # else:
    #     l = len(s1)
    #     for n in range(l):
    #         # it rotates each char and check if it matches with other string
    #         if (s1[n+1:] + s1[:n+1]) == s2:
    #             return True
    #     return False

    # the best and famous trick is, If s2 is a rotation of s1, then s2 must be a substring of s1+s1.
    if len(s1) != len(s2):
        return False
    return s2 in (s1+s1)

print(is_rotation_string("abcde", "cdeab"))
print(is_rotation_string("abcd", "cdab"))
print(is_rotation_string("aab", "aba"))
print(is_rotation_string("abcd", "acbd"))
