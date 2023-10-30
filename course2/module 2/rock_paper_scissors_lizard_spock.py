timur_input = input()
ruslan_input = input()

if timur_input == ruslan_input:
    print('ничья')
elif timur_input + ruslan_input in ["каменьножницы", "каменьящерица", "бумагакамень", "бумагаСпок", "ножницыбумага",
                                    "ножницыящерица", "Спокножницы", "Споккамень", "ящерицаСпок", "ящерицабумага"]:
    print('Тимур')
else:
    print('Руслан')
