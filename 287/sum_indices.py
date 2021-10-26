from typing import List
from collections import defaultdict


def accumulator(arr):
    s = 0
    for i, _ in enumerate(arr):
        s += sum(arr[: i + 1])
    return s


def sum_indices(items: List[str]) -> int:
    item_indexes = defaultdict(list)
    for i, item in enumerate(items):
        item_indexes[item].append(i)
    sums = []
    for idx in item_indexes.values():
        sums.append(accumulator(idx))
    return sum(sums)