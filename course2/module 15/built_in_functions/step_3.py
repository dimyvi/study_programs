abscissas = [float(i) ** 2 for i in input().split()]
ordinates = [float(i) ** 2 for i in input().split()]
applicates = [float(i) ** 2 for i in input().split()]
print(all(map(lambda x: True if x[0]+x[1]+x[2] <= 4 else False, zip(abscissas, ordinates, applicates))))