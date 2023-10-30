n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

for k in matrix[::-1]:
    print(*k)
