ls = [input() for _ in range(int(input()) + int(input()))]
st1 = set()
st2 = set()

for i in ls:
    if i in st1:
        st2.add(i)
    else:
        st1.add(i)
print(len(st1 ^ st2) if len(st1 ^ st2) > 0 else 'NO')