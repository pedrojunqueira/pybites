import os
from pathlib import Path
from urllib.request import urlretrieve

tmp = Path(os.getenv("TMP", "/tmp"))
timings_log = tmp / "pytest_timings.out"
if not timings_log.exists():
    urlretrieve(
        "https://bites-data.s3.us-east-2.amazonaws.com/pytest_timings.out", timings_log
    )


def get_timings():
    with open(timings_log, "r") as fp:
        data = fp.read()
    return data.splitlines()


def calc_stats(test: str) -> tuple:
    bite = test[0]
    tested = test[2]
    status = test[3]
    total_time = float(test[-3])
    average = float(total_time) / float(tested)
    return (bite, tested, status, total_time, average)


def passing_valid(test):
    return test[2] != "no"


def get_bite_with_fastest_avg_test(timings: list) -> str:
    """Return the bite which has the fastest average time per test"""
    tests = [
        calc_stats(test.split()) for test in timings if passing_valid(test.split())
    ]
    return sorted(tests, key=lambda x: x[4])[0][0]
