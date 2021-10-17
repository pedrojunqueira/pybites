from datetime import timedelta


def get_missing_dates(dates):
    """Receives a range of dates and returns a sequence
    of missing datetime.date objects (no worries about order).

    You can assume that the first and last date of the
    range is always present (assumption made in tests).

    See the Bite description and tests for example outputs.
    """
    sorted_dates = sorted(dates)
    first = sorted_dates[0]
    last = sorted_dates[-1]
    days = (last - first).days
    current_date = first
    all_dates = [current_date + timedelta(days=i) for i in range(days)]
    return [d for d in all_dates if d not in dates]
