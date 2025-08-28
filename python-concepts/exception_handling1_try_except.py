# exception without stoping the further execution
while True:
    try:
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
        print("the division of two number is: ", a/b)

    # exception will not crash the code and continue the process
    except ValueError:
        print("Don't perform bad typecasting")
    except ZeroDivisionError:
        print("Do not divide by Zero")
    except Exception as e:
        print("Unknown error: ", e)


