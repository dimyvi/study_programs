import sys

data = [line.strip() for line in sys.stdin]
ans = 0
count = 0

for i in data:
    try:
        ans += float(i)
    except ValueError:
        count += 1

if ans % 1 == 0:
    print(int(ans))
else:
    print(ans)
print(count)
