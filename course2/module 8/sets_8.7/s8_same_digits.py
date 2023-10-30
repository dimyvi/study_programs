n = set([i for i in input()])
m = set([j for j in input()])
if n.isdisjoint(m):
    print('NO')
else:
    print('YES')