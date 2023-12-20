from datetime import *


def saturdays_between_two_dates(start, end):
    a = [start, end]
    a.sort()
    ans1 = int(a[0].toordinal())
    ans2 = int(a[1].toordinal())
    ls = [date.fromordinal(i) for i in range(ans1, ans2 + 1) if date.fromordinal(i).isoweekday() == 6]
    return len(ls)