n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
for i in range(n):
    if sorted(matrix[i]) != list(range(1, n + 1)) or sorted([matrix[j][i] for j in range(n)]) != list(range(1, n + 1)):
        print('NO')
        break
else:
    print('YES')