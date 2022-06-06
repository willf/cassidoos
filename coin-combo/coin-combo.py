from itertools import combinations, product, chain


def power_set(seq):
    """
    Returns all the subsets of this set. This is a generator.
    from 'largest' to 'smallest'
    >>> list(power_set([2, 1]))
    [(2, 1), (2,), (1,), ()]
    """
    for r in range(len(seq), -1, -1):
        for combo in combinations(seq, r):
            yield combo


def coin_combo(coins, total):
    """
    Given an int array coins and an int amount, 
    return an array of coins that add up to amount 
    (and an empty array if it's an impossible combination).

    >>> coins = [2, 3, 5, 7]
    >>> amount = 17
    >>> sorted(coin_combo(coins, amount))
    [2, 3, 5, 7]
    >>> sorted(coin_combo([3, 3, 5], 11))
    [3, 3, 5]
    >>> sorted(coin_combo([25, 10, 10, 10], 30))
    [10, 10, 10]
    >>> sorted(coin_combo([25, 10, 10, 10], 31))
    []
    """
    for set in power_set(sorted(coins, reverse=True)):
        if sum(set) == total:
            return list(set)
    return []


def coin_combo_2(coins, total):
    """
    Given an int array coins and an int amount, 
    return an generator of arrays of coins that add up to amount 
    (and an empty array if it's an impossible combination).

    This is the same as solving:
    n1*c1 + n2*c2 + n3*c3 + ... + nk*ck = total
    where k is the number of coins and ck is the value of coin k.

    probably the intent is to have a unique set of coins that add up to the total.

    so, one way to solve this is to try all possible combinations of coins.
    but, this is not the most efficient way to solve this problem.

    we can set a maximum for n by taking the floor of total/min(coins).
    >>> coins = [2, 3, 5, 7]
    >>> amount = 17
    >>> [2,3,5,7] in list(coin_combo_2(coins, amount))
    True
    >>> [3,3,5] in list(coin_combo_2([3, 5], 11))
    True
    >>> [10, 10, 10] in list(coin_combo_2([25, 10], 30))
    True
    >>> list(coin_combo_2([25, 10], 31))
    []

    """
    max_n = total // min(coins) + 1
    matrix = product(range(max_n), repeat=len(coins))
    for row in matrix:
        check_total = sum(coins[i] * row[i] for i in range(len(coins)))
        if check_total == total:
            yield list(
                chain.from_iterable([[coins[i]] * row[i] for i in range(len(coins))])
            )
    return matrix


if __name__ == "__main__":
    import doctest

    doctest.testmod()
