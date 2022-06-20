from functools import lru_cache


@lru_cache
def fibonacci(n):
    """
    Given a number n, return the fibonacci of n.
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(3)
    2
    >>> fibonacci(4)
    3
    >>> fibonacci(5)
    5
    >>> fibonacci(6)
    8
    >>> fibonacci(9)
    34
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


@lru_cache
def fibs_le_n(n):
    """
    Given a number n, return all the fib numbers up to fib(n)
    >>> fibs_le_n(0)
    []
    >>> fibs_le_n(1)
    [0, 1, 1]
    >>> fibs_le_n(34)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    >>> fibs_le_n(33)
    [0, 1, 1, 2, 3, 5, 8, 13, 21]
    """
    if n == 0:
        return []
    if n == 1:
        return [0, 1, 1]
    return [fibonacci(fib) for fib in range(n) if fibonacci(fib) <= n]


def previous_fibonacci(n):
    """
    Given a Fibonacci number, give the previous Fibonacci number. 
    If the number given is not a Fibonacci number, return -1.

    >>> previous_fibonacci(0)
    -1
    >>> previous_fibonacci(21)
    7
    >>> previous_fibonacci(22)
    -1

    """
    fibs = fibs_le_n(n)

    if len(fibs) == 0:
        return -1
    elif fibs[-1] != n:
        return -1
    else:
        return len(fibs) - 2


if __name__ == "__main__":
    import doctest

    doctest.testmod()

