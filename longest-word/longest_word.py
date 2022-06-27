import regex

"""
Given a string str and a set of words words, find the longest word in words that is a subsequence of str. 

>>> str = "abppplee"
>>> words = {"able", "ale", "apple", "bale", "kangaroo"}
>>> longest_word(str, words)
>>> 'apple'
# "able" and "ale" also work, but are shorter than "apple"
# "bale" has all the right letters, but not in the right order
"""


def convert_to_regex(str):
    """
    >>> str = 'apple'
    >>> convert_to_regex(str) == regex.compile('[^a]*a[^p]*p[^p]*p[^l]*l[^e]*e')
    True
    """
    parts = [f"[^{let}]*{let}" for let in str]
    re = regex.compile("".join(parts))
    return re


def matches(probe, target):
    """
    >>> matches('apple', 'abppplee')
    True
    >>> matches('kangaroo', 'abppplee')
    False
    """
    re = convert_to_regex(probe)
    if re.search(target):
        return True
    return False


def all_matching(probes, target):
    """
    >>> words = {"able", "ale", "apple", "bale", "kangaroo"}
    >>> str = 'abppplee'
    >>> m = set(all_matching(words, str))
    >>> s = {'able', 'ale', 'apple'}
    >>> m == s
    True
    """
    return [probe for probe in probes if matches(probe, target)]


def longest_str(words):
    """
    >>> words = {'able', 'ale', 'apple'}
    >>> longest_str(words)
    'apple'
    """
    sorted_words = sorted(list(words), key=len, reverse=True)
    return sorted_words[0]


def longest_word(str, words):
    """
    >>> str = "abppplee"
    >>> words = {"able", "ale", "apple", "bale", "kangaroo"}
    >>> longest_word(str, words)
    'apple'
    """
    all_words = all_matching(words, str)
    return longest_str(all_words)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
