n = int(input())
m = int(input())
mult = [[str(i * j).ljust(3) for i in range(m)] for j in range(n)]
for k in range(len(mult)):
    print(*mult[k])
