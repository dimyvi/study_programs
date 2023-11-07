d = {}
for _ in range(int(input())):
    country_city = [i for i in input().split()]
    for j in country_city[1:]:
        d.setdefault(j, country_city[0])

for _ in range(int(input())):
    s = input()
    print(d[s])