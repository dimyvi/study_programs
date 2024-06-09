import csv

# Создаем данные для записи в файл
data = [
    ['first_col', 'second_col'],
    ['value1', 'value2']
]

# Открываем файл для записи
with open('writing_test.csv', 'w', newline='', encoding='utf-8') as csvfile:
    # Создаем объект writer
    writer = csv.writer(csvfile)

    # Записываем данные в файл
    writer.writerows(data)
