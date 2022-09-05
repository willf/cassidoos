"""
This week’s question:
Write a function fromTo that produces a generator, that will produce values in a range.

Usage:

let gen = fromTo(5,7)

> gen()
5
> gen()
6
> gen()
7
> gen()
undefined
"""

def fromToIter(start, end):
    while start <= end:
        yield start
        start += 1

def fromTo(start, end):
    """
    Write a function fromTo that produces a generator, that will produce values in a range.
    >>> gen = fromTo(5,7)
    >>> gen()
    5
    >>> gen()
    6
    >>> gen()
    7
    >>> gen()
    """
    iter = fromToIter(start, end)
    return lambda: next(iter, None)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
