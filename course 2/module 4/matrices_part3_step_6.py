n = int(input())
mx = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == j or j == n - i - 1:
            mx[i][j] = 1
        elif i > j and i > n - j - 1 or j > i and i < n - j - 1:
            mx[i][j] = 1

for k in mx:
    print(*k)
