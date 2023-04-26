number = int(input())
if len(str(number)) == 5:
    five_dight_number = [letter for letter in str(number)]
    five_dight_number.reverse()
    print(int(''.join(five_dight_number)))

elif len(str(number)) == 6:
    six_dight_number = [letter for letter in str(number)]
    six_dight_number.reverse()
    print(six_dight_number[-1], ''.join(six_dight_number[:-1:]), sep='')
