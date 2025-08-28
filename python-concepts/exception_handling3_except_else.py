# exception without stoping the further execution
for i in range(5):
    try:
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
        print("the division of two number is: ", a/b)

    # except block executes when there is an error in try block
    # exception will not crash the code and continue the process
    except ValueError:
        print("Don't perform bad typecasting")
    except ZeroDivisionError:
        print("Do not divide by Zero")
    except Exception as e:
        print("Unknown error: ", e)

    # else block executes when there is no error in try block
    else:
        print("This prints when there is no error in try block!")


