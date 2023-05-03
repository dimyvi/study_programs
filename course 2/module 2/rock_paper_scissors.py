timur = input().lower()
ruslan = input().lower()
if timur == ruslan:
    print('ничья')
elif timur + ruslan in ['каменьножницы', 'ножницыбумага', 'бумагакамень']:
    print('Тимур')
else:
    print('Руслан')
