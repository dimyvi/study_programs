n = int(input())
m = int(input())
mat = set()
inf = set()
for _ in range(n):
    mat.add(input())
for _ in range(m):
    inf.add(input())

print(len(mat ^ inf) if len(mat ^ inf) > 0 else 'NO')