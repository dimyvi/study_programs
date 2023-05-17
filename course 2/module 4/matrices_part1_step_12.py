matrix = []
for string in range(int(input())):
    row = [int(k) for k in input().split()]
    matrix.append(row)

max_number = []
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i >= j:
            max_number.append(matrix[i][j])
print(max(max_number))
