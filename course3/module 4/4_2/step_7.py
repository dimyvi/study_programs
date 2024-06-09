import csv

with open('data.csv', encoding='utf-8') as file:
    d = {}
    next(file)
    g = file.read()
    table = [s.split('@')[1] for s in g.splitlines()]
    for name in table:
        d[name] = table.count(name)
    sorted_d = sorted(d.items(), key=lambda item: (item[1], item[0]))

with open('domain_usage.csv',  'w', encoding='utf-8', newline='') as fil:
    writ = csv.writer(fil)
    writ.writerow(['domain', 'count'])
    for ans in sorted_d:
        writ.writerow(ans)