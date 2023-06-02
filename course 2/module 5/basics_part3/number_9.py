ls = [input().split() for _ in range(int(input()))]
for i in range(len(ls)):
    print(ls[i][0], ls[i][1])

print()

for i in range(len(ls)):
    if ls[i][1] in '45':
        print(ls[i][0], ls[i][1])