import sys

data = [line.strip() for line in sys.stdin]
date_out = [i.strip()[::-1] for i in data]
for x in date_out:
    print(x)