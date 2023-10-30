n = input().split(' ')
m = input().split(' ')
print(*sorted(set(n).intersection(set(m))))