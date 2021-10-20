import os
import urllib.request
from functools import reduce

# PREWORK
TMP = os.getenv("TMP", "/tmp")
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(f'{S3}{DICT}', DICTIONARY)

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}

# start coding

def load_words():
    """Load the words dictionary (DICTIONARY constant) into a list and return it"""
    with open(DICTIONARY, "r") as fp:
        text = fp.read()
    return text.splitlines()


def calc_word_value(word):
    """Given a word calculate its value using the LETTER_SCORES dict"""
    word_value = 0
    for c in word:
        if LETTER_SCORES.get(c.upper()):
            word_value += LETTER_SCORES[c.upper()]
    return  word_value


def max_word_value(words):
    """Given a list of words calculate the word with the maximum value and return it"""
    word_values = [ ( word , calc_word_value(word)) for word in words]
    return max(word_values, key=lambda x: x[1])[0]

