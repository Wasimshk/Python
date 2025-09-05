# Check if a string is a palindrome without using built-in functions and reversing

str = input("Enter anything to verify the palindrome: ")

# without reversing
l = len(str)
# def ispalindrome(str):
#     for i in range(l):
#         if str[i] != str[-(i+1)]:
#             return False
#     return True
#
# # with reversing
# if str == str[::-1]:
#     print("the string is a palindrome")
# else:
#     print("the string is not a palindrome")
#
# print(ispalindrome(str))

left, right = 0, l-1
while left<right:
    if str[left] != str[right]:
        print(False)
    left +=1
    right -=1
