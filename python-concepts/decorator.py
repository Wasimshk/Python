# decorator is a function that takes function as an argument and return a function


def my_decorator(func):
    def wrapper():
        print(".....runs before actual function.....")
        func()
        print(".....runs after actual function.....")
    return wrapper

#  one way
def gift():
    print(".....actual gift....")

decorated_gift = my_decorator(gift)
decorated_gift()

# another way
@my_decorator
def gift():
    print(".....actual gift....")
gift()


# ///////////////////////////////////////////

def my_home_decorator(func):
    def wrapper():
        print("........front decoration.......")
        func()
        print(".....back decoration....")
    return wrapper


@my_home_decorator
def home():
    print("......This is My home.......")

home()


# //////////////////////////////////////////

def money_transfer_decorator(func):
    def wrapper(*args):
        print("transaction is processing")
        func(*args)
        print("You transaction has been complete!")
    return wrapper

# # actual function
# def money_transfer(money):
#     print(f"transfering {money:.2f} rupees")


# function with decorator
@money_transfer_decorator
def money_transfer(money):
    print(f"transfering {money:.2f} rupees")

money = int(input("Please enter the amount to start the transaction:"))
money_transfer(money)