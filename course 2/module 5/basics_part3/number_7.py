numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
numbers = [list(i) for i in list(numbers)]
new = []
for j in numbers:
    new.append(sum(j) / len(j))
print(new)
