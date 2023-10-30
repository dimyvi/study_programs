st = set()
for _ in range(int(input())):
    st.add(input())
s = input()
if s in st:
    print('REPEAT')
else:
    print('OK')