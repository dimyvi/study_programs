dnk = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}

rnk = ''
for i in input():
    rnk += dnk[i]
print(rnk)