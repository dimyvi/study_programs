s = input().split()
for j in range(len(s)):
    s[j] = s[j].lstrip('0')

st = set()
for i in s:
    if i in st:
        print('YES')
    else:
        st.add(i)
        print('NO')
