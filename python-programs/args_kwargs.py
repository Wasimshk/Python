# *args (Arbitrary Positional Arguments):
# The *args syntax allows a function to accept a variable number of non-keyworded (positional) arguments.
# When used in a function definition, *args collects all the positional arguments passed during the function call into a tuple.
# The name args is a convention; any valid variable name prefixed with a single asterisk (*) can be used.

# How to pass arguments
# we can pass the aguments in the form of list, tuple, set, dictionary or any number of non-keyworded(positional) arguments, it will store the arguments in tuple

def my_args(normal_var, *myargs):
    print(myargs)
    # prints all the values in tuple args
    # for i in args:
    #     print(i)

normal = "this is a normal argument"
arr = ["a", "b", "c"]
my_set = {1, 2, 3, 4, 5}
my_tuple = (11, 12, 13)
my_list = [22, 33, 44]
my_dict = {"name":"wasim", "age":29, "role":"SDET"}
# print(type(arr))

# ways to pass argument for function has *args
# my_args(normal)
# my_args(normal, *arr)
# my_args(normal, "wasim", "shaikh", 1, 2)
# my_args(normal, *arr, "wasim", "shaikh", 1, 2)
# my_args(normal, arr, "wasim", "shaikh", 1, 2)
# my_args(normal, my_set, my_list, my_tuple, my_dict)
# my_args(normal, *my_dict) #this will store all the keys as a tuple values


# //////////////////////////////////////////////////////////////////////////
# **kwargs (Arbitrary Keyword Arguments):
# The **kwargs syntax allows a function to accept a variable number of keyworded arguments.
# When used in a function definition, **kwargs collects all the keyword arguments passed during the function call into a dictionary, where keys are the argument names and values are their corresponding values.
# The name kwargs is a convention; any valid variable name prefixed with two asterisks (**) can be used.

# We can pass the Kwargs argument in the form of dictionary or any number of keyworded arguments

def my_kwargs(normal, **mykwargs):
    # print(mykwargs)
    for key, value in mykwargs.items():
        print(f"Key: {key} and Value:{value}")

my_dict1 = {"name":"wasim", "age":29, "role":"SDET"}
normal = "this is a normal argument"

# ways to pass argument for function has **kwargs
# my_kwargs(normal, **my_dict1)
my_kwargs(normal, mydict=my_dict1, **my_dict1, timeout=180)