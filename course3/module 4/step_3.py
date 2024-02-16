from datetime import datetime


def days_difference(date1, date2):
    delta = abs(date2 - date1).days
    return delta


dates = []
while True:
    try:
        date_str = input().strip()
        if not date_str:
            break
        date = datetime.strptime(date_str, "%Y-%m-%d")
        dates.append(date)

difference = days_difference(dates, dates)
print(difference)
