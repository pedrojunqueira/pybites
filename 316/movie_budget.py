from datetime import date
from typing import Dict, Sequence, NamedTuple


class MovieRented(NamedTuple):
    title: str
    price: int
    date: date


RentingHistory = Sequence[MovieRented]
STREAMING_COST_PER_MONTH = 12
STREAM, RENT = 'stream', 'rent'


def rent_or_stream(
    renting_history: RentingHistory,
    streaming_cost_per_month: int = STREAMING_COST_PER_MONTH
)->Dict[str, str]:
    """Function that calculates if renting movies one by one is
       cheaper than streaming movies by months.

       Determine this PER MONTH for the movies in renting_history.

       Return a dict of:
       keys = months (YYYY-MM)
       values = 'rent' or 'stream' based on what is cheaper

       Check out the tests for examples.
    """
    recommendation = dict()
    for movie in renting_history:
        price, date = movie.price, movie.date
        month = f"{date.year}-{date.month:0>2}"
        recommendation[month] = price if not recommendation.get(month) else recommendation[month] + price
    return { k:("rent" if v <= 12 else "stream") for k, v in recommendation.items()}

