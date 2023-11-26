def print_products(*args):
    ls = [i for i in args if type(i) is str and len(i) > 0]
    if len(ls) > 0:
        for j in range(len(ls)):
            print(str(j+1)+')', ls[j])
    else:
        print('Нет продуктов')

print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)