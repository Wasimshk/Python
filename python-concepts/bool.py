"""
In programming you often need to know if an expression is True or False.

You can evaluate any expression in Python, and get one of two answers, True or False.

When you compare two values, the expression is evaluated and Python returns the Boolean answer:
"""

print(10 > 9)
print(10 == 9)
print(10 < 9)

# conditional
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# Evaluate Values and Variables
print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15
print(bool(x))
print(bool(y))

"""
Most Values are True
Almost any value is evaluated to True if it has some sort of content.
Any number is True, except 0.
Any string list, tuple, set, and dictionary are True, except empty ones.
"""
bool(123)
bool("abc")
bool(["apple", "cherry", "banana"])