def zellers_congruence(day, month, year):
    if month < 3:
        month += 12
        year -= 1

    q = day
    m = month
    k = year % 100
    j = year // 100

    h = (q + (13 * (m + 1) // 5) + k + (k // 4) + (j // 4) - (2 * j)) % 7

    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return days[h]

import itertools

def take(n, iterable):
    "Return first n items of the iterable as a list."
    return list(itertools.islice(iterable, n))

# An infinite stream of integers: 0, 1, 2, 3...
integers = itertools.count(start=1900)
perfect_years = ("February 1, " + str(year) for year in integers if zellers_congruence(1,2,year) == "Sunday")
for perfect_year in take(28, perfect_years):
    print(perfect_year)
