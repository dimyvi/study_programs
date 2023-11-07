d = {}
for _ in range(int(input())):
    st = input().split()
    d.setdefault(st[0], st[1])
    d.setdefault(st[1], st[0])
print(d[input()])