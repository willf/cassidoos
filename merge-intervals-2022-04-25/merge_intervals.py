# This week’s question:
# Given an array of intervals, merge the overlapping intervals, and return an array of the resulting intervals.
#
# Example:
#
# $ mergeIntervals([[1,4],[2,6],[8,10],[15,20]])
# $ [[1,6],[8,10],[15,20]]
#
# $ mergeIntervals([[1,2],[2,7]])
# $ [[1,7]]


def merge_two_intervals(interval_1, interval_2):
    """
    Merge two intervals
    >>> merge_two_intervals([1, 2], [2, 7])
    [[1, 7]]
    >>> merge_two_intervals([2, 7], [1, 2])
    [[1, 7]]
    >>> merge_two_intervals([1, 3], [2, 7])
    [[1, 7]]
    >>> merge_two_intervals([2, 7], [1, 3])
    [[1, 7]]
    >>> merge_two_intervals([1, 2], [3, 7])
    [[1, 2], [3, 7]]
    >>> merge_two_intervals([3, 7], [1, 2])
    [[1, 2], [3, 7]]
    >>> merge_two_intervals([1, 7], [2, 3])
    [[1, 7]]
    >>> merge_two_intervals([2, 3], [1, 7])
    [[1, 7]]
    """
    intervals = sorted([interval_1, interval_2], key=lambda x: x[0])
    i1, i2 = intervals
    min1, max1 = i1
    min2, max2 = i2
    if max1 >= min2:
        return [[min(min1, min2), max(max1, max2)]]
    else:
        return [i1, i2]


def merge_intervals(intervals):
    """
    >>> merge_intervals([[1,4],[2,6],[8,10],[15,20]])
    [[1, 6], [8, 10], [15, 20]]
    >>> merge_intervals([[1,2],[2,7]])
    [[1, 7]]
    >>> merge_intervals([])
    []
    >>> merge_intervals([[1, 7]])
    [[1, 7]]
    """
    if len(intervals) <= 1:
        return intervals
    # else
    i1 = intervals[0]
    i2 = intervals[1]
    rest = intervals[2:]
    merged_two = merge_two_intervals(i1, i2)
    if len(merged_two) == 1:
        return merge_intervals(merged_two + rest)
    # else
    i1, i2 = merged_two
    return [i1] + merge_intervals([i2] + rest)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
