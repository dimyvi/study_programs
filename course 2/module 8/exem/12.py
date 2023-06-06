m = int(input())
s = {input() for i in range(int(input()))}

for _ in range(m-1):
    s &= {input() for _ in range(int(input()))}

print(*sorted(s), sep='\n')