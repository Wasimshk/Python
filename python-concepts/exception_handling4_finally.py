# exception without stoping the further execution

def divide(a, b):
    try:
        return "the division of two number is: ", a/b

    except ZeroDivisionError:
        print("Do not divide by Zero")
        return None
    # currently else block will never execute as we are returning the value in try block
    else:
        print("no issues found")

    # executes everytime before the return statement
    finally:
        print("executes every time even if any of the other blocks are returning something")

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
print(divide(a, b))