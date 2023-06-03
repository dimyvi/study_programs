tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
tuples = [list(i) for i in tuples]
new_tuples = []
for j in tuples:
    j[-1] = 100
    new_tuples.append(tuple(j))
print(new_tuples)
