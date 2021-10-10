from typing import List


def common_words(sentence1: List[str], sentence2: List[str]) -> List[str]:
    """
    Input:  Two sentences - each is a  list of words in case insensitive ways.
    Output: those common words appearing in both sentences. Capital and lowercase
            words are treated as the same word.

            If there are duplicate words in the results, just choose one word.
            Returned words should be sorted by word's length.
    """
    common_words_found = [
        word.lower()
        for word in sentence1
        if word.lower() in [w.lower() for w in sentence2]
    ]
    return sorted(set(common_words_found), key=len)
