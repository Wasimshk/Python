# Write a program to check if two strings are anagrams (without sorting).

str_set1 = set(input("Enter 1st string: "))
str_set2 = set(input("Enter 2nd string: "))

if str_set1 == str_set2:
    print("the two strings are anagrams")
else:
    print("the two strings are not anagrams")

