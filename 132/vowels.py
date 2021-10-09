VOWELS = list('aeiou')


def get_word_max_vowels(text):
    """Get the case insensitive word in text that has most vowels.
       Return a tuple of the matching word and the vowel count, e.g.
       ('object-oriented', 6)"""
    words = text.split()
    vowel_counter = dict()
    for word in words:
       number_of_vowels = 0
       for char in word:
          if char.lower() in VOWELS:
             number_of_vowels += 1
       vowel_counter[word] = number_of_vowels
    max_vowel = (max(vowel_counter, key=vowel_counter.get))
    return max_vowel, vowel_counter[max_vowel]

