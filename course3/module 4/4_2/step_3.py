import csv

with open('sales.csv') as f:
    data = f.read()
    table = [i.split(';') for i in data.splitlines()]
    del table[0]

    ls = [name[0] for name in table if int(name[1]) > int(name[2])]
    for ans in ls:
        print(ans)
