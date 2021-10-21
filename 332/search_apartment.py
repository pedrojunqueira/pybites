from typing import List

EAST = "E"
WEST = "W"


def search_apartment(buildings: List[int], direction: str) -> List[int]:
    """
    Find and return the indices of those building with
    the desired view: EAST (E) or WEST (W).

    See sample inputs / outputs below and in the tests.
    """
    max_hight = 0
    can_see_direction = []
    if direction == WEST:
        for i, building in enumerate(buildings):
            if building > max_hight:
                can_see_direction.append(i)
                max_hight = building
    if direction == EAST:
        for i, building in reversed(list(enumerate(buildings))):
            if building > max_hight:
                can_see_direction.append(i)
                max_hight = building
        can_see_direction = sorted(can_see_direction)
    return can_see_direction


if __name__ == "__main__":
    A = [3, 5, 4, 4, 7, 1, 3, 2]  # central tallest
    B = [1, 1, 1, 1, 1, 2]  # almost flat
    #
    #  W <-                    ->  E(ast)
    #
    print(search_apartment(A, "W"))  # [0, 1, 4]
    print(search_apartment(A, "E"))  # [4, 6, 7]
    print(search_apartment(B, "W"))  # [0, 5]
    print(search_apartment(B, "E"))  # [5]
