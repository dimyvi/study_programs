n, m = int(input()), int(input())

matrix = [[int(num) for num in input().split()] for num in range(n)]

st = [int(k) for k in input().split()]
a = st[0]
b = st[1]

for i in range(n):
    matrix[i][a], matrix[i][b] = matrix[i][b], matrix[i][a]

for h in matrix:
    print(*h)
