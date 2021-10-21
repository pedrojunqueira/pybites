import argparse
from functools import reduce
import sys

OPERATIONS = {
    "add": lambda x, y: x + y,
    "sub": lambda x, y: x - y,
    "mul": lambda x, y: x * y,
    "div": lambda x, y: x / y,
}


def calculator(operation, numbers):
    if not numbers:
        sys.exit()
    numbers = [float(number) for number in numbers]
    return reduce(OPERATIONS[operation], numbers)


def create_parser():
    parser = argparse.ArgumentParser(description="a simple calculator")
    parser.add_argument("-a", "--add", help="Sum numbers", nargs="*")
    parser.add_argument("-s", "--sub", help="Subtract numbers", nargs="*")
    parser.add_argument("-m", "--mul", help="Multiply numbers", nargs="*")
    parser.add_argument("-d", "--div", help="Divide numbers", nargs="*")

    return parser


def call_calculator(args=None, stdout=False):
    parser = create_parser()

    if args is None:
        args = parser.parse_args()
        print(args)

    # taking the first operation in args namespace
    # if combo, e.g. -a and -s, take the first one

    for operation, numbers in vars(args).items():
        if numbers is None:
            continue

        try:
            res = calculator(operation, numbers)
        except ZeroDivisionError:
            res = 0

        if stdout:
            print(res)

        return round(res, 2)


if __name__ == "__main__":
    call_calculator(stdout=True)
