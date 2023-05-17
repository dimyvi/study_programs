n, m = int(input()), int(input())
matrix = []
for i in range(n):
    matrix += [[input() for _ in range(m)]]

for k in matrix:
    print(*k)