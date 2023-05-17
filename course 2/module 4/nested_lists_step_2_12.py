ls = []

for i in input().split():
    if ls and i in ls[-1]:
        ls[-1].append(i)
    else:
        ls.append([i])

print(ls)
