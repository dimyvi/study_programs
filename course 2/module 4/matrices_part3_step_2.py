n = int(input())
mx = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if j == n - i - 1:
            mx[i][j] = 1
        elif i > n - j - 1:
            mx[i][j] = 2
for k in mx:
    print(*k)
