n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
matrix.reverse()
new = []
for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[j][i], end=' ')
    print()
