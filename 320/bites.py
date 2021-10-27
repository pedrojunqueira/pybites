from dataclasses import dataclass
import enum
from typing import List  # TODO: can remove >= 3.9


class BiteLevel(enum.IntEnum):
    INTRO = 1
    BEGINNER = 2
    INTERMEDIATE = 3
    ADVANCED = 4


@dataclass(order=True)
class Bite:
    number: int
    title: str
    level: BiteLevel


def create_bites(numbers: List[int], titles: List[str], levels: List[BiteLevel]):
    """Generate a generator of Bite dataclass objects"""
    for number, title, level in zip(numbers, titles, levels):
        yield Bite(number=number, title=title, level=level)
