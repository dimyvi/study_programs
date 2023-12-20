from datetime import date

def get_date_range(start, end):
    ans1 = int(start.toordinal())
    ans2 = int(end.toordinal())
    ls = [date.fromordinal(i) for i in range(ans1, ans2+1)]
    return ls