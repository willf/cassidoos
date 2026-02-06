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

def nearest_perfect_month_prior(year):
    if zellers_congruence(1,2,year) == "Sunday":
        return year
    else:
        return nearest_perfect_month_prior(year-1)

def nearest_perfect_month_post(year):
    if zellers_congruence(1,2,year) == "Sunday":
        return year
    else:
        return nearest_perfect_month_post(year+1)

def nearest_perfect_months(year):
    prior = nearest_perfect_month_prior(year)
    post = nearest_perfect_month_post(year+1)
    return {"year": year, "prior": str(prior)+ "-02", "post": str(post)+"-02"}

print(nearest_perfect_months(2025))
# {'year': 2025, 'prior': '2015-02', 'post': '2026-02'}
print(nearest_perfect_months(2026))
# {'year': 2026, 'prior': '2026-02', 'post': '2032-02'}
