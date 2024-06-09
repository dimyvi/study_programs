import csv

n = int(input()) - 1

with open('deniro.csv', encoding='utf-8') as file:
    table = list(csv.reader(file))
    if n == 0:
        table.sort(key=lambda x: x[n])
    else:
        table.sort(key=lambda x: int(x[n]))
    for i in table:
        print(*i, sep=',')