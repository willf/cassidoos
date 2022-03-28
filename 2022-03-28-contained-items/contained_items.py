#
# This week’s question:
# Given a string that represents items as asterisks (*) and compartment walls 
# as pipes (|), a start index, and an end index, return the number of items in a closed compartment.
#
# Example:
# 
# let str = '|**|*|*'
#
# > containedItems(str, 0, 5)
# > 2
# 
# > containedItems(str, 0, 6)
# > 3
#
# > containedItems(str, 1, 7)
# > 1
# Extra credit: What if you had multiple pairs of start and end indices? You can do it in O(n) time!

def contained_items_once(str, start, end):
    """
    Given a string that represents items as asterisks (*) and compartment walls 
    as pipes (|), a start index, and an end index, return the number of items in a closed compartment.

    >>> str = '|**|*|*'
    >>> contained_items_once(str, 0, 5)
    2
    >>> contained_items_once(str, 0, 6)
    3
    >>> contained_items_once(str, 1, 7)
    1
    """
    substr = str[start:end].strip('*')
    splits = substr.split('|')
    return sum(len(s) for s in splits)

def contained_items(str, starts_and_ends):
    """
    Given a string that represents items as asterisks (*) and compartment walls 
    as pipes (|), a start index, and an end index, return the number of items in a closed compartment.

    >>> str = '|**|*|*'
    >>> contained_items(str, [(0, 5), (0, 6), (1, 7)])
    6
    """
    return sum(contained_items_once(str, start, end) for start, end in starts_and_ends)

if __name__ == '__main__':
    import doctest
    doctest.testmod()