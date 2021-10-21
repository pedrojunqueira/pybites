import random

import pytest

from fizzbuzz import fizzbuzz


def test_meet_3_and_5():
    """
    given: a function
    when: a number at sametime divisible by 3 and 5
    then: return 'Fizz Buzz'
    """
    assert fizzbuzz(15) == "Fizz Buzz"


def test_meet_3():
    """
    given: a function
    when: a number at sametime divisible by 3 and 5
    then: return 'Fizz'
    """
    assert fizzbuzz(3) == "Fizz"


def test_meet_5():
    """
    given: a function
    when: a number divisible by 5
    then: return 'Buzz'
    """
    assert fizzbuzz(5) == "Buzz"


@pytest.mark.parametrize(
    "rand",
    [
        random.choice([i for i in range(100) if i % 3 != 0 and i % 5 != 0]),
        random.choice([i for i in range(100) if i % 3 != 0 and i % 5 != 0]),
        random.choice([i for i in range(100) if i % 3 != 0 and i % 5 != 0]),
        random.choice([i for i in range(100) if i % 3 != 0 and i % 5 != 0]),
    ],
)
def test_others(rand):
    """
    given: a function
    when: a number not divisible by 3 or 5
    then: return 'Buzz'
    """
    assert fizzbuzz(rand) == rand
