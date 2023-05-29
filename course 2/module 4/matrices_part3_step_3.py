nm = input().split()
mx = []
count = 1
for i in range(int(nm[0])):
    mx.append([])
    for j in range(int(nm[1])):
        mx[i].append(count)
        count += 1
for k in mx:
    print(*k)
