"""
Write a function that determines if all the characters in a given string are unique. 
Can you do this without making any new variables? 
You choose if you want to include capitalization in your consideration for this one, as a fun challenge.

Example:

> allUnique('Cassidy')
> false

> allUnique('cat & dog')
> false

> allUnique('cat+dog')
> true

"""


def all_unique_(items):
    return len(set(items)) == len(items)


def all_unique(string, fold=True):
    """
    Are all the characters in a string unique? 
    >>> all_unique('Cassidy')
    False
    >>> all_unique('cat & dog')
    False
    >>> all_unique('cat+dog')
    True
    >>> all_unique('Cc', fold=False)
    True
    >>> all_unique('Cc', fold=True)
    False
    """
    if fold:
        return all_unique_(string.lower())
    return all_unique_(string)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
