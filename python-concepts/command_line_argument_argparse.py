# from argparse import ArgumentParser
# parser = ArgumentParser(description="Simple calculator")

import argparse
parser = argparse.ArgumentParser(description="Simple calculator")


# postional arguments
# here the argument has to be in order
parser.add_argument("num1", type=float, help="first number")
parser.add_argument("num2", type=float, help="second number")
parser.add_argument("operation", choices=["add", "sub", "div", "mul"], help="operation to perform")
# CLI
# python .\command_line_argument_argparse.py 5 10 add



# named(optional) arguments (just like keyworded arguments), we will use - or --
# arguments can be in any order, we can use space or = sign to specify key value pairs, and these are optional
# Single dash (-) is usually for short options (-n, -o etc.).
# Double dash (--) is for long options (--num1, --operation).
parser.add_argument("--num1", type=float, help="first number")
parser.add_argument("--num2", type=float, help="second number")
parser.add_argument("--operation", choices=["add", "sub", "div", "mul"], help="operation to perform")
# CLI
# python .\command_line_argument_argparse.py --num2=5 --num1 10 --operation add

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