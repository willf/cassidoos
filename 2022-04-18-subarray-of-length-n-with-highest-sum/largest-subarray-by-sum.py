# Given an unsorted array of integers and a number n, find the subarray of length n that has the largest sum.
#
#Example:
#
#$ largestSubarraySum([3,1,4,1,5,9,2,6], 3)
#$ [9, 2, 6]

def largestSubarraySum(arr, n):
    """
    >>> largestSubarraySum([3,1,4,1,5,9,2,6], 3)
    [9, 2, 6]
    >>> largestSubarraySum([3,1,4,1,5,9,2,6], 4)
    [5, 9, 2, 6]
    >>> largestSubarraySum([3,1,4,1,5,9,2,6], 8)
    [3, 1, 4, 1, 5, 9, 2, 6]
    >>> largestSubarraySum([3,1,4,1,5,9,2,6], 100)
    []
    >>> largestSubarraySum([3,1,4,1,5,9,2,6], 0)
    []
    """
    subarrays = list(zip(*[arr[i:] for i in range(n)]))
    if not subarrays:
        return []
    return max(subarrays, key=sum)  

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    