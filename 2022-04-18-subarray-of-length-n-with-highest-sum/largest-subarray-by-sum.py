# Given an unsorted array of integers and a number n, find the subarray of length n that has the largest sum.
#
#Example:
#
#$ largestSubarraySum([3,1,4,1,5,9,2,6], 3)
#$ [9, 2, 6]

def largestSubarraySum(arr, n):
    """
    Given an unsorted array of integers and a number n, 
    find the subarray of length n that has the largest sum.
    Thows an error if n < 1 or n > len(arr)
    >>> largestSubarraySum([3,1,4,1,5,9,2,6], 3)
    [9, 2, 6]
    >>> largestSubarraySum([3,1,4,1,5,9,2,6], 4)
    [5, 9, 2, 6]
    >>> largestSubarraySum([3,1,4,1,5,9,2,6], 8)
    [3, 1, 4, 1, 5, 9, 2, 6]
    >>> largestSubarraySum([3,1,4,1,5,9,2,6], 100)
    Traceback (most recent call last):
    ...
    ValueError: max() arg is an empty sequence
    >>> largestSubarraySum([3,1,4,1,5,9,2,6], 0)
    Traceback (most recent call last):
    ...
    ValueError: max() arg is an empty sequence
    """
    subarrays = zip(*[arr[i:] for i in range(n)])
    return list(max(subarrays, key=sum))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    