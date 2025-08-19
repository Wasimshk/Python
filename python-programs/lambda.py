"""
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

syntax: lambda arguments : expression
"""
print("///////////////////////////////////////////////////////////////")

# Example of a simple lambda function
print((lambda str : str + "\nA. Lambda function")("which function?"))

print((lambda x: x + 10)(5))

x = lambda a : a * 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


# Lambda functions can also be used as arguments to higher-order functions like map, filter, and reduce.
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))

print(myfunc(2)(11))  # Directly calling the lambda function returned by myfunc