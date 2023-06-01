n, m = [int(h) for h in input().split()]
mx1 = [[int(k) for k in input().split()] for _ in range(n)]
p = input()
mx2 = [[int(u) for u in input().split()] for _ in range(n)]

new = []

for i in range(n):
    for j in range(m):
        new.append(mx1[i][j] + mx2[i][j])

for _ in range(n):
    print(*new[:m])
    del new[:m]
