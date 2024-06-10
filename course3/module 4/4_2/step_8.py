import csv

with open('wifi.csv', encoding='utf-8') as file:
    d = {}
    data = file.read()
    table = [i.split(';') for i in data.splitlines()]
    del table[0]
    table.sort(key=lambda x: x[1])

    ans = []
    for area in table:
        if area[1] not in ans:
            ans.append(area[1])

    for name in ans:
        values = []
        for wifi in table:
            if wifi[1] == name:
                values.append(int(wifi[3]))
        d[name] = sum(values)

    sorted_d = sorted(d.items(), key=lambda num: num[1], reverse=True)

    for district, count in sorted_d:
        print(f'{district}: {count}')