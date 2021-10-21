from datetime import datetime, timedelta
import os
import re
import urllib.request

# getting the data
COURSE_TIMES = os.path.join(os.getenv("TMP", "/tmp"), "course_timings")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/course_timings", COURSE_TIMES
)


def get_all_timestamps():
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
    Here is a snippet of the input file:

    Start  What is Practical JavaScript? (3:47)
    Start  The voice in your ear (4:41)
    Start  Is this course right for you? (1:21)
    ...

     Return a list of MM:SS timestamps
    """
    with open(COURSE_TIMES, "r") as fp:
        course_times_txt = fp.read()
    lines = [line for line in course_times_txt.splitlines() if line and line != " "]
    clean_lines = [line for line in lines if ":" in line]
    times = [line.split()[-1].strip("(").strip(")") for line in clean_lines]
    return times


def calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
    and calculates the total duration as HH:MM:SS"""
    total_sec = 0
    for ts in timestamps:
        total_sec += int(ts.split(":")[0]) * 60 + int(ts.split(":")[1])
    delta = timedelta(seconds=total_sec)
    return str(delta)
