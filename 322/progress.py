from datetime import datetime, date, timedelta


def days_elapsed():
    return datetime.now().timetuple().tm_yday

def ontrack_reading(books_goal: int, books_read: int,
                    day_of_year: int = None) -> bool:
    read_ratio = books_read/books_goal
    if not day_of_year:
        day_of_year = days_elapsed()
    year_elapsed_ratio = day_of_year/365
    return read_ratio >= year_elapsed_ratio
