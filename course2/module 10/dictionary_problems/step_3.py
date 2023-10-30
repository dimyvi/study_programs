a = ''.join(i.lower() for i in input() if i.isalpha())
b = ''.join(i.lower() for i in input() if i.isalpha())
a = sorted(a)
b = sorted(b)
print(a)
print(b)
if a == b:
    print('YES')
else:
    print('NO')
