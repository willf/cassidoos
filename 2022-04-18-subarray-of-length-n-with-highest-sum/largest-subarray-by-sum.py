# Given an unsorted array of integers and a number n, find the subarray of length n that has the largest sum.
#
#Example:
#
#$ largestSubarraySum([3,1,4,1,5,9,2,6], 3)
#$ [9, 2, 6]
#

# Things I learned:
# 1. How the zip(*arr) works.
# 2. But that zip(*arr) is slower than yielding ngrams directly. about 2x as slow
# 3. the ngrams function is also a lot clearer than the zip(*arr) version.


def ngrams(arr, n):
    '''
    Yields all of the n-grams of an array.

    >>> list(ngrams([1,2,3], 2))
    [[1, 2], [2, 3]]
    >>> list(ngrams([1,2,3], 3))
    [[1, 2, 3]]
    >>> list(ngrams([1,2,3], 4))
    []
    >>> list(ngrams([1,2,3], 0))
    []
    >>> list(ngrams([], 2))
    []
    '''
    for i in range(len(arr) - n + 1):
        a = arr[i:i+n]
        if a: # python yields empty arrays ...
            yield a
        else:
            break
    

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
    subarrays = ngrams(arr, n)
    return list(max(subarrays, key=sum))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
