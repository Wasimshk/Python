# Remove all keys from a dictionary with values less than 10.
marks = {"wasim": 7, "azim": 9, "obaid": 6, "irshad": 15, "anup": 17, "wajid": 13, "aditya": 19 }

# create new dict
passed = {s:m for s, m in marks.items() if m >= 10}

# inplace removal, remove from existing dict
marks = {s:m for s, m in marks.items() if m >= 10}


# for s, m in marks.items():
#     if marks[s] >= 10:
#         passed[s] = m

print(passed)
print(marks)

