matrix = []
for _ in range(int(input())):
    row = [int(num) for num in input().split()]
    matrix.append(row)

s1, s2, s3, s4 = 0, 0, 0, 0

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i > j and i < len(matrix) - 1 - j:
            s1 += matrix[i][j]
        elif i > j and i > len(matrix) - 1 - j:
            s2 += matrix[i][j]
        elif i < j and i > len(matrix) - 1 - j:
            s3 += matrix[i][j]
        else:
            if i < j and i < len(matrix) - 1 - j:
                s4 += matrix[i][j]

print('Верхняя четверть:', s4)
print('Правая четверть:', s3)
print('Нижняя четверть:', s2)
print('Левая четверть:', s1)
