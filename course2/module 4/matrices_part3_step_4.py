nm = input().split()
mx = []
count = 1
for i in range(int(nm[1])):
    for j in range(int(nm[0])):
        mx.append([])
        mx[j].append(count)
        count += 1
for k in mx:
    if k != []:
        print(*k)
