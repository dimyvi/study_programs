d = {
    "1": ".,?!:",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
    "0": " "
}
st = ''

for i in input().upper():
    for j in d.items():
        for u in range(len(j[1])):
            if i == j[1][u]:
                st += j[0] * (u + 1)

print(st)
