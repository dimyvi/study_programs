s = list(input().lower())
st = set()
for j in s:
    if j in '.,;:-?!':
        s.remove(j)
s = ''.join(s)

for i in s.split(' '):
    st.add(i)
print(len(st))
