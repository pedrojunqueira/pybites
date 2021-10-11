from datetime import date


def get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""
    first_may_week_day = date(year,5,1).weekday()
    first_sunday = 7 - first_may_week_day
    second_sunday = first_sunday + 7
    return date(year, 5, second_sunday)