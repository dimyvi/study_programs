from fractions import Fraction
n = int(input())

ls = []
for ch in range(1, n+1):
    for zn in range(1, n+1):
        if ch / zn != 0 and ch < zn and Fraction(ch, zn) not in ls:
            ls.append(Fraction(ch, zn))
ls.sort()
print(*ls, sep='\n')