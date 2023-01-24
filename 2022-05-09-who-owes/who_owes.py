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
$ 'Clara owes Cassidy $21, Ximena owes Cassidy $15'
"""


def roll_up(receipts):
    """
    From a list of {'name' :, 'paid' :} pairs, create a hash
    table with names for keys, and total paid for
    values.
    >>> receipts = [{ 'name' : 'Ximena', 'paid' : 45 }, { 'name' : 'Clara', 'paid' : 130 }, { 'name' : 'Ximena', 'paid' : 100 }, { 'name' : 'Cassidy', 'paid' : 140 }, { 'name' : 'Cassidy', 'paid' : 76 }, { 'name' : 'Clara', 'paid' : 29 }, { 'name' : 'Ximena', 'paid' : 20 },]
    >>> roll_up(receipts)
    [{'name': 'Ximena', 'paid': 165}, {'name': 'Clara', 'paid': 159}, {'name': 'Cassidy', 'paid': 216}]
    """
    ht = defaultdict(int)
    for receipt in receipts:
        ht[receipt["name"]] += receipt["paid"]

    return [{"name": key, "paid": value} for key, value in ht.items()]


def calculate_over_under(rolled_up):
    """
    >>> calculate_over_under([{'name': 'Ximena', 'paid': 165}, {'name': 'Clara', 'paid': 159}, {'name': 'Cassidy', 'paid': 216}])
    [{'name': 'Ximena', 'paid': 165, 'over_under': 15.0, 'owed': 180.0, 'percent_paid': 0.9166666666666666}, {'name': 'Clara', 'paid': 159, 'over_under': 21.0, 'owed': 180.0, 'percent_paid': 0.8833333333333333}, {'name': 'Cassidy', 'paid': 216, 'over_under': -36.0, 'owed': 180.0, 'percent_paid': 1.2}]
    """
    owed = sum([rup["paid"] for rup in rolled_up]) / len(rolled_up)
    for rup in rolled_up:
        rup["over_under"] = owed - rup["paid"]
        rup["owed"] = owed
        rup["percent_paid"] = rup["paid"] / rup["owed"]

    return rolled_up


def transfer_some_money(ower, owed):
    """
    The ower pays the owed the percent of the owed's over_under
    #>>> transfer_some_money([{'name': 'B', 'paid': 20, 'over_under': -5.0}], [{'name': 'A', 'paid': 10, 'over_under': 5.0}])
    #('A', 'B')
    """
    pct = ower["percent_paid"]
    amount_to_pay = owed["owed"] * (1 - pct)
    return (owed["name"], ower["name"], amount_to_pay)


def who_pays_(rolled_up):
    """
    driver function for who_pays
    """
    rolled_up = sorted(rolled_up, key=lambda x: x["over_under"] < 0)
    transferred = []
    oweds = [x for x in rolled_up if x["over_under"] < 0]
    owers = [x for x in rolled_up if x["over_under"] > 0]
    for ower in owers:
        for owed in oweds:
            transferred.append(transfer_some_money(ower, owed))
    return transferred


def who_pays(receipts):
    """
    >>> who_pays([{'name' : 'Ximena', 'paid' : 45}, {'name' : 'Clara', 'paid' : 130}, {'name' : 'Ximena', 'paid' : 100}, {'name' : 'Cassidy', 'paid' : 140}, {'name' : 'Cassidy', 'paid' : 76}, {'name' : 'Clara', 'paid' : 29}, {'name' : 'Ximena', 'paid' : 20}])
    'Clara owes Cassidy $21.00, Ximena owes Cassidy $15.00'
    """
    rolled_up = roll_up(receipts)
    rolled_up = calculate_over_under(rolled_up)
    return ", ".join(
        [
            f"{payer} owes {payee} ${amount:,.2f}"
            for payee, payer, amount in sorted(who_pays_(rolled_up))
        ]
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
