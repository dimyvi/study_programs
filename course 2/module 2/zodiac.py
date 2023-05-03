zodiacs_signs = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь",
                 "Овца"]
year = int(input())
remainder = year % 12
print(zodiacs_signs[remainder])
