letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
         '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---',
         '...--', '....-', '.....', '-....', '--...', '---..', '----.']
# лучше zip() конечно
al = list()
for i in range(len(letters)):
    for j in range(len(morse)):
        if i == j:
            tup = (letters[i], morse[j])
            al.append(tup)
st = list()
for y in input().upper():
    for m in al:
        if y == m[0]:
            st.append(m[1])
print(*st)
