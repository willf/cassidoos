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


def transfer_some_money(payers, owed):
    """
    >>> transfer_some_money([{'name': 'B', 'paid': 20, 'over_under': -5.0}], [{'name': 'A', 'paid': 10, 'over_under': 5.0}])
    ('A', 'B')
    """
    for owed_person in owed:
        for payer in payers:
            if (
                payer["over_under"] < 0
                and -payer["over_under"] == owed_person["over_under"]
            ):
                payer["over_under"] += owed_person["over_under"]
                owed_person["over_under"] = 0
                return (owed_person["name"], payer["name"])
    raise Exception("No one can pay anyone")


def who_pays_(rolled_up):
    """
    >>> who_pays_([{'name': 'A', 'paid': 20, 'over_under': 5.0}, {'name' : 'B', 'paid' : 10, 'over_under': -5.0}])
    [('A', 'B')]
    """
    rolled_up = sorted(rolled_up, key=lambda x: x["over_under"] < 0)
    transferred = []
    owed = [x for x in rolled_up if x["over_under"] > 0]
    while owed:
        payers = [x for x in rolled_up if x["over_under"] < 0]
        total_underpaid = sum([x["over_under"] for x in payers])
        total_overpaid = sum([x["over_under"] for x in owed])
        assert total_overpaid + total_underpaid == 0
        transferred.append(transfer_some_money(payers, owed))
        owed = [x for x in rolled_up if x["over_under"] > 0]
    return transferred


def who_pays(receipts):
    """
    >>> who_pays([{'name' : 'Ximena', 'paid' : 45}, {'name' : 'Clara', 'paid' : 130}, {'name' : 'Ximena', 'paid' : 100}, {'name' : 'Cassidy', 'paid' : 140}, {'name' : 'Cassidy', 'paid' : 76}, {'name' : 'Clara', 'paid' : 29}, {'name' : 'Ximena', 'paid' : 20}])
    'Clara owes Cassidy $19, Ximena owes Cassidy $17'
    """
    rolled_up = roll_up(receipts)
    rolled_up = calculate_over_under(rolled_up)
    return ", ".join([f"{payer} owns {payee}" for payer, payee in who_pays_(rolled_up)])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
