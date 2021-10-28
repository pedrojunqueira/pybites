import string
from typing import Tuple
from collections import Counter
from string import whitespace


EXCEPTIONS = ["-", "'"]
ODD = ["_"]


def strip_unwanted(word):
    for char in word:
        if ord(char) <= 64:
            word = word.replace(char, "")
        if ord(char) <= 191 and ord(char) >= 123:
            word = word.replace(char, "")
        if ord(char) >= 247:
            word = word.replace(char, "")
        if char in ODD:
            word = word.replace(char, "")
    return word


def max_letter_word(text: str) -> Tuple[str, str, int]:

    if not isinstance(text, str):
        raise ValueError
    if not text:
        return ("", "", 0)
    words = [
        (
            word,
            Counter(strip_unwanted(word).casefold()).most_common(1)[0]
            if strip_unwanted(word)
            else ("", 0),
        )
        for word in text.split()
    ]
    word, (ch, count) = sorted(words, key=lambda x: x[1][1], reverse=True)[0]
    clean_word = word if any(c in EXCEPTIONS for c in word) else strip_unwanted(word)
    return (clean_word.strip(".'\""), ch, count)
