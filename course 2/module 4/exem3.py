n = int(input())
matrix = [['.'] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j or n - i - 1 == j or i == n // 2 or j == n // 2:
            matrix[i][j] = '*'

for i in matrix:
    print(*i)