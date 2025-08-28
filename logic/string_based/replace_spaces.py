# "Replace all spaces in a string with - (without using .replace())."
str = "Replace all spaces in a string with"
l = str.split()
str2 = "-".join(l)
print(str2)

# for ch in str:
#     if ch == " ":
#         ch = "-"
#     print(ch, end="")