# This is a simple calculator

if __name__ == "__main__":
    print("Hello, User! This is a Calculator app")
    stopper = None
    while stopper != 'q' :
        try:
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))

            print("""Choose the operation you want to perform!
                  For Addition, press '+'
                  For Addition, press '-'
                  For Addition, press '*'
                  For Addition, press '/' """)

            match o := input("Enter operation: "):
                case '+':
                    print("The result is: ", a + b)
                case '-':
                    print("The result is: ", a - b)
                case '*':
                    print("The result is: ", a * b)
                case '/':
                    print("The result is: ", a / b)
                case _:
                    print("Invalid operation please try again!")

        except ValueError:
            print("Don't perform bad typecasting")
        except ZeroDivisionError:
            print("Do not divide by Zero")
        except Exception as e:
            print("Unknown error: ", e)

        finally:
            stopper = input("Press enter to continue or press 'q' to exit!")

    print("Thank you for using our app!")