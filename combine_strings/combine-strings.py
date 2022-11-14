# Given a list of strings arr, and a max size n,
# return a new list where the strings (from left to right)
# are joined together with a space, so that each new string is
# less than or equal to the max size.
# For example:
# >>> combine_strings(['abc', 'def', 'ghi'], 7)
# ['abc def', 'ghi']
# >>> combine_strings(['abc', 'def', 'ghi'], 6)
# ['abc', 'def', 'ghi']

def combine_strings_destructive(arr, n):
    """
    >>> combine_strings_destructive(['abc', 'def', 'ghi'], 7)
    ['abc def', 'ghi']
    >>> combine_strings_destructive(['abc', 'def', 'ghi'], 6)
    ['abc', 'def', 'ghi']
    >>> combine_strings_destructive([], 5)
    []
    >>> combine_strings_destructive(['abc', 'def', 'ghi'], 0)
    ['abc', 'def', 'ghi']
    >>> combine_strings_destructive(['abc', 'define', 'ghi', 'jkl'], 6)
    ['abc', 'define', 'ghi', 'jkl']
    """
    if not arr:
        return []
    result = []
    current_string = arr[0]
    for string in arr[1:]:
        if len(current_string) + len(string) + 1 <= n:
            current_string += ' ' + string
        else:
            result.append(current_string)
            current_string = string
    result.append(current_string)
    return result

def combine_strings_recursive(in_array, n, out_array=[]):
    """
    >>> combine_strings_recursive(['abc', 'def', 'ghi'], 7)
    ['abc def', 'ghi']
    >>> combine_strings_recursive(['abc', 'def', 'ghi'], 6)
    ['abc', 'def', 'ghi']
    >>> combine_strings_recursive([], 5)
    []
    >>> combine_strings_recursive(['abc', 'def', 'ghi'], 0)
    ['abc', 'def', 'ghi']
    >>> combine_strings_recursive(['abc', 'define', 'ghi', 'jkl'], 6)
    ['abc', 'define', 'ghi', 'jkl']
    """
    if not in_array:
        return out_array
    if not out_array:
        return combine_strings_recursive(in_array[1:], n, [in_array[0]])
    if len(out_array[-1]) + len(in_array[0]) + 1 <= n:
        return combine_strings_recursive(in_array[1:], n, out_array[:-1] + [out_array[-1] + ' ' + in_array[0]])
    else:
        return combine_strings_recursive(in_array[1:], n, out_array + [in_array[0]])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
