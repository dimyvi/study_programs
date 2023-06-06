n = int(input())
m = int(input())
mat = set()
inf = set()
for _ in range(n):
    mat.add(input())
for _ in range(m):
    inf.add(input())

print(len(mat - (mat & inf)))