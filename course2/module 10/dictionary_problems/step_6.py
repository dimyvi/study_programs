d = {}
for _ in range(int(input())):
    a, b = input().lower().split(' ')
    d[b] = d.get(b, []) + [a]

for _ in range(int(input())):
    s = input().lower()
    if s in d:
        print(*d[s])
    else:
        print('абонент не найден')
