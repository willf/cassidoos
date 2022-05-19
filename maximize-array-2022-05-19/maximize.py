"""
Given two integer arrays of size n, return a new array of size n such that n consists of only unique elements and the sum of all its elements is maximum.

Example:

let arr1 = [7, 4, 10, 0, 1]
let arr2 = [9, 7, 2, 3, 6]

$ maximizedArray(arr1, arr2)
$ [9, 7, 6, 4, 10]
"""


def maximize_array(arr1, arr2):
    """
    >>> arr = maximize_array([7, 4, 10, 0, 1], [9, 7, 2, 3, 6])
    >>> set(arr) == set([9, 7, 6, 4, 10]) and len(arr) == len([9, 7, 6, 4, 10])
    True
    """
    s1 = set(arr1)
    s2 = set(arr2)
    l = sorted(list(s1.union(s2)), reverse=True)
    return l[0 : min(len(arr1), len(arr2))]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
