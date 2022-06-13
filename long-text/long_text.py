"""
Create a loooong teeeext generator that takes in a string and an integer n, 
and multiplies the vowels in the string by n. 

Example: 

$ longText('hello world', 3)
$ 'heeellooo wooorld'

$ longText('lol', 10)
$ 'looooooooool'
"""


def is_vowel(ch):
    """
    >>> is_vowel('a')
    True
    >>> is_vowel('b')
    False
    """
    return ch in ["a", "e", "i", "o", "u", "y"]


def long_text(str, n):
    """
    >>> long_text('hello world', 3)
    'heeellooo wooorld'
    >>> long_text('lol',10)
    'looooooooool'
    >>> long_text('get well soon, Cassidy!', 5)
    'geeeeet weeeeell soooooooooon, Caaaaassiiiiidyyyyy!'
    """
    return "".join([c * n if is_vowel(c) else c for c in str])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
