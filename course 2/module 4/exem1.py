a = input().split()
n = int(input())
new = []
for i in range(n):
    new.append(a[i::n])
print(new)