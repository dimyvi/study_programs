d = {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}
c = 0
s = [i for i in input()]
for j in s:
    for k, v in d.items():
        if j in v:
            c += k
print(c)