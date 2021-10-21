from functools import reduce


def common_languages(programmers: dict) -> list:
    """Receive a dict of keys -> names and values -> a sequence of
    of programming languages, return the common languages"""
    return list(
        reduce(
            set.intersection,
            [set(languages) for languages in programmers.values() if languages],
        )
    )
