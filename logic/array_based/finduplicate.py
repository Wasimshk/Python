# Find duplicates in a list without using set().

arr = [2, 4, 2, 5, 6, 7, 7, 8, 5, 9, 5]
dup_dict = {}
# for num in arr:
    # if num not in duplicate:
    #     duplicate[num] = 1
    # else:
    #     duplicate[num] += 1

for num in arr:
    # single line is equivalent to above 4 lines
    dup_dict[num] = dup_dict.get(num, 0) + 1
print(dup_dict)

duplicates = [key for key, value in dup_dict.items() if value > 1]
print(duplicates)

