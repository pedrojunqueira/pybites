from collections import namedtuple
from datetime import datetime, timedelta

TimeOffset = namedtuple('TimeOffset', 'offset date_str divider')

NOW = datetime.now()
MINUTE, HOUR, DAY = 60, 60*60, 24*60*60
TIME_OFFSETS = (
    TimeOffset(10, 'just now', None),
    TimeOffset(MINUTE, '{} seconds ago', None),
    TimeOffset(2*MINUTE, 'a minute ago', None),
    TimeOffset(HOUR, '{} minutes ago', MINUTE),
    TimeOffset(2*HOUR, 'an hour ago', None),
    TimeOffset(DAY, '{} hours ago', HOUR),
    TimeOffset(2*DAY, 'yesterday', None),
)


def pretty_date(date):
    """Receives a datetime object and converts/returns a readable string
       using TIME_OFFSETS"""
    if not isinstance(date, datetime):
        raise ValueError
    delta = (NOW - date)
    days, seconds = delta.days, delta.seconds
    if days < 0:
        raise ValueError
    print(days, seconds)
    total_seconds = seconds + days*DAY
    to = list(filter(lambda x: total_seconds < x.offset, TIME_OFFSETS))
    if to:
        to = to[0]
        if to.divider:
            return f"{to.date_str.format(int(seconds/to.divider))}"
        if not to.divider:
            return f"{to.date_str if seconds > MINUTE else to.date_str.format(seconds)}"
    else:
        return date.strftime("%m/%d/%y")