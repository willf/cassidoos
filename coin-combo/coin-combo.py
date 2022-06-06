from itertools import combinations


def power_set(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    return (combo for r in range(len(seq), 0, -1) for combo in combinations(seq, r))


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


if __name__ == "__main__":
    import doctest

    doctest.testmod()
