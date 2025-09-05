from jinja2.utils import missing
# arr = []
# l = int(input("Enter total number of list: "))
#
# for i in range(l):
#     arr.append(i)
# print(arr)
#
# del arr[5:l:9]
# print(arr)
# n = max(arr)
# missing_numbers = []
# for i in range(n):
#     if i not in arr:
#         missing_numbers.append(i)
#
# print(missing_numbers)

# arr = [0, 1, 2, 3, 5, 6, 8]
# n = max(arr)
#
# present = {}
# for num in arr:
#     present[num] = True
#
# missing_numbers = []
# for i in range(n+1):  # include n
#     if i not in present:
#         missing_numbers.append(i)
#
# print("Missing numbers:", missing_numbers)  # [4, 7]


arr = [0, 1, 2, 3, 5, 6, 8]
n = max(arr)

missing_numbers=[]
present = {}

for num in arr:
    present[num] = True

for i in range(n+1):
    if i not in present:
        missing_numbers.append(i)

print("Missing numbers:", missing_numbers)

