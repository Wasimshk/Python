# Multiline string

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Looping Through a String
for x in "banana":
  print(x)

# String Length
a = "Hello, World!"
print(len(a))

# Check String
txt = "The best things in life are free!"
print("free" in txt)

# Use it in an if statement:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)


# /////////////////////////////////////////////////////
# Slicing

b = "Hello, World!"
print(b[2:5])
# slice from start 
b = "Hello, World!"
print(b[:5])
# slice to the end 
b = "Hello, World!"
print(b[2:])
# Negative Indexing
b = "Hello, World!"
print(b[-5:]) #print orl


# /////////////////////////////////////////////////////
# Modify string

a = "Hello, World!"
print(a.upper())
print(a.lower())

a = " Hello, World! "
print(a.strip()) #remove space from both end
print(a.rstrip()) #remove space at right
print(a.lstrip()) #remove space at left

a = "Hello, World!"
print(a.replace("H", "W"))
print(a.replace("J", "W")) #does not change anything as J is not present

a = "Hello, World!"
print(a.split()) #default split with a white space
print(a.split(",")) #split from the comma

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# /////////////////////////////////////////////////////
# format

age = 29
txt = f"My name is Wasim, I am {age}"
print(txt)

price = 85
txt = f"The price is {price} dollars"
print(txt)
# Display the price with 2 decimals:
price = 85
txt = f"The price is {price:.2f} dollars"
print(txt)
# Perform a math operation in the placeholder, and return the result:
txt = f"The price is {20 * 59} dollars"
print(txt)

# /////////////////////////////////////////////////////////
# escape sequence

#this is unacceptable
# txt = "We are the so-called "Vikings" from the north." 

#this is acceptable
txt = "We are the so-called 'Vikings' from the north." 

# with escape sequence char it is allowed to use same type of quote through out the string
txt = "We are the so-called \"Vikings\" from the north."

'''
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value
'''


# /////////////////////////////////////////////////////////
# string methods
'''
Method	Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
'''