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

# 
#  zip(*[arr[i:] for i in range(n)])
# 

from hashlib import new
from itertools import islice, tee

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

def i_ngrams(arr, n):
    '''
    Yields all of the n-grams of an array.

    >>> list(i_ngrams([1,2,3], 2))
    [(1, 2), (2, 3)]
    >>> list(i_ngrams([1,2,3], 3))
    [(1, 2, 3)]
    >>> list(i_ngrams([1,2,3], 4))
    []
    >>> list(i_ngrams([1,2,3], 0))
    []
    >>> list(i_ngrams([], 2))
    []
    '''
    # zip(*[arr[i:] for i in range(n)])
    return zip(*[islice(arr, i, None) for i in range(n)])

def z_ngrams(arr, n):
    return zip(*[arr[i:] for i in range(n)])
    

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
    #subarrays = i_ngrams(arr, n)
    #return list(max(subarrays, key=sum))
    return largest_subarray_sum(arr, n)

def largest_subarray_sum(arr, n):
    if n < 1 or n > len(arr):
        raise ValueError('max() arg is an empty sequence')
    new_sum = sum(arr[0:n])
    max = new_sum
    max_i = 0
    #print(f'At start: n: {n}, arr: {arr}; {new_sum}; arr[:n]: {arr[:n]}')
    #print(f' range: {list(range(n, len(arr)-n+1))}')
    for i in range(n, len(arr)-n+1):
        #print(f'i: {i}, i+n=1: {i+n-1} arr[i:i+n-1]: {arr[i:i+n-1]}')
        #print(f"Dropping arr[i-n]: {arr[i-n]} ; Adding arr[i+n-1] {arr[i+n-1]}:")
        new_sum = new_sum - arr[i-n] + arr[i+n-1]
        #print(f'new_sum: {new_sum}')
        if new_sum > max:
            max = new_sum
            max_i = i
            #print(f'max: {max}; max_i: {max_i}, max_i+n: {max_i+n}; new_sum: {new_sum}; arr[max_i:max_i+n]: {arr[max_i:max_i+n]}')
    return arr[max_i:max_i+n]

if __name__ == '__main__':
    #import doctest
    #doctest.testmod()
    #exit()
    import pyperf

    def max_zip_ngrams(arr,n):
        return max(z_ngrams(arr, n), key=sum)
    
    def max_izip_ngrams(arr, n):
        return max(i_ngrams(arr, n), key=sum)

    def max_ngrams(arr, n):
        return max(ngrams(arr, n), key=sum)

    def max_largest_subarray_sum(arr, n):
        return largest_subarray_sum(arr, n)


    runner = pyperf.Runner()
    for l in [100, 1000, 10000, 100000, 1000000]:
        for n in [2, 3]:
            arr = list(range(0, l))
            runner.bench_func(f'max_zip_ngrams; length: {l}, ngram_size: {n} ', lambda: max_zip_ngrams(arr, n))
            runner.bench_func(f'max_izip_ngrams; length: {l}, ngram_size: {n} ',lambda: max_izip_ngrams(arr, n))
            runner.bench_func(f'max_ngrams_ngrams; length: {l}, ngram_size: {n} ', lambda:max_ngrams(arr, n))
            runner.bench_func(f'max_largest_subarray_sum; length: {l}, ngram_size: {n} ', lambda: max_largest_subarray_sum(arr, n))

    
