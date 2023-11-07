s = input()
d1 = {}
for i in s:
    d1.setdefault(i, str(s.count(i)))

d2 = {}
for _ in range(int(input())):
    num = input().split(': ')
    d2.setdefault(str(num[-1]), num[0])

s2 = ''
for j in s:
    s2 += d1[j]

s3 = ''
for k in s2:
    s3 += d2[k]
print(s3)
