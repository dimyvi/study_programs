matrix = []
for _ in range(int(input())):
    row = [int(i) for i in input().split()]
    matrix.append(row)

for string in matrix:
    count = 0
    average = (sum(string)) / len(string)
    for value in string:
        if value > average:
            count += 1
    print(count)
