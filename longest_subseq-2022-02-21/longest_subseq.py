import math


def longest_subseq(arr):
    """ 
    Given an array of integers, find the length of the longest sub-sequence 
    such that elements in the sub-sequence are consecutive integers, 
    the consecutive numbers can be in any order. 
    >>> longest_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    10
    >>> longest_subseq([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    10
    >>> longest_subseq([])
    0
    >>> longest_subseq([1])
    1
    >>> longest_subseq([1,3,5,7,9])
    1
    >>> longest_subseq([1,3,5,7,9,10])
    2
    >>> longest_subseq([1, 9, 87, 3, 10, 4, 20, 2, 45])
    4
    >>> longest_subseq([36, 41, 56, 35, 91, 33, 34, 92, 43, 37, 42])
    5
    
    """
    if not arr:
        return 0
    sorted_array = sorted(arr)
    max_length = 1
    current_length = 1
    last = sorted_array[0]
    for i in sorted_array[1:]:
        if i == last + 1:
            current_length += 1
            if current_length > max_length:
                max_length = current_length
        else:
            current_length = 1
        last = i
    return max_length


def longest_subseq_rec(arr):
    """ 
    RECURSIVE VERSION OF longest_subseq
    Given an array of integers, find the length of the longest sub-sequence 
    such that elements in the sub-sequence are consecutive integers, 
    the consecutive numbers can be in any order. 
    >>> longest_subseq_rec([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    10
    >>> longest_subseq_rec([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    10
    >>> longest_subseq_rec([])
    0
    >>> longest_subseq_rec([1])
    1
    >>> longest_subseq_rec([1,3,5,7,9])
    1
    >>> longest_subseq_rec([1,3,5,7,9,10])
    2
    >>> longest_subseq_rec([1, 9, 87, 3, 10, 4, 20, 2, 45])
    4
    >>> longest_subseq_rec([36, 41, 56, 35, 91, 33, 34, 92, 43, 37, 42])
    5    
    """

    def rec(arr, last, current_length, max_length):
        if not arr:
            return max_length

        if arr[0] == last + 1:
            return rec(
                arr[1:], arr[0], current_length + 1, max(max_length, current_length + 1)
            )
        else:
            return rec(arr[1:], arr[0], 1, max(max_length, 1))

    return rec(sorted(arr), math.nan, 0, 0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
