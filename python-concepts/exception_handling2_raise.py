# raise exception to stop the execution as soon as the condition met
while True:
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    if b == 0:
        raise ZeroDivisionError
    print("the division of two number is: ", a/b)