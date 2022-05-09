from collections import defaultdict
from itertools import groupby

"""
This week’s question:
You went on a vacation with friends. Each of you paid for certain meals 
on the trip for the group. Write a function that determines who owes money 
to whom so that everyone pays equally. 

Example: 

receipts = [
  { 'name' : 'Ximena', 'paid' : 45 },
  { 'name' : 'Clara', 'paid' : 130 },
  { 'name' : 'Ximena', 'paid' : 100 },
  { 'name' : 'Cassidy', 'paid' : 140 },
  { 'name' : 'Cassidy', 'paid' : 76 },
  { 'name' : 'Clara', 'paid' : 29 },
  { 'name' : 'Ximena', 'paid' : 20 },
]

$ whoOwes(receipts)
$ 'Clara owes Cassidy $19, Ximena owes Cassidy $17'
"""


def roll_up(receipts):
    """
  From a list of {'name' :, 'paid' :} pairs, create a hash
  table with names for keys, and total paid for 
  values.
  
  >>> roll_up([{'name' : 'A', 'paid' : 10}, {'name' : 'A', 'paid' : 10}, {'name' : 'B', 'paid' : 10}])
  [{'name': 'A', 'paid': 20}, {'name': 'B', 'paid': 10}]
  """
    ht = defaultdict(int)
    for receipt in receipts:
        ht[receipt["name"]] += receipt["paid"]

    return [{"name": key, "paid": value} for key, value in ht.items()]


def calculate_over_under(rolled_up):
    """
  >>> calculate_over_under([{'name': 'A', 'paid': 20}, {'name' : 'B', 'paid' : 10}])
  [{'name': 'A', 'paid': 20, 'over_under': 5.0}, {'name': 'B', 'paid': 10, 'over_under': -5.0}]
  """
    average = sum([rup["paid"] for rup in rolled_up]) / len(rolled_up)
    for rup in rolled_up:
        rup["over_under"] = rup["paid"] - average
    return rolled_up


def who_pays(rolled_up):
    groups = groupby(rolled_up, lambda x: x["over_under"] < 0)
    owed = groups[False]
    payers = groups[True]
    total_underpaid = sum([x["over_under"] for x in payers])
    total_overpaid = sum([x["over_under"] for x in owned])
    assert total_overpaid + total_underpaid == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
