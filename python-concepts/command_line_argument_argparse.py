# from argparse import ArgumentParser
# parser = ArgumentParser(description="Simple calculator")

import argparse
parser = argparse.ArgumentParser(description="Simple calculator")

parser.add_argument("num1", type=float, help="first number")
parser.add_argument("num2", type=float, help="second number")
parser.add_argument("operation", choices=["add", "sub", "div", "mul"], help="operation to perform")

args = parser.parse_args()

print(args)

match args.operation:
    case "add":
        print(f"The result is {args.num1 + args.num2}")
    case "sub":
        print(f"The result is {args.num1 - args.num2}")
    case "mul":
        print(f"The result is {args.num1 * args.num2}")
    case "div":
        print(f"The result is {args.num1 / args.num2}")
    case _:
        print("Please select a valid operation")