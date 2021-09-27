from collections import namedtuple
from datetime import date, datetime
import json
import os
from pathlib import Path
from typing import List
from urllib.request import urlretrieve


import pytest

from zodiac import (
    get_signs,
    get_sign_with_most_famous_people,
    signs_are_mutually_compatible,
    get_sign_by_date,
    _get_month_int,
)

Sign = namedtuple("Sign", "name compatibility famous_people sun_dates")

# original source: https://zodiacal.herokuapp.com/api
URL = "https://bites-data.s3.us-east-2.amazonaws.com/zodiac.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "zodiac.json")


@pytest.fixture(scope="module")
def signs():
    if not PATH.exists():
        urlretrieve(URL, PATH)
    with open(PATH) as f:
        data = json.loads(f.read())
    return get_signs(data)


def test_return_data(signs):
    assert isinstance(signs, list)
    for s in signs:
        assert s.__class__.__name__ == "Sign"


def test_return_most_famous(signs):
    most_famous = get_sign_with_most_famous_people(signs)
    assert most_famous[0] == "Scorpio"


@pytest.mark.parametrize(
    "combination, result",
    [
        (("Aries", "Taurus"), False),
        (("Aries", "Gemini"), True),
        (("Aries", "Cancer"), False),
        (("Aries", "Leo"), True),
        (("Aries", "Virgo"), False),
        (("Aries", "Libra"), False),
        (("Aries", "Scorpio"), False),
        (("Aries", "Sagittarius"), True),
        (("Aries", "Capricorn"), False),
        (("Aries", "Aquarius"), True),
        (("Aries", "Pisces"), False),
        (("Taurus", "Gemini"), False),
        (("Taurus", "Cancer"), True),
        (("Taurus", "Leo"), False),
        (("Taurus", "Virgo"), True),
        (("Taurus", "Libra"), False),
        (("Taurus", "Scorpio"), False),
        (("Taurus", "Sagittarius"), False),
        (("Taurus", "Capricorn"), True),
        (("Taurus", "Aquarius"), False),
        (("Taurus", "Pisces"), True),
        (("Gemini", "Cancer"), False),
        (("Gemini", "Leo"), False),
        (("Gemini", "Virgo"), False),
        (("Gemini", "Libra"), True),
        (("Gemini", "Scorpio"), False),
        (("Gemini", "Sagittarius"), False),
        (("Gemini", "Capricorn"), False),
        (("Gemini", "Aquarius"), False),
        (("Gemini", "Pisces"), False),
        (("Cancer", "Leo"), False),
        (("Cancer", "Virgo"), False),
        (("Cancer", "Libra"), False),
        (("Cancer", "Scorpio"), True),
        (("Cancer", "Sagittarius"), False),
        (("Cancer", "Capricorn"), False),
        (("Cancer", "Aquarius"), False),
        (("Cancer", "Pisces"), False),
        (("Leo", "Virgo"), False),
        (("Leo", "Libra"), False),
        (("Leo", "Scorpio"), False),
        (("Leo", "Sagittarius"), False),
        (("Leo", "Capricorn"), False),
        (("Leo", "Aquarius"), False),
        (("Leo", "Pisces"), False),
        (("Virgo", "Libra"), False),
        (("Virgo", "Scorpio"), False),
        (("Virgo", "Sagittarius"), False),
        (("Virgo", "Capricorn"), False),
        (("Virgo", "Aquarius"), False),
        (("Virgo", "Pisces"), False),
        (("Libra", "Scorpio"), False),
        (("Libra", "Sagittarius"), False),
        (("Libra", "Capricorn"), False),
        (("Libra", "Aquarius"), False),
        (("Libra", "Pisces"), False),
        (("Scorpio", "Sagittarius"), False),
        (("Scorpio", "Capricorn"), False),
        (("Scorpio", "Aquarius"), False),
        (("Scorpio", "Pisces"), False),
        (("Sagittarius", "Capricorn"), False),
        (("Sagittarius", "Aquarius"), False),
        (("Sagittarius", "Pisces"), False),
        (("Capricorn", "Aquarius"), False),
        (("Capricorn", "Pisces"), False),
        (("Aquarius", "Pisces"), False),
    ],
)
def test_multiple_compatible(signs, combination, result):
    s1, s2 = combination
    assert signs_are_mutually_compatible(signs, s1, s2) == result
    assert signs_are_mutually_compatible(signs, s2, s1) == result

def test_multiple_compatible2(signs):
    assert signs_are_mutually_compatible(signs, "Aquarius", "Pisces") == False



@pytest.mark.parametrize(
    "start, end, name",
    [
        ("April 20", "May 20", "Taurus"),
        ("May 21", "June 20", "Gemini"),
        ("June 21", "July 22", "Cancer"),
        ("July 23", "August 22", "Leo"),
        ("August 23", "September 22", "Virgo"),
        ("September 23", "October 22", "Libra"),
        ("October 23", "November 21", "Scorpio"),
        ("November 22", "December 21", "Sagittarius"),
        ("December 22", "January 19", "Capricorn"),
        ("January 20", "February 18", "Aquarius"),
        ("February 19", "March 20", "Pisces"),
    ],
)
def test_get_sign_by_month(signs, start, end, name):
    m, d = start.split()
    assert get_sign_by_date(signs, date=date(1976, _get_month_int(m), int(d))) == name
    m, d = end.split()
    assert get_sign_by_date(signs, date=date(1976, _get_month_int(m), int(d))) == name
    for s in signs:
        assert s.__class__.__name__ == "Sign"