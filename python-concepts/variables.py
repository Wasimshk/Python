# Legal variable names: 

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
# //////////////////////////////
# Illegal variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# //////////////////////////////
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# //////////////////////////////
x = y = z = "Orange"
print(x)
print(y)
print(z)

# //////////////////////////////
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# //////////////////////////////
# output
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = "John"
print(x, y)

# error
x = 5
y = "John"
print(x + y)

# //////////////////////////////////////
# Global 

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# //////////////////////////////
# If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# ///////////////////////////////
# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)