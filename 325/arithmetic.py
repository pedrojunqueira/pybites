from decimal import Decimal, getcontext, ROUND_HALF_UP
from typing import Generator
import json

VALUES = "[0.1, 0.2, 0.3, 0.005, 0.005, 2.67]"
TEMPLATE = (
    "The sum of {number1} and {number2}, rounded to two decimal places, is {total:.2f}."
)


def calc_sums(values: str = VALUES) -> Generator[str, None, None]:
    """
    Process the above JSON-encoded string of values and calculate the sum of each adjacent pair.

    The output should be a generator that produces a string that recites the calculation for each pair, for example:

        'The sum of 0.1 and 0.2, rounded to two decimal places, is 0.3.'
    """
    getcontext().prec = 3
    getcontext().rounding = ROUND_HALF_UP

    numbers = json.loads(VALUES)
    for i in range(len(numbers) - 1):
        n1 = str(numbers[i])
        n2 = str(numbers[i + 1])
        sum_ = Decimal(n1) + Decimal(n2)
        yield TEMPLATE.format(number1=n1, number2=n2, total=round(sum_, 2))
