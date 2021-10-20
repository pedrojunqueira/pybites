from functools import reduce
from typing import Iterable, Set, Any


def intersection(*args: Iterable) -> Set[Any]:
    return (
        set()
        if all(i is None for i in args)
        else reduce(set.intersection, [set(i) for i in args if i])
    )
